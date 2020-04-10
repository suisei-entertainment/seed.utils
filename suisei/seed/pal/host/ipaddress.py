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
Contains the implementation of the IPAddress class.
"""

class IPAddress:

    """
    Representation of an IP address of a physical network interface.

    Authors:
        Attila Kovacs
    """

    @property
    def Address(self) -> str:

        """
        The link address.

        Authors:
            Attila Kovacs
        """

        return self._address

    @property
    def Netmask(self) -> str:

        """
        The netmask associated with the address.

        Authors:
            Attila Kovacs
        """

        return self._netmask

    @property
    def BroadcastAddress(self) -> str:

        """
        The broadcast address associated with the address.

        Authors:
            Attila Kovacs
        """

        return self._broadcast_address

    def __init__(self,
                 address: str,
                 netmask: str,
                 broadcast_address: str,
                 is_localhost: bool = False,
                 is_link_local_address: bool = False) -> None:

        """
        Creates a new IPAddress instance.

        Authors:
            Attila Kovacs
        """

        self._address = address
        self._netmask = netmask
        self._broadcast_address = broadcast_address
        self._is_localhost = is_localhost
        self._is_link_local_address = is_link_local_address

    def is_localhost(self) -> bool:

        """
        Returns whether or not the address represents a localhost address.

        Returns:
            'True' if the address is a localhost address, 'False' otherwise.

        Authors:
            Attila Kovacs
        """

        return self._is_localhost

    def is_link_local_address(self) -> bool:

        """
        Returns whether or not the address represents a link local address.

        Returns:
            'True' if the address is a link local address, 'False' otherwise.

        Authors:
            Attila Kovacs
        """

        return self._is_link_local_address
