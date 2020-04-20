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
Contains the implementation of the HostNetworking class.
"""

# Platform Imports
import requests

# SEED Imports
from suisei.seed.exceptions import InvalidInputError
from suisei.seed.log import LogWriter
from .physicalinterface import PhysicalInterface
from .hostlocation import HostLocation

class HostNetworking(LogWriter):

    """
    Utility class that represents the networking capabilities of the host
    system.

    Authors:
        Attila Kovacs
    """

    @property
    def PhysicalInterfaces(self) -> dict:

        """
        Provides access to the identified physical network interfaces of the
        host system.

        Authors:
            Attila Kovacs
        """

        return self._physical_interfaces

    @property
    def PublicIP(self) -> str:

        """
        Provides access to the public IP address of the machine.

        Authors:
            Attila Kovacs
        """

        return self._public_ip

    @property
    def HostLocation(self) -> 'HostLocation':

        """
        Provides access to the host location descriptor.

        Authors:
            Attila Kovacs
        """

        return self._host_location

    def __init__(self,
                 geoip_database_path: str = '/data/geoip') -> None:

        """
        Creates a new HostNetworking instance.

        Args:
            geoip_database_path:    Path to the GeoIP database.

        Authors:
            Attila Kovacs
        """

        super().__init__(channel_name='suisei.seed.pal', cache_entries=True)

        # List of phyisical network interfaces in the host system.
        self._physical_interfaces = {}

        # The public IP address of the host system.
        self._public_ip = None

        # The location descriptor of the public IP address.
        self._host_location = None

        # Path to the GeoIP database to use.
        self._geoip_database_path = geoip_database_path

        self._detect_networking(self._get_interfaces())
        self._detect_public_ip()

    def has_network_interface(self, interface_name: str) -> bool:

        """
        Returns whether or not the given network interface exists.

        Args:
            interface_name:     Name of the network interface to check.

        Returns:
            'True' if the interface exists, 'False' otherwise.

        Authors:
            Attila Kovacs
        """

        if interface_name in self._physical_interfaces:
            return True

        return False

    def _get_interfaces(self) -> list:

        """
        Collects the network interfaces on the host system using netifaces.

        Returns:
            A list of all interfaces found by netifaces.

        Authors:
            Attila Kovacs
        """

        interfaces = []

        try:
            self.debug('Attempting to retrieve network interfaces by using '
                       'netifaces...')
            # Imported here so detection works even without the package
            # installed.
            #pylint: disable=import-outside-toplevel
            import netifaces
            interfaces = netifaces.interfaces()
            self.debug('Network interfaces retrieved successfully.')
        except ImportError:
            self.warning('The netifaces package is not available on '
                         'the host system. Network interfaces cannot be '
                         'retrieved.')

        return interfaces

    def _add_physical_interface(self, nwif: str) -> PhysicalInterface:

        """
        Create the physical interface if it doesn't exist already.

        Args:
            nwif:       The name of the network interface.

        Authors:
            Attila Kovacs
        """

        if not self.has_network_interface(nwif):
            self._create_network_interface(nwif)

        return self._physical_interfaces[nwif]

    def _add_link_addresses(self,
                            physical_interface: PhysicalInterfaces,
                            addresses: list) -> None:

        """
        Adds all link layer addresses to a physical interface.

        Args:
            physical_interface: The PhysicalInterface instance to add to.
            addresses: List of addresses returned by netifaces.

        Authors:
            Attila Kovacs
        """

        try:
            self.debug(f'Adding link layer addresses to interface '
                       f'{physical_interface.Name}')
            # Imported here so detection works even without the package
            # installed.
            #pylint: disable=import-outside-toplevel
            import netifaces
            for address in addresses[netifaces.AF_LINK]:
                physical_interface.add_link_address(address['addr'])
        except KeyError:
            self.debug(f'No link layer addresses found for interface '
                       f'{physical_interface.Name}')
        except ImportError:
            self.warning('The netifaces package is not available on '
                         'the host system. Network interfaces cannot be '
                         'retrieved.')

    def _add_ipv4_addresses(self,
                            physical_interface: PhysicalInterfaces,
                            addresses: list) -> None:

        """
        Adds all IPv4 addresses to a physical interface.

        Args:
            physical_interface: The PhysicalInterface instance to add to.
            addresses: List of addresses returned by netifaces.

        Authors:
            Attila Kovacs
        """

        try:
            self.debug(f'Adding IPv4 addresses to interface '
                       f'{physical_interface.Name}')
            # Imported here so detection works even without the package
            # installed.
            #pylint: disable=import-outside-toplevel
            import netifaces
            for address in addresses[netifaces.AF_INET]:

                # Identify localhost
                is_locahost = False
                if address['addr'].startswith('127.0.0.'):
                    is_locahost = True

                # Identify link local address, according to RFC 3927
                is_link_local = False
                if address['addr'].startswith('169.254'):
                    is_link_local = True

                physical_interface.add_ipv4_address(
                    address=address['addr'],
                    netmask=address['netmask'],
                    broadcast_address=address['broadcast'],
                    is_localhost=is_locahost,
                    is_link_local_address=is_link_local)
        except KeyError:
            self.debug(f'No IPv4 addresses found for interface '
                       f'{physical_interface.Name}')
        except ImportError:
            self.warning('The netifaces package is not available on '
                         'the host system. Network interfaces cannot be '
                         'retrieved.')

    def _add_ipv6_addresses(self,
                            physical_interface: PhysicalInterfaces,
                            addresses: list) -> None:

        """
        Adds all IPv6 addresses to a physical interface.

        Args:
            physical_interface: The PhysicalInterface instance to add to.
            addresses: List of addresses returned by netifaces.

        Authors:
            Attila Kovacs
        """

        try:
            self.debug(f'Adding IPv6 addresses to interface '
                       f'{physical_interface.Name}')
            # Imported here so detection works even without the package
            # installed.
            #pylint: disable=import-outside-toplevel
            import netifaces
            for address in addresses[netifaces.AF_INET6]:

                # Identify localhost
                is_locahost = False
                if address['addr'] == '::1':
                    is_locahost = True

                # Identify link local address, according to RFC 3927
                is_link_local = False
                if address['addr'].startswith('fe80'):
                    is_link_local = True

                physical_interface.add_ipv6_address(
                    address=address['addr'],
                    netmask=address['netmask'],
                    broadcast_address=address['broadcast'],
                    is_localhost=is_locahost,
                    is_link_local_address=is_link_local)
        except KeyError:
            self.debug(f'No IPv6 addresses found for interface '
                       f'{physical_interface.Name}')
        except ImportError:
            self.warning('The netifaces package is not available on '
                         'the host system. Network interfaces cannot be '
                         'retrieved.')

    def _detect_networking(self, interfaces: list) -> None:

        """
        Processes all network interfaces returned by netifaces.

        Args:
            interfaces:     List of network interfaces returned by netifaces.

        Authors:
            Attila Kovacs
        """

        for nwif in interfaces:

            # Create the physical interface if it doesn't exist already
            physical_interface = self._add_physical_interface(nwif)

            # Collect all addresses on the interface
            addresses = []
            try:
                # Imported here so detection works even without the package
                # installed.
                #pylint: disable=import-outside-toplevel
                import netifaces
                addresses = netifaces.ifaddresses(nwif)
            except ImportError:
                self.warning('The netifaces package is not available on '
                             'the host system. Network addresses cannot be '
                             'retrieved.')
                return

            # Link layer addresses
            self._add_link_addresses(physical_interface, addresses)

            # IPv4 addresses
            self._add_ipv4_addresses(physical_interface, addresses)

            # IPv6 addresses
            self._add_ipv6_addresses(physical_interface, addresses)

    def _create_network_interface(self, interface_name: str) -> None:

        """
        Creates a new physical network interface.

        Args:
            interface_name:         Name of the physical interface to create.

        Authors:
            Attila Kovacs
        """

        if self.has_network_interface(interface_name):
            self.warning(f'Physical interface {interface_name} already '
                         f'exists, won\'t be created again.')
            return

        self._physical_interfaces[interface_name] = \
            PhysicalInterface(interface_name)

        self.debug(f'New physical network interface ({interface_name}) has '
                   f'been created.')

    def _detect_public_ip(self) -> None:

        """
        Detects the public IP of the host by calling the ipify API.

        Authors:
            Attila Kovacs
        """

        try:
            ip = requests.get('https://api.ipify.org', timeout=1).text
        except requests.exceptions.Timeout:
            self.warning('Failed to detect public IP. Request timeout.')
            return

        self._public_ip = ip
        self.debug(f'Public IP is detected as {self._public_ip}.')

        try:
            self._host_location = HostLocation(
                public_ip=self._public_ip,
                database_path=self._geoip_database_path)
        except InvalidInputError:
            self.debug('Failed to detect host location. GeoIP databasae is '
                         'not available.')
