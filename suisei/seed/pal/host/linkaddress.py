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
Contains the implementation of the LinkAddress class.
"""

class LinkAddress:

    """
    Representation of a link layer address, e.g. a MAC address of a physical
    network interface.

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

    def __init__(self, address: str) -> None:

        """
        Creates a new LinkAddress instance.

        Authors:
            Attila Kovacs
        """

        self._address = address