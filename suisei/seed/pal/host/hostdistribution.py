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
Contains the implementation of the HostDistribution class.
"""

# SEED Imports
from suisei.seed.exceptions import MissingRequirementError

class HostDistribution:

    """
    Utility class that provides additional details on the host OS distribution
    on Unix systems.

    This class requires the distro package to be installed on the host system.

    Authors:
            Attila Kovacs
    """

    @property
    def ID(self) -> str:

        """
        Returns the distro ID of the host operating system's distribution.

        Authors:
            Attila Kovacs
        """

        return self._id

    @property
    def Name(self) -> str:

        """
        Returns the short name of the host operating system's distribution.

        Authors:
            Attila Kovacs
        """

        return self._name

    @property
    def FullName(self) -> str:

        """
        Returns the full name of the host operating system's distribution,
        including the version number and release codename.

        Authors:
            Attila Kovacs
        """

        return self._fullname

    @property
    def MajorVersion(self) -> int:

        """
        Returns the major version of the operating system's distribution.

        Authors:
            Attila Kovacs
        """

        return self._major

    @property
    def MinorVersion(self) -> int:

        """
        Returns the minor version of the operating system's distribution.

        Authors:
            Attila Kovacs
        """

        return self._minor

    @property
    def BuildNumber(self) -> int:

        """
        Returns the build number of the operating system's distribution.

        Authors:
            Attila Kovacs
        """

        return self._build

    @property
    def VersionString(self) -> str:

        """
        Returns the version string of the operating system's distribution.

        Authors:
            Attila Kovacs
        """

        return self._versionstring

    @property
    def Codename(self) -> str:

        """
        Returns the release codename of the operating system's distribution.

        Authors:
            Attila Kovacs
        """

        return self._codename

    @property
    def Like(self) -> str:

        """
        Returns a space separated distribution list that are similar to
        this one.

        Authors:
            Attila Kovacs
        """

        return self._like

    def __init__(self) -> None:

        """
        Creates a new HostDistribution instance.

        Authors:
            Attila Kovacs
        """

        try:
            # Imported here so detection works even without the package
            # installed.
            #pylint: disable=import-outside-toplevel
            import distro
            self._id = distro.id()
            self._name = distro.name(pretty=False)
            self._fullname = distro.name(pretty=True)

            try:
                self._major = int(distro.major_version())
            except ValueError:
                self._major = -1

            try:
                self._minor = int(distro.minor_version())
            except ValueError:
                self._minor = -1

            try:
                self._build = int(distro.build_number())
            except ValueError:
                self._build = -1

            self._versionstring = distro.version(pretty=False)
            self._codename = distro.codename()
            self._like = distro.like()
        except ImportError:
            raise MissingRequirementError(
                'HostDistribution requires the distro package.',
                requirement='distro')
