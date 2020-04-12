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
Contains the unit tests of HostLocation class.
"""

# Platform Imports
import os
import unittest
import tarfile
import shutil

# Dependency Imports
import wget

# SEED Imports
from suisei.seed.pal.host.hostlocation import HostLocation
from suisei.seed.exceptions import InvalidInputError

# Constants
DATABASE_PACKAGE_PATH = os.path.abspath(
    os.path.expanduser('/tmp/GeoLite2-City.tar.gz'))

DATABASE_PATH = os.path.abspath(
    os.path.expanduser('~/.sde/testfiles/GeoLite2-City.mmdb'))

DATABASE_DIR = os.path.abspath(
    os.path.expanduser('~/.sde/testfiles'))

class HostLocationTest(unittest.TestCase):

    """
    Contains the unit tests of HostLocation class.
    """

    @classmethod
    def setUpClass(cls):

        def find_mmdb(members):
            for member in members:
                if os.path.splitext(member.name)[1] == '.mmdb':
                    member.name = os.path.basename(member.name)
                    yield member

        print('')
        print('*******************************************************************************')
        print('     >>>>> HostLocation <<<<<')
        print('*******************************************************************************')

        # Download a GeoIP database
        download_url = \
            'https://download.maxmind.com/app/geoip_download?edition_id=GeoLite2-City&license_key=pELDCVUneMIsHhyU&suffix=tar.gz'

        print('')
        print('Downloading GeoIP database...')
        wget.download(url=download_url, out=DATABASE_PACKAGE_PATH)
        print('')
        print('Extracting GeoIP database...')
        tar = tarfile.open(DATABASE_PACKAGE_PATH)
        tar.extractall(path='/tmp', members=find_mmdb(tar))
        tar.close()
        shutil.move(src='/tmp/GeoLite2-City.mmdb', dst=DATABASE_PATH)
        os.remove(DATABASE_PACKAGE_PATH)

    def test_creation(self):

        """
        Tests that a HostLocation instance can be created successfully.
        """

        # STEP #1 - Create with a valid IP, but without a database
        with self.assertRaises(InvalidInputError):
            sut = HostLocation(public_ip='5.187.173.113',
                               database_path='/data')
            self.assertEqual(sut.Continent, 'UNKNOWN')
            self.assertEqual(sut.Country, 'UNKNOWN')
            self.assertEqual(sut.City, 'UNKNOWN')
            self.assertEqual(sut.PostalCode, 'UNKNOWN')
            self.assertEqual(sut.Location, (0,0))

        # STEP #2 - Create with an invalid IP and without a database
        with self.assertRaises(InvalidInputError):
            sut = HostLocation(public_ip='192.168.0.1',
                               database_path='/data')
            self.assertEqual(sut.Continent, 'UNKNOWN')
            self.assertEqual(sut.Country, 'UNKNOWN')
            self.assertEqual(sut.City, 'UNKNOWN')
            self.assertEqual(sut.PostalCode, 'UNKNOWN')
            self.assertEqual(sut.Location, (0,0))

        # STEP #3 - Create with a valid IP and a database
        sut = HostLocation(public_ip='5.187.173.113',
                           database_path=DATABASE_DIR)
        self.assertNotEqual(sut.Continent, 'UNKNOWN')
        self.assertNotEqual(sut.Country, 'UNKNOWN')
        self.assertNotEqual(sut.City, 'UNKNOWN')
        self.assertNotEqual(sut.PostalCode, 'UNKNOWN')
        self.assertNotEqual(sut.Location, (0,0))

        # STEP #4 - Create with an invalid IP and a database
        sut = HostLocation(public_ip='192.168.0.1',
                           database_path=DATABASE_DIR)
        self.assertEqual(sut.Continent, 'UNKNOWN')
        self.assertEqual(sut.Country, 'UNKNOWN')
        self.assertEqual(sut.City, 'UNKNOWN')
        self.assertEqual(sut.PostalCode, 'UNKNOWN')
        self.assertEqual(sut.Location, (0,0))

def load_tests(loader, tests, pattern):

    """
    Registers the test suite with the test runner.
    """

    suite = unittest.TestSuite()

    suite.addTest(HostLocationTest('test_creation'))

    return suite
