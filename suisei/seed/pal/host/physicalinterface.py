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
Contains the implementation of the PhysicalInterface class.
"""

# SEED Imports
from suisei.seed.log import LogWriter

from .linkaddress import LinkAddress
from .ipv4address import IPv4Address
from .ipv6address import IPv6Address

class PhysicalInterface(LogWriter):

    """
    Represents a single physical network interface.

    Authors:
        Attila Kovacs
    """

    @property
    def Name(self) -> str:

        """
        Returns the name of the physical interface.

        Authors:
            Attila Kovacs
        """

        return self._name

    def __init__(self, interface_name: str) -> str:

        """
        Creates a new PhysicalInterface instance.

        Args:
            interface_name:     Name of the physical interface.

        Authors:
            Attila Kovacs
        """

        super().__init__(channel_name='suisei.seed.pal', cache_entries=True)

        self._name = interface_name
        """
        Name of the physical interface.
        """

        self._link_addresses = {}
        """
        The list of link layer addresses associated with the interface.
        """

        self._ipv4_addresses = {}
        """
        The list of IPv4 addresses associated with the interface.
        """

        self._ipv6_addresses = {}
        """
        The list of IPv6 addresses associated with the interface.
        """

    def has_link_address(self, address: str) -> bool:

        """
        Returns whether or not the link address already exists in the
        interface.

        Args:
            address:        The link address to check.

        Returns:
            'True' if the given link address is already associated with the
            network interface, 'False' otherwise.

        Authors:
            Attila Kovacs
        """

        if not self._link_addresses:
            return False

        if address in self._link_addresses:
            return True

        return False

    def add_link_address(self, address: str) -> None:

        """
        Adds a new link address to the interface.

        Args:
            address:        The address to add.

        Authors:
            Attila Kovacs
        """

        if self.has_link_address(address):
            self.warning(f'Link address {address} already exists in physical '
                         f'interface {self._name}, won\'t be added twice.')
            return

        self._link_addresses[address] = LinkAddress(address)
        self.debug(f'Link address {address} was added to physical interface '
                   f'{self._name}.')

    def has_ipv4_address(self, address: str) -> bool:

        """
        Returns whether or not the IPv4 already exists in the
        interface.

        Args:
            address:        The IPv4 address to check.

        Returns:
            'True' if the given IPv4 address is already associated with the
            network interface, 'False' otherwise.

        Authors:
            Attila Kovacs
        """

        if not self._ipv4_addresses:
            return False

        if address in self._ipv4_addresses:
            return True

        return False

    def add_ipv4_address(self,
                         address: str,
                         netmask: str,
                         broadcast_address: str,
                         is_localhost: bool = False,
                         is_link_local_address: bool = False) -> None:

        """
        Adds a new IPv4 address to the interface.

        Args:
            address:                The IPv4 address.
            netmask:                The netmask of the address.
            broadcast_address:      The broadcast address associated with the
                                    address.
            is_localhost:           Marks whether or not the address is a
                                    localhost address.
            is_link_local_address:  Marks whether or not the address is a link
                                    local address.

        Authors:
            Attila Kovacs
        """

        if self.has_ipv4_address(address):
            self.warning(f'IPv4 address {address} already exists in physical '
                         f'interface {self._name}, won\'t be added twice.')

        self._ipv4_addresses[address] = IPv4Address(address,
                                                    netmask,
                                                    broadcast_address,
                                                    is_localhost,
                                                    is_link_local_address)
        self.debug(f'IPv4 address {address} was added to physical interface '
                   f'{self._name}.')

    def has_ipv6_address(self, address: str) -> bool:

        """
        Returns whether or not the IPv6 already exists in the
        interface.

        Args:
            address:        The IPv6 address to check.

        Returns:
            'True' if the given IPv6 address is already associated with the
            network interface, 'False' otherwise.

        Authors:
            Attila Kovacs
        """

        if not self._ipv6_addresses:
            return False

        if address in self._ipv6_addresses:
            return True

        return False

    def add_ipv6_address(self,
                         address: str,
                         netmask: str,
                         broadcast_address: str,
                         is_localhost: bool = False,
                         is_link_local_address: bool = False) -> None:

        """
        Adds a new IPv6 address to the interface.

        Args:
            address:                The IPv6 address.
            netmask:                The netmask of the address.
            broadcast_address:      The broadcast address associated with the
                                    address.
            is_localhost:           Marks whether or not the address is a
                                    localhost address.
            is_link_local_address:  Marks whether or not the address is a link
                                    local address.

        Authors:
            Attila Kovacs
        """

        if self.has_ipv6_address(address):
            self.warning(f'IPv6 address {address} already exists in physical '
                         f'interface {self._name}, won\'t be added twice.')

        self._ipv6_addresses[address] = IPv6Address(address,
                                                    netmask,
                                                    broadcast_address,
                                                    is_localhost,
                                                    is_link_local_address)
        self.debug(f'IPv6 address {address} was added to physical interface '
                   f'{self._name}')
