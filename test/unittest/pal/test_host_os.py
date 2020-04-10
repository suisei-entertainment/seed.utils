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
Contains the unit tests of HostOS class.
"""

# Platform Imports
import platform
import unittest

# SEED Imports
from suisei.seed.pal.host.hostos import HostOS

class HostOSTest(unittest.TestCase):

    """
    Contains the unit tests of HostOS class.
    """

    @classmethod
    def setUpClass(cls):

        print('')
        print('*******************************************************************************')
        print('     >>>>> HostOS <<<<<')
        print('*******************************************************************************')

    def test_creation(self):

        """
        Tests that a HostOS instance can be created.
        """

        sut = HostOS()
        self.assertEqual(sut.Platform, platform.platform())
        self.assertEqual(sut.Name, platform.system())
        self.assertEqual(sut.Release, platform.release())
        self.assertEqual(sut.Version, platform.version())

        if platform.system().lower() == 'linux':
            self.assertNotEqual(sut.Distribution, None)
        else:
            self.assertEqual(sut.Distribution, None)

def load_tests(loader, tests, pattern):

    """
    Registers the test suite with the test runner.
    """

    suite = unittest.TestSuite()

    suite.addTest(HostOSTest('test_creation'))

    return suite
