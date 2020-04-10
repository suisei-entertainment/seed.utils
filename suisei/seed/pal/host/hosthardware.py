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
Contains the implementation of the HostHardware class.
"""

# SEED Imports
from .hostcpu import HostCPU
from .hostmemory import HostMemory
from .hostnetworking import HostNetworking

class HostHardware:

    """
    Utility class that represents the hardware of the host system.

    Authors:
        Attila Kovacs
    """

    @property
    def CPU(self) -> HostCPU:

        """
        Provides access to the information of the host CPU.

        Authors:
            Attila Kovacs
        """

        return self._cpu

    @property
    def Memory(self) -> HostMemory:

        """
        Provides access to the information of the host memory.

        Authors:
            Attila Kovacs
        """

        return self._memory

    @property
    def Networking(self) -> HostNetworking:

        """
        Provides access to the information of the host's networkig
        capabilities.

        Authors:
            Attila Kovacs
        """

        return self._networking

    def __init__(self) -> None:

        """
        Creates a new HostHardware instance.

        Authors:
            Attila Kovacs
        """

        self._cpu = HostCPU()
        self._memory = HostMemory()
        self._networking = HostNetworking()
