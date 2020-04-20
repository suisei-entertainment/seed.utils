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
Contains the implementation of the HostMemory class.
"""

# SEED Imports
from suisei.seed.log import LogWriter

class HostMemory(LogWriter):

    """
    Utility class that represents the memory of the host system.

    Authors:
        Attila Kovacs
    """

    @property
    def TotalSystemMemory(self) -> str:

        """
        The total amount of system memory in the host system.

        Authors:
            Attila Kovacs
        """

        return self._total_ram

    def __init__(self) -> None:

        """
        Creates a new HostMemory instance.

        Authors:
            Attila Kovacs
        """

        super().__init__(channel_name='suisei.seed.pal', cache_entries=True)

        self._total_ram = 0
        """
        Total amount of system memory.
        """

        self._get_total_ram()

    def _get_total_ram(self) -> None:

        """
        Retrieves the total amount of RAM available on the host system.

        Authors:
            Attila Kovacs
        """

        try:
            self.debug('Attempting to retrieve the total amount of host '
                        'memory through psutil...')
            # Imported here so detection works even without the package
            # installed.
            #pylint: disable=import-outside-toplevel
            import psutil
            memory = psutil.virtual_memory()
            self._total_ram = memory.total
            self.debug(f'Total amount of memory on the host system: '
                       f'{self._total_ram} MB')
        except ImportError:
            self.warning('The psutil library is not available on the host '
                         'system. Memory information cannot be retrieved.')
            self._total_ram = -1
