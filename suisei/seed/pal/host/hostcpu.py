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
Contains the implementation of the HostCPU class.
"""

# Platform Imports
import platform
import multiprocessing

# SEED Imports
from suisei.seed.log import LogWriter

class HostCPU(LogWriter):

    """
    Utility class to inspect the host CPU of the system.

    Authors:
        Attila Kovacs
    """

    @property
    def Architecture(self) -> str:

        """
        The CPU architecture of the host system.

        Authors:
            Attila Kovacs
        """

        return self._architecture

    @property
    def NumCores(self) -> int:

        """
        The amount of CPU cores in the host system, including any virtual
        cores, such as Intel HyperThreading.

        Authors:
            Attila Kovacs
        """

        return self._num_cores

    @property
    def NumPhysicalCores(self) -> int:

        """
        The amount of physical CPU cores in the host system.

        Authors:
            Attila Kovacs
        """

        return self._num_physical_cores

    @property
    def VendorID(self) -> str:

        """
        The vendor ID of the CPU manufacturer.

        Authors:
            Attila Kovacs
        """

        return self._vendor_id

    @property
    def Name(self) -> str:

        """
        The name of the CPU.

        Authors:
            Attila Kovacs
        """

        return self._cpu_name

    @property
    def MaxSpeed(self) -> str:

        """
        The maximum advertised CPU speed.

        Authors:
            Attila Kovacs
        """

        return self._max_speed

    @property
    def L2CacheSize(self) -> int:

        """
        Size of the L2 cache.

        Authors:
            Attila Kovacs
        """

        return self._l2_cache_size

    @property
    def Stepping(self) -> int:

        """
        The stepping of the CPU.

        Authors:
            Attila Kovacs
        """

        return self._stepping

    @property
    def Model(self) -> int:

        """
        The model of the CPU.

        Authors:
            Attila Kovacs
        """

        return self._model

    @property
    def ExtendedModel(self) -> int:

        """
        The extended model of the CPU.

        Authors:
            Attila Kovacs
        """

        return self._extended_model

    @property
    def Family(self) -> int:

        """
        The family of the CPU.

        Authors:
            Attila Kovacs
        """

        return self._family

    def __init__(self) -> None:

        """
        Creates a new HostCPU instance.

        Authors:
            Attila Kovacs
        """

        super().__init__(channel_name='suisei.seed.pal', cache_entries=True)

        self._architecture = ''
        """
        The CPU architecture of the host system.
        """

        self._num_cores = -1
        """
        The amount of CPU cores in the host system, including any virtual
        cores, such as Intel HyperThreading.
        """

        self._num_physical_cores = -1
        """
        The amount of physical CPU cores in the host system.
        """

        self._vendor_id = ''
        """
        The vendor ID of the CPU manufacturer.
        """

        self._cpu_name = ''
        """
        The name of the CPU.
        """

        self._max_speed = ''
        """
        The maximum advertised CPU speed.
        """

        self._l2_cache_size = 0
        """
        Size of the L2 cache.
        """

        self._stepping = ''
        """
        The stepping of the CPU.
        """

        self._model = ''
        """
        The model of the CPU.
        """

        self._extended_model = ''
        """
        The extended model of the CPU.
        """

        self._family = ''
        """
        The family of the CPU.
        """

        self._detect_cpu()

    def _detect_cpu(self) -> None:

        """
        Executes the detection logic of the CPU.

        Authors:
            Attila Kovacs
        """

        info = None

        try:
            # Imported here so detection works even without the package
            # installed.
            #pylint: disable=import-outside-toplevel
            import cpuinfo
            info = cpuinfo.get_cpu_info()
            self.debug('Raw CPU information retrieved from cpuinfo.')
        except ImportError:
            self.warning('The cpuinfo package is not available, only '
                         'fallback methods will be available to retrieve '
                         'information on the host CPU.')
            info = {}

        self._detect_architecture(info)
        self._detect_cpu_count(info)
        self._detect_cpu_type(info)
        self._detect_cpu_speed(info)
        self._detect_cache_data(info)

    def _detect_architecture(self, info: dict) -> None:

        """
        Detection logic for the CPU architecture.

        Args:
            info:       The raw data returned by the cpuinfo package.

        Authors:
            Attila Kovacs
        """

        try:
            self.debug('Attempting to retrieve architecture from raw '
                        'cpuinfo data...')
            self._architecture = info['arch']
            self.debug(f'CPU architecture is identified '
                        f'as {self._architecture}.')
        except KeyError:
            self.debug('Cannot identify CPU architecture from cpuinfo. '
                       'Falling back to platform.')

            self._architecture = platform.machine().upper()

        self.debug(f'CPU architecture is identified as {self._architecture}.')

    def _detect_cpu_count(self, info: dict) -> None:

        """
        Detection logic for the amount of CPU cores.

        Args:
            info:       The raw data returned by the cpuinfo package.

        Authors:
            Attila Kovacs
        """

        # Virtual cores
        try:
            self.debug('Attempting to retrieve the amount of virtual cores '
                       'from raw cpuinfo data...')
            self._num_cores = info['count']
            self.debug(f'Amount of cores detected: {self._num_cores}')
        except KeyError:
            self.debug('Cannot identify the amount of cores from cpuinfo, '
                       'falling back to multiprocessing.')

            self._num_cores = multiprocessing.cpu_count()
            self.debug(f'Amount of cores detected: {self._num_cores}')

        # Physical cores
        try:
            self.debug('Attempting to retrieve the amount of phyisical '
                       'cores from psuitl...')
            # Imported here so detection works even without the package
            # installed.
            #pylint: disable=import-outside-toplevel
            import psutil
            self._num_physical_cores = psutil.cpu_count(logical=False)
            self.debug(f'Amount of physical cores detected: '
                       f'{self._num_physical_cores}')
        except ImportError:
            self.warning('The psutil package is not available on the host '
                         'system, amount of physical CPU cores cannot be '
                         'retrieved.')
            self._num_physical_cores = -1

    def _detect_cpu_type(self, info: dict) -> None:

        """
        Detection logic for the CPU type.

        Args:
            info:       The raw data returned by the cpuinfo package.

        Authors:
            Attila Kovacs
        """

        # Vendor ID
        try:
            self._vendor_id = info['vendor_id']
            self.debug(f'Identified CPU vendor ID: {self._vendor_id}')
        except KeyError:
            self.warning('Failed to detect the vendor ID of the CPU.')
            self._vendor_id = 'UNKNOWN'

        # CPU name
        try:
            self._cpu_name = info['brand']
            self.debug(f'Identified CPU name: {self._cpu_name}')
        except KeyError:
            self.warning('Failed to detect the name of the CPU.')
            self._cpu_name = 'UNKNOWN'

        # CPU stepping
        try:
            self._stepping = info['stepping']
            self.debug(f'Identified CPU stepping: {self._stepping}')
        except KeyError:
            self.warning('Failed to detect the stepping of the CPU.')
            self._stepping = -1

        # CPU model
        try:
            self._model = info['model']
            self.debug(f'Identified CPU model: {self._model}')
        except KeyError:
            self.warning('Failed to detect the model of the CPU.')
            self._model = -1

        # Extended CPU model
        try:
            self._extended_model = info['extended_model']
            self.debug(f'Identified extended CPU model: {self._extended_model}')
        except KeyError:
            self.warning('Failed to detect the extended model of the CPU.')
            self._extended_model = -1

        # CPU family
        try:
            self._family = info['family']
            self.debug(f'Identified CPU family: {self._family}')
        except KeyError:
            self.warning('Failed to detect the family of the CPU.')
            self._family = -1

    def _detect_cpu_speed(self, info: dict) -> None:

        """
        Detection logic for the CPU speed.

        Args:
            info:       The raw data returned by the cpuinfo package.

        Authors:
            Attila Kovacs
        """

        try:
            self._max_speed = info['hz_advertised']
            self.debug(f'Maximum CPU speed: {self._max_speed}')
        except KeyError:
            self.warning('Failed to detect the maximum CPU speed.')
            self._max_speed = 'UNKNOWN'

    def _detect_cache_data(self, info: dict) -> None:

        """
        Detection logic for the CPU cache size.

        Args:
            info:       The raw data returned by the cpuinfo package.

        Authors:
            Attila Kovacs
        """

        try:
            self._l2_cache_size = info['l2_cache_size']
            self.debug(f'Size of the L2 cache: {self._l2_cache_size}')
        except KeyError:
            self.warning('Failed to detect the cache size of the CPU.')
            self._l2_cache_size = 'UNKNOWN'
