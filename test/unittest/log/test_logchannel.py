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
Contains the unit tests of the LogChannel class.
"""

# Platform Imports
import os
import unittest

# SEED Imports
from suisei.seed.log import LogChannel

class LogChannelTest(unittest.TestCase):

    """
    Contains all unit tests of the LogChannel class.
    """

    @classmethod
    def setUpClass(cls):

        print('')
        print('*******************************************************************************')
        print('     >>>>> LogChannel <<<<<')
        print('*******************************************************************************')

    def test_creation(self):

        """
        Tests that a log channel can be created.
        """

        return

def load_tests(loader, tests, pattern):

    """
    Registers the test suite with the test runner.
    """

    suite = unittest.TestSuite()

    suite.addTest(LogChannelTest('test_creation'))

    return suite
