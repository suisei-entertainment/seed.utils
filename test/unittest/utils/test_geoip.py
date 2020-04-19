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
Contains the unit tests of GeoIP class.
"""

# Platform Imports
import os
import unittest

# SEED Imports
from suisei.seed.utils import GeoIP, GeoIPData

DATABASE_UPDATE_LINK = \
    'https://download.maxmind.com/app/geoip_download?edition_id=GeoLite2-City&license_key=pELDCVUneMIsHhyU&suffix=tar.gz'

DATABASE_PATH = os.path.abspath(os.path.expanduser('~/.sde/testfiles'))

class GeoIPTest(unittest.TestCase):

    """
    Contains all unit tests of the GeoIP class.
    """

    @classmethod
    def setUpClass(cls):

        print('')
        print('*******************************************************************************')
        print('     >>>>> GeoIP <<<<<')
        print('*******************************************************************************')

        # Delete the database if it's already there
        if os.path.isfile('{}/GeoLite2-City.mmdb'.format(DATABASE_PATH)):
            os.remove('{}/GeoLite2-City.mmdb'.format(DATABASE_PATH))

    def test_creation(self):

        """
        Tests that a GeoIP object can be created.
        """

        sut = GeoIP(update_link=DATABASE_UPDATE_LINK,
                    database_path=DATABASE_PATH)

        self.assertTrue(os.path.isfile(
            '{}/GeoLite2-City.mmdb'.format(DATABASE_PATH)))

    def test_geoip_query(self):

        """
        Tests that IP addresses can be queried.
        """

        sut = GeoIP(update_link=DATABASE_UPDATE_LINK,
                    database_path=DATABASE_PATH)

        # STEP #1 - Query valid IP address
        result = sut.query('5.187.173.113')
        self.assertIsNotNone(result)
        self.assertEqual(result.IPAddress, '5.187.173.113')
        self.assertEqual(result.Continent, 'Europe')
        self.assertEqual(result.Country, 'Hungary')
        self.assertEqual(result.City, 'God')
        self.assertEqual(result.PostalCode, '2132')
        self.assertEqual(result.Latitude, 47.6832)
        self.assertEqual(result.Longitude, 19.1342)

        # STEP #2 - Query internal IP address
        result = sut.query('192.168.0.1')
        self.assertIsNotNone(result)
        self.assertEqual(result.IPAddress, '192.168.0.1')
        self.assertEqual(result.Continent, 'UNKNOWN')
        self.assertEqual(result.Country, 'UNKNOWN')
        self.assertEqual(result.City, 'UNKNOWN')
        self.assertEqual(result.PostalCode, 'UNKNOWN')
        self.assertEqual(result.Latitude, 'UNKNOWN')
        self.assertEqual(result.Longitude, 'UNKNOWN')

def load_tests(loader, tests, pattern):

    """
    Registers the test suite with the test runner.
    """

    suite = unittest.TestSuite()

    suite.addTest(GeoIPTest('test_creation'))
    suite.addTest(GeoIPTest('test_geoip_query'))

    return suite