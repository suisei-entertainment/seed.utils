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
Contains the implementation of the HostPython class.
"""

# Platform Imports
import sys

class HostPython:

    """
    Utility class that represents the Python environment on the host system.

    Authors:
        Attila Kovacs
    """

    @property
    def MajorVersion(self) -> int:

        """
        The major version of Python on the host system.

        Authors:
            Attila Kovacs
        """

        return self._major

    @property
    def MinorVersion(self) -> int:

        """
        The minor version of Python on the host system.

        Authors:
            Attila Kovacs
        """

        return self._minor

    @property
    def PatchLevel(self) -> int:

        """
        The patch level of Python on the host system.

        Authors:
            Attila Kovacs
        """

        return self._patch

    @property
    def PythonVersion(self) -> str:

        """
        The full version of Python on the host system as a string.

        Authors:
            Attila Kovacs
        """

        return '{}.{}.{}'.format(self._major, self._minor, self._patch)

    @property
    def Location(self) -> str:

        """
        The location of the Python executable on the host system.

        Authors:
            Attila Kovacs
        """

        return self._location

    def __init__(self) -> None:

        """
        Creates a new HostPython instance.
        """

        self._major = -1
        self._minor = -1
        self._patch = -1
        self._location = ''

        self._detect_version()
        self._detect_location()

    @staticmethod
    def is_virtual_env() -> bool:

        """
        Returns whether or not the application was started inside virtualenv.

        Returns:
            'True' if the application is running inside virtualenv, 'False'
            otherwise.

        Authors:
            Attila Kovacs
        """

        if (hasattr(sys, 'real_prefix')) \
           or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
            return True

        return False

    def _detect_version(self) -> None:

        """
        Detection logic for the Python version.

        Authors:
            Attila Kovacs
        """

        self._major = sys.version_info.major
        self._minor = sys.version_info.minor
        self._patch = sys.version_info.micro

    def _detect_location(self) -> None:

        """
        Detects the location of the Python executable on the host system.

        Authors:
            Attila Kovacs
        """

        self._location = sys.executable
