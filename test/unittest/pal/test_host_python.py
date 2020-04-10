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
Contains the unit tests of HostPython class.
"""

# Platform Imports
import sys
import unittest
from unittest.mock import MagicMock

# SEED Imports
from suisei.seed.pal.host.hostpython import HostPython

class HostPythonTest(unittest.TestCase):

    """
    Contains the unit tests of HostPython class.
    """

    @classmethod
    def setUpClass(cls):

        print('')
        print('*******************************************************************************')
        print('     >>>>> HostPython <<<<<')
        print('*******************************************************************************')

    def test_creation(self):

        """
        Tests that a HostPython instance can be created.
        """

        sut = HostPython()
        self.assertEqual(sut.MajorVersion, sys.version_info.major)
        self.assertEqual(sut.MinorVersion, sys.version_info.minor)
        self.assertEqual(sut.PatchLevel, sys.version_info.micro)
        self.assertEqual(sut.PythonVersion,
                         '{}.{}.{}'.format(sys.version_info.major,
                                           sys.version_info.minor,
                                           sys.version_info.micro))
        self.assertEqual(sut.Location, sys.executable)

    def test_virtualenv_detection(self):

        """
        Tests that detecting virtualenv is working.

        This testcase assumes that tests are always executed in a virtualenv
        environment.
        """

        sut = HostPython()
        self.assertEqual(sut.is_virtual_env(), True)

def load_tests(loader, tests, pattern):

    """
    Registers the test suite with the test runner.
    """

    suite = unittest.TestSuite()

    suite.addTest(HostPythonTest('test_creation'))
    suite.addTest(HostPythonTest('test_virtualenv_detection'))

    return suite