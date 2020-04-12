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
Contains the implementation of the HostDescriptor class.
"""

# Murasame Imports
from .hosthardware import HostHardware
from .hostos import HostOS
from .hostpython import HostPython

class HostDescriptor:

    """
    Utility class that inspects the host system upon creation and stores basic
    system information about it.

    Authors:
        Attila Kovacs
    """

    @property
    def Hardware(self) -> str:

        """
        Provides access to the information of the host hardware.

        Authors:
            Attila Kovacs
        """

        return self._hardware

    @property
    def OS(self) -> str:

        """
        Provides access to the information of the host operating system.

        Authors:
            Attila Kovacs
        """

        return self._os

    @property
    def Python(self) -> HostPython:

        """
        Provides access to the information of the host Python environment.

        Authors:
            Attila Kovacs
        """

        return self._python

    def __init__(self, geoip_database_path: str = '/data/geoip') -> None:

        """
        Creates a new HostDescriptor instance.

        Args:


        Authors:
            Attila Kovacs
        """

        self._hardware = HostHardware(geoip_database_path=geoip_database_path)
        self._os = HostOS()
        self._python = HostPython()
