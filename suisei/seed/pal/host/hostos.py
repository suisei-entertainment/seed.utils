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
Contains the implementation of the HostOS class.
"""

# Platform Imports
import logging
import platform

# SEED Imports
from suisei.seed.exceptions import MissingRequirementError

from .hostdistribution import HostDistribution

class HostOS:

    """
    Utility class that represents the host operating system.

    Authors:
        Attila Kovacs
    """

    @property
    def Platform(self) -> str:

        """
        Name of the host platform.

        Authors:
            Attila Kovacs
        """

        return self._platform

    @property
    def Name(self) -> str:

        """
        Name of the host operating system.

        Authors:
            Attila Kovacs
        """

        return self._os

    @property
    def Release(self) -> str:

        """
        The release name of the host operating system.

        Authors:
            Attila Kovacs
        """

        return self._os_release

    @property
    def Version(self) -> str:

        """
        The version of the host operating system.

        Authors:
            Attila Kovacs
        """

        return self._os_version

    @property
    def Distribution(self) -> HostDistribution:

        """
        Provides access to the detailed distribution information on Linux
        systems.

        Authors:
            Attila Kovacs
        """

        return self._distro

    def __init__(self) -> None:

        """
        Creates a new HostOS instance.

        Authors:
            Attila Kovacs
        """

        self._platform = ''
        """
        Name of the host platform.
        """

        self._os = ''
        """
        Name of the host operating system.
        """

        self._os_release = ''
        """
        The release name of the host operating system.
        """

        self._os_version = ''
        """
        The version of the host operating system.
        """

        self._distro = None
        """
        Contains detailed information on the host Linux distribution.
        """

        self._detect_os()

    def _detect_os(self) -> None:

        """
        Executes the OS detection logic.

        Authors:
            Attila Kovacs
        """

        logger = logging.getLogger('suisei.seed.pal')

        logger.debug('Detecting host operating system...')

        self._platform = platform.platform()
        logger.debug('Host platform is identified as %s', self._platform)

        self._os = platform.system()
        logger.debug('Host operating system is identified as %s', self._os)

        self._os_release = platform.release()
        logger.debug('Host operating system release is identified as %s',
                     self._os_release)

        self._os_version = platform.version()
        logger.debug('Host operating system version is identified as %s',
                     self._os_version)

        # Gather additional information on Linux by using the distro package
        if self._os.lower() == 'linux':
            try:
                self._distro = HostDistribution()
            except MissingRequirementError:
                logger.warning(
                    'The distro package is not installed on the host system, '
                    'not all operating system information can be retrieved.')
