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
Contains the unit tests of HostDistribution class.
"""

# Platform Imports
import unittest

# SEED Imports
from suisei.seed.pal.host.hostdistribution import HostDistribution

class HostDistributionTest(unittest.TestCase):

    """
    Contains the unit tests of HostDistribution class.
    """

    @classmethod
    def setUpClass(cls):

        print('')
        print('*******************************************************************************')
        print('     >>>>> HostDistribution <<<<<')
        print('*******************************************************************************')

    def test_creation(self):

        """
        Tests that a HostDistribution instance can be created.
        """

        sut = HostDistribution()
        self.assertEqual(sut.ID, 'ubuntu')
        self.assertEqual(sut.Name, 'Ubuntu')
        self.assertTrue(sut.FullName.startswith('Ubuntu 18.04') or sut.FullName.startswith('Ubuntu 19.04'))
        self.assertTrue(sut.MajorVersion in (18, 19))
        self.assertEqual(sut.MinorVersion, 4)
        self.assertEqual(sut.BuildNumber, -1)
        self.assertTrue(sut.VersionString in ('18.04', '19.04'))
        self.assertTrue(sut.Codename.lower() in ('bionic', 'disco'))
        self.assertEqual(sut.Like, 'debian')

def load_tests(loader, tests, pattern):

    """
    Registers the test suite with the test runner.
    """

    suite = unittest.TestSuite()

    import platform

    if platform.system().lower() == 'linux':
        suite.addTest(HostDistributionTest('test_creation'))

    return suite
