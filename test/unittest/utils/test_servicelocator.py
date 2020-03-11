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
Contains the unit tests of the service locator design pattern.
"""

# Platform Imports
import os
import sys
import unittest

from suisei.seed.utils import ServiceLocator, Service
from suisei.seed.utils.servicelocator import ServicePath

TEST_SERVICE = \
"""
from suisei.seed.utils import Service, ServiceLocator

class AbstractService:
    def service_function(self):
        pass

class AnotherAbstractService:
    def service_function(self):
        pass

@Service(AbstractService)
class ConcreteService(AbstractService):
    def service_function(self):
        return True
"""

SERVICE_DIR = os.path.abspath(os.path.expanduser('~/.sde/testfiles/services/'))

class ServiceLocatorTest(unittest.TestCase):

    """
    Contains the unit tests of the service locator pattern.
    """

    @classmethod
    def setUpClass(cls):

        print('')
        print('*******************************************************************************')
        print('     >>>>> ServiceLocator <<<<<')
        print('*******************************************************************************')

    def setUp(self):

        # Add .testfiles to the Python path
        sys.path.append(os.path.abspath(os.path.expanduser(
            '~/.sde/testfiles/')))

        if not os.path.isdir(SERVICE_DIR):
            os.mkdir(SERVICE_DIR)

        # Create a test service file
        service_file = '{}/{}'.format(SERVICE_DIR, 'testservice.py')
        with open(service_file, 'w+') as test_file:
            test_file.write(TEST_SERVICE)

        # Create an __init__.py file
        init_file = '{}/{}'.format(SERVICE_DIR, '__init__.py')
        with open(init_file, 'w+') as test_file:
            test_file.write('\n')

    def test_service_path(self):

        """
        Tests that service paths can be created correctly.
        """

        service_path = '/path/to/services'
        service_package = 'path.to.services'

        sut = ServicePath(service_path, service_package)
        self.assertEqual(sut.Path, service_path)
        self.assertEqual(sut.Package, service_package)

    def test_service_discovery(self):

        """
        Tests that service discovery works properly.
        """

        # STEP #1 - Load a valid service path

        # Register the path with the service locator
        ServiceLocator.instance().register_path(SERVICE_DIR, 'services')

        # Run service discovery
        ServiceLocator.instance().discover_services()

        from services.testservice import AbstractService

        self.assertNotEqual(
            ServiceLocator.instance().get_provider(AbstractService),
            None)

        # STEP #2 - Try to load an invalid service path
        ServiceLocator.instance().register_path('/invalid/path', 'services')
        ServiceLocator.instance().discover_services()

        self.assertNotEqual(
            ServiceLocator.instance().get_provider(AbstractService),
            None)

    def test_duplicate_service_path_registration(self):

        """
        Tests that service paths cannot be registered twice.
        """

        ServiceLocator.instance().register_path(SERVICE_DIR, 'services')
        ServiceLocator.instance().register_path(SERVICE_DIR, 'services')
        ServiceLocator.instance().discover_services()

        from services.testservice import AbstractService
        self.assertNotEqual(
            ServiceLocator.instance().get_provider(AbstractService),
            None)

    def test_accessing_services(self):

        """
        Tests that services can be accessed throug the ServiceLocator.
        """

        ServiceLocator.instance().register_path(SERVICE_DIR, 'services')
        ServiceLocator.instance().discover_services()

        from services.testservice import AbstractService
        provider = ServiceLocator.instance().get_provider(AbstractService)
        self.assertNotEqual(provider, None)
        self.assertTrue(provider.service_function())

def load_tests(loader, tests, pattern):

    """
    Registers the test suite with the test runner.
    """

    suite = unittest.TestSuite()

    suite.addTest(ServiceLocatorTest('test_service_path'))
    suite.addTest(ServiceLocatorTest('test_service_discovery'))
    suite.addTest(ServiceLocatorTest(
        'test_duplicate_service_path_registration'))
    suite.addTest(ServiceLocatorTest('test_accessing_services'))

    return suite
