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
Contains the unit tests of the Singleton class.
"""

# Platform Imports
import unittest

# Framework Imports
from suisei.seed.utils import Singleton

@Singleton
class TestSingleton:

    """
    Basic test singleton.
    """

    def __init__(self):

        self.testvalue = 'test'

    def testfunction(self):

        """
        Simple test function to test function calling on the singleton.
        """

        self.testvalue = 'modified'

class SingletonTest(unittest.TestCase):

    """
    Test suite for the Singleton annotation.
    """

    @classmethod
    def setUpClass(cls):

        print('')
        print('*******************************************************************************')
        print('     >>>>> Singleton <<<<<')
        print('*******************************************************************************')

    def test_singleton_access(self):

        """
        Test accessing the singleton through the instance method.
        """

        # STEP 1 - Singleton access through the instance() method
        sut = TestSingleton.instance()
        self.assertEqual(sut.testvalue, 'test')

        # STEP 2 - Singleton cannot be accessed outside the instance() method.
        with self.assertRaises(TypeError):
            sut = TestSingleton()

    def test_singleton_function_call(self):

        """
        Test calling functions on the singleton.
        """

        sut = TestSingleton.instance()
        sut.testfunction()
        self.assertEqual(sut.testvalue, 'modified')

    def test_singleton_instance_check(self):

        """
        Test the instance check functionality of the Singleton.
        """

        sut = TestSingleton.instance()
        self.assertEqual(isinstance(sut, TestSingleton), True)

def load_tests(loader, tests, pattern):

    """
    Registers the test suite with the test runner.
    """

    suite = unittest.TestSuite()
    suite.addTest(SingletonTest('test_singleton_access'))
    suite.addTest(SingletonTest('test_singleton_function_call'))
    suite.addTest(SingletonTest('test_singleton_instance_check'))

    return suite
