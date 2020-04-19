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
Contains the unit tests of Secrets class.
"""

# Platform Imports
import os
import unittest

# SEED Imports
from suisei.seed.utils import Secrets, JsonFile

# Test data
TEST_CONFIG_DIRECTORY = os.path.abspath(os.path.expanduser('~/.sde/testfiles'))

TEST_DATA = \
{
    'testkey': 'testvalue'
}

TEST_PASSWORD = 'testpassword'

def get_password():
    return TEST_PASSWORD

class SecretsTest(unittest.TestCase):

    """
    Contains all unit tests of the GeoIP class.
    """

    @classmethod
    def setUpClass(cls):

        print('')
        print('*******************************************************************************')
        print('     >>>>> Secrets <<<<<')
        print('*******************************************************************************')

        # Create the test file
        config_file = JsonFile(
            path='{}/secrets.conf'.format(TEST_CONFIG_DIRECTORY),
            cb_retrieve_key=get_password)
        config_file.overwrite_content(content=TEST_DATA)
        config_file.save()

        # Set the environment variable
        os.environ['SEED_SECRETS_KEY'] = TEST_PASSWORD

    def test_creation(self):

        """
        Tests that a GeoIP object can be created.
        """

        sut = Secrets(config_directory=TEST_CONFIG_DIRECTORY)

    def test_query(self):

        """
        Tests that values can be retrieved from the secrets file.
        """

        sut = Secrets(config_directory=TEST_CONFIG_DIRECTORY)
        self.assertEquals(sut.get_secret(key='testkey'), 'testvalue')

def load_tests(loader, tests, pattern):

    """
    Registers the test suite with the test runner.
    """

    suite = unittest.TestSuite()

    suite.addTest(SecretsTest('test_creation'))
    suite.addTest(SecretsTest('test_query'))

    return suite