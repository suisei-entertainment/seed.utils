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
Contains the implementation of the GeoIP class.
"""

# Platform Imports
import os
import tarfile
import shutil

# Dependency Imports
import wget

# Path to the temporary location where the update package will be downloaded
PACKAGE_DOWNLOAD_LOCATION = '/tmp/GeoLite2-City.tar.gz'

class GeoIPData:

    """
    Represents the result of a single GeoIP search query.

    Authors:
        Attila Kovacs
    """

    @property
    def IPAddress(self) -> str:

        """
        The IP address whose data is stored.

        Authors:
            Attila Kovacs
        """

        return self._ip_address

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
    def PostalCode(self) -> str:

        """
        The postal code of the city where the IP address is located.

        Authors:
            Attila Kovacs
        """

        return self._postal_code

    @property
    def Latitude(self) -> str:

        """
        The approximate latitude of the location where the IP address is
        located.

        Authors:
            Attila Kovacs
        """

        return self._latitude

    @property
    def Longitude(self) -> str:

        """
        The approximate longitude of the location where the IP address is
        located.

        Authors:
            Attila Kovacs
        """

        return self._longitude

    def __init__(self,
                 ip_address: str,
                 continent: str = 'UNKNOWN',
                 country: str = 'UNKNOWN',
                 city: str = 'UNKNOWN',
                 postal_code: str = 'UNKNOWN',
                 latitude: str = 'UNKNOWN',
                 longitude: str = 'UNKNOWN') -> None:

        """
        Creates a new GeoIPData instance.

        Args:
            ip_address:     The IP address whose data is stored.
            continent:      The continent where the IP address is located.
            country:        The country where the IP address is located.
            city:           The city where the IP address is located.
            postal_code:    The postal code of the city where the IP address is
                            located.
            latitude:       The approximate latitude of the location where the
                            IP address is located.
            longitude:      The approximate longitude of the location where the
                            IP address is located.

        Authors:
            Attila Kovacs
        """

        self._ip_address = ip_address
        """
        The IP address whose data is stored.
        """

        self._continent = continent
        """
        The continent where the IP address is located.
        """

        self._country = country
        """
        The country where the IP address is located.
        """

        self._city = city
        """
        The city where the IP address is located.
        """

        self._postal_code = postal_code
        """
        The postal code of the city where the IP address is located.
        """

        self._latitude = latitude
        """
        The approximate latitude of the location where the IP address is
        located.
        """

        self._longitude = longitude
        """
        The approximate longitude of the location where the IP address is
        located.
        """

class GeoIP:

    """
    Utility class to execute GeoIP queries and database updates.

    Authors:
        Attila Kovacs
    """

    def __init__(self,
                 update_link: str = None,
                 database_path: str = None) -> None:

        """
        Creates a new GeoIP instance.

        Args:
            update_link:        The URL from which the GeoIP database can be
                                downloaded.
            database_path:      Path to the directory where the GeoIP database
                                should be stored.
        """

        # The update link from where the GeoIP database can be downloaded.
        self._update_link = update_link

        # Path to the directory where the GeoIP database will be stored.
        self._database_path = database_path

        # Try to retrieve the database if it doesn't exist.
        if os.path.isfile('{}/GeoLite2-City.mmdb'.format(self._database_path)):
            self.update_database()

    def update_database(self) -> None:

        """
        Updates the GeoIP database.

        Authors:
            Attila Kovacs
        """

        if not self._update_link:
            return

        # Download the update package
        wget.download(url=self._update_link,
                      out=PACKAGE_DOWNLOAD_LOCATION)

        # Extract the update package
        tar = tarfile.open(PACKAGE_DOWNLOAD_LOCATION)
        tar.extractall(path='/tmp', members=GeoIP._find_mmdb)
        tar.close()

        # Move the database to the requested location
        shutil.move(src='/tmp/GeoLite2-City.mmdb',
                    dst='{}/GeoLite2-City.mmdb'.format(self._database_path))

        # Delete the update package
        os.remove(PACKAGE_DOWNLOAD_LOCATION)

    def query(self, ip_address: str) -> GeoIPData:

        """
        Queries the data of the given IP address.

        Args:
            ip_address:     The IP address to look up in the database.

        Returns:
            A GeoIPData object containing the information about the IP address,
            or None, if the IP address was not found in the database.

        Authors:
            Attila Kovacs
        """

        result = None

        if os.path.isfile('{}/GeoLite2-City.mmdb'.format(self._database_path)):
            try:
                response = reader.city(ip_address)
                result = GeoIPData(
                    ip_address=ip_address,
                    continent=response.continent.name,
                    country=response.country.name,
                    city=response.city.name,
                    postal_code=response.postal.code,
                    latitude=response.location.latitude,
                    longitude=response.location.longitude)
            except geoip2.errors.AddressNotFoundError:
                result = GeoIPData(ip_address=ip_address)

        return result

    def _find_mmdb(members: list):

        """
        Finds the GeoIP database inside the downloaded package.

        Args:
            members:        List of files in the update package

        Returns:
            The database file inside the update package.

        Authors:
            Attila Kovacs
        """

        for member in members:
            if os.path.splittext(member.name)[1] == '.mmdb':
                member.name = os.path.basename(member.name)
                yield member
