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
Contains the implementation of the HostLocation class.
"""

# Platform Imports
import os

# Dependency Imports
import geoip2.database

# SEED Imports
from suisei.seed.exceptions import InvalidInputError

class HostLocation:

    """
    Utility class to determine the location of the host based on it's GeoIP
    data.

    At the moment this class uses MaxMind's GeoIP 2 Lite database to determine
    the location of a given IP address.

    Authors:
        Attila Kovacs
    """

    @property
    def Continent(self) -> str:

        """
        The continent where the IP address is located.

        Authors:
            Attila Kovacs
        """

        return self._continent

    @property
    def Country(self) -> str:

        """
        The country where the IP address is located.

        Authors:
            Attila Kovacs
        """

        return self._country

    @property
    def City(self) -> str:

        """
        The city where the IP address is located.

        Authors:
            Attila Kovacs
        """

        return self._city

    @property
    def Location(self) -> tuple:

        """
        The geographical location of the IP address represented as latitude and
        longitude.

        Authors:
            Attila Kovacs
        """

        return self._location

    @property
    def PostalCode(self) -> str:

        """
        The postal code where the IP address is located.

        Authors:
            Attila Kovacs
        """

        return self._postal_code

    def __init__(self, public_ip: str, database_path: str) -> None:

        """
        Creates a new HostLocation instance.

        Args:
            public_ip:          The public IP of the host.
            database_path:      Path to the diretory where the GeoIP database
                                is located.

        Raises:
            InvalidInputError:  Raised if the GeoIP database was not found.

        Authors:
            Attila Kovacs
        """

        # The continent where the IP address is located
        self._continent = 'UNKNOWN'

        # The country where the IP address is located
        self._country = 'UNKNOWN'

        # The city where the UP address is located
        self._city = 'UNKNOWN'

        # The geographical coordinates of the IP address
        self._location = (0,0)

        # The postal code where the IP address is located
        self._postal_code = 'UNKNOWN'

        full_path = os.path.abspath(os.path.expanduser(
            '{}/GeoLite2-City.mmdb'.format(database_path)))

        if not os.path.isfile(full_path):
            raise InvalidInputError('GeoIP database was not found.')

        reader = geoip2.database.Reader(full_path)
        response = reader.city(public_ip)
        if response:
            self._continent = response.continent.name
            self._country = response.country.name
            self._city = response.city.name
            self._postal_code = response.postal.code
            self._location = (
                response.location.latitude,
                response.location.longitude)
