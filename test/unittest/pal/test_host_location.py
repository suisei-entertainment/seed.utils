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
import unittest

# SEED Imports
from suisei.seed.pal.host.hostlocation import HostLocation
from suisei.seed.exceptions import InvalidInputError

class HostLocationTest(unittest.TestCase):

    """
    Contains the unit tests of HostLocation class.
    """

    @classmethod
    def setUpClass(cls):

        print('')
        print('*******************************************************************************')
        print('     >>>>> HostLocation <<<<<')
        print('*******************************************************************************')

    def test_creation(self):

        """
        Tests that a HostLocation instance can be created successfully.
        """

        # STEP #1 - Create with a valid IP, but without a database
        with self.assertRaises(InvalidInputError):
            sut = HostLocation(public_ip='5.187.173.113', database_path='/data')
            self.assertEqual(sut.Continent, 'UNKNOWN')
            self.assertEqual(sut.Country, 'UNKNOWN')
            self.assertEqual(sut.Location, (0,0))
            self.assertEqual(sut.Timezone, 'UNKNOWN')

        # STEP #2 - Create with an invalid IP and without a database
        with self.assertRaises(InvalidInputError):
            sut = HostLocation(public_ip='192.168.0.1', database_path='/data')
            self.assertEqual(sut.Continent, 'UNKNOWN')
            self.assertEqual(sut.Country, 'UNKNOWN')
            self.assertEqual(sut.Location, (0,0))
            self.assertEqual(sut.Timezone, 'UNKNOWN')

        # STEP #3 - Create with a valid IP and a database
        # STEP #4 - Create with an invalid IP and a database

def load_tests(loader, tests, pattern):

    """
    Registers the test suite with the test runner.
    """

    suite = unittest.TestSuite()

    suite.addTest(HostLocationTest('test_creation'))

    return suite