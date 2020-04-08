## ============================================================================
##                   **** SEED Virtual Reality Platform ****
##                Copyright (C) 2019-2020, Suisei Entertainment
## ============================================================================
##
##  This program is free software: you can redistribute it and/or modify
##  it under the terms of the GNU General Public License as published by
##  the Free Software Foundation, either version 3 of the License, or
##  (at your option) any later version.
##
##  This program is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##  GNU General Public License for more details.
##
##  You should have received a copy of the GNU General Public License
##  along with this program.  If not, see <http://www.gnu.org/licenses/>.
##
## ============================================================================

"""
Contains the implementation of the service locator design pattern.
"""

# Platform Imports
import os
import glob
import importlib
import logging

# Murasame Imports
from .singleton import Singleton

class ServicePath:

    """
    Represents a directory that contains the services to be registered in the
    service locator.

    Authors:
        Attila Kovacs
    """

    @property
    def Path(self) -> str:

        """
        The path to the directory where the services are located.

        Authors:
            Attila Kovacs
        """

        return self._path

    @property
    def Package(self) -> str:

        """
        Name of the package to import for importing the service module.

        Authors:
            Attila Kovacs
        """

        return self._package

    def __init__(self, path: str, package: str) -> None:

        """
        Creates a new ServicePath instance.

        Authors:
            Attila Kovacs
        """

        self._path = path
        self._package = package

@Singleton
class ServiceLocator:

    """
    Central class of the service locator pattern. Stores the list of available
    services and handles service disovery.

    This implementation is based on the one by yujanshrestha.
        https://github.com/innolitics/service-locator

    Authors:
        Attila Kovacs
    """

    def __init__(self) -> None:

        """
        Creates a new ServiceLocator instance.

        Authors:
            Attila Kovacs
        """

        self._services = {}
        """
        List of registered srvice providers grouped by the service they
        provide.
        """

        self._service_paths = []
        """
        List of directories where service implementations are stored.
        """

    def register_provider(self, service: object, instance: object) -> None:

        """
        Registers a new service provider for a given service.

        Args:
            service:        The service to register a provider for.
            instance:       The service provider instance to register.

        Authors:
            Attila Kovacs
        """

        providers = self._services.get(service)

        if providers is None:
            providers = []
            self._services[service] = providers

        providers.append(instance)

    def unregister_provider(self, service: object, instance: object) -> None:

        """
        Unregisters a provider from a given service.

        Args:
            service:        The service to unregister the provider from.
            instance:       The service provider instance to unregister.

        Authors:
            Attila Kovacs
        """

        providers = self._services.get(service)

        if providers is not None:
            providers.remove(instance)

        if len(providers) == 0:
            service_object = self._services.get(service)
            if service_object:
                del service_object

    def unregister_all_providers(self, service: object) -> None:

        """
        Unregisters all providers of a given service.

        Args:
            service:        The service to unregister the providers from.

        Authors:
            Attila Kovacs
        """

        service_object = self._services.get(service)
        if service_object:
            del service_object

    def reset(self) -> None:

        """
        Resets the service locator.

        Authors:
            Attila Kovacs
        """

        self._services = {}
        self._service_paths = []

    def get_all_providers(self, service: object) -> list:

        """
        Returns all providers for a given service.

        Args:
            service: The serviec to get the providers for.

        Returns:
            A list of service providers that provide the requested service, or
            an empty list if there are no providers registered that provide
            the requested service.

        Authors:
            Attila Kovacs
        """

        providers = self._services.get(service) or []
        return providers

    def get_provider(self, service: object) -> object:

        """
        Returns a provider for a given service.

        This function will always return the first registered service provider
        for the given service.

        Args:
            service:        The service to get a provider for.

        Returns:
            A provicer for the given service, or None if there are no providers
            registered that provide the requested service.

        Authors:
            Attila Kovacs
        """

        provider = None

        try:
            provider = self.get_all_providers(service)[0]
        except IndexError:
            pass

        return provider

    def has_service_path(self, path: str) -> bool:

        """
        Returns wheter or not the given path is already registered as a service
        path.

        Args:
            path:       The path to check.

        Returns:
            'True' if the given path is already registered, 'False' otherwise.

        Authors:
            Attila Kovacs
        """

        for service_path in self._service_paths:
            if service_path.Path == path:
                return True

        return False

    def register_path(self, path: str, package: str) -> None:

        """
        Registers a new service path with the service locator.

        Args:
            path:       The path to the directory containing the services.
            package:    The package that will be used to include the services
                        inside that path.

        Authors:
            Attila Kovacs
        """

        # Do not register the same path twice.
        if self.has_service_path(path):
            return

        self._service_paths.append(ServicePath(path, package))

    def discover_services(self) -> None:

        """
        Service discovery logic to load all services from all registered
        service paths.

        Authors:
            Attila Kovacs
        """

        for service_path in self._service_paths:

            # Check if the directory exists
            if not os.path.isdir(os.path.abspath(service_path.Path)):
                continue

            # Collect files from the target directory
            current_dir = os.getcwd()
            os.chdir(os.path.abspath(service_path.Path))

            for file in glob.iglob('*.py', recursive=False):

                # Skip __init__.py
                if file.endswith('__init__.py'):
                    continue

                # Import the module
                dummy, filename = os.path.split(file)
                filename, dummy = os.path.splitext(filename)

                import_name = '{}.{}'.format(service_path.Package, filename)

                # Register the service
                importlib.import_module(import_name)

            os.chdir(current_dir)

# Using underscore service here would redefine an existing name
#pylint: disable=invalid-name
def Service(*services):

    """
    Class decorator that declares a class to provide a set of services. It is
    expected that the class has a no-arg constructor and will be instantiated
    as a singleton.

    Args:
        services:       The list of services that the decorated class will
                        provide.

    Authors:
        Attila Kovacs
    """

    def real_decorator(service_class: object) -> object:

        """
        Creates the decorated class.

        Args:
            service_class:      The class that will provide the service.

        Authors:
            Attila Kovacs
        """

        # Pylint doesn't recognize the instance() member from the Singleton
        # decorator.
        # pylint: disable=no-member

        instance = service_class()
        for service in services:
            ServiceLocator.instance().register_provider(service, instance)
        return service_class

    return real_decorator
