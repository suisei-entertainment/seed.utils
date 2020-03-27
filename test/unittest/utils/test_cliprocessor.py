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
Contains the unit tests of the CliProcessor class.
"""

# Platform Imports
import os
import unittest

# SEED Imports
from suisei.seed.utils import CliProcessor, JsonFile

# Test data
TEST_COMMAND_MAP = \
[
    {
        'type': 'group',
        'name': 'test group',
        'description': 'test description',
        'commands':
        [
            {
                'type': 'switch',
                'shortkey': '',
                'command': '--switch-test',
                'help': 'test',
                'default': 'False'
            },
            {
                'type': 'config',
                'shortkey': '-t',
                'command': '--config-test',
                'help': 'test',
                'metavar': 'VALUE'
            }
        ]
    },
    {
        'type': 'switch',
        'shortkey': '',
        'command': '--switch-test2',
        'help': 'test',
        'default': 'False'
    },
    {
        'type': 'config',
        'shortkey': '-c',
        'command': '--config-test2',
        'help': 'test',
        'metavar': 'VALUE'
    }
]

TEST_FILE_PATH = os.path.abspath(os.path.expanduser(
    '~/.sde/testfiles/cli_test.conf'))

class CliProcessorTest(unittest.TestCase):

    """
    Contains all unit tests of the CliProcessor class.
    """

    @classmethod
    def setUpClass(cls):

        print('')
        print('*******************************************************************************')
        print('     >>>>> CliProcessor <<<<<')
        print('*******************************************************************************')

    def test_creation_from_command_map(self):

        """
        Tests that a CliProcessor object can be created from a command map.
        """

        # STEP #1 - CliProcesor can be created from a command map
        sut = CliProcessor(command_map=TEST_COMMAND_MAP)
        self.assertIsNotNone(sut.Parser)

    def test_creation_from_config_file(self):

        """
        Tests that a CliProcessor object can be created from a configuration
        file.
        """

        # STEP #1 - CliProcessor can be created from a config file
        file = JsonFile(path=TEST_FILE_PATH)
        file.overwrite_content(content=TEST_COMMAND_MAP)
        file.save()
        sut = CliProcessor(config_file=TEST_FILE_PATH)
        self.assertIsNotNone(sut.Parser)

def load_tests(loader, tests, pattern):

    """
    Registers the test suite with the test runner.
    """

    suite = unittest.TestSuite()

    suite.addTest(CliProcessorTest('test_creation_from_command_map'))
    suite.addTest(CliProcessorTest('test_creation_from_config_file'))

    return suite