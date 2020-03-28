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
from suisei.seed.exceptions import InvalidInputError

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

    def test_creation_from_command_map(self) -> None:

        """
        Tests that a CliProcessor object can be created from a command map.
        """

        # STEP #1 - CliProcesor can be created from a command map
        sut = CliProcessor(command_map=TEST_COMMAND_MAP)
        self.assertIsNotNone(sut.Parser)

    def test_creation_from_config_file(self) -> None:

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

    def test_creation_error_handling(self) -> None:

        """
        Tests that errors during object creation work correctly.
        """

        # STEP #1 - Trying to create without command map and config file.
        with self.assertRaises(InvalidInputError):
            sut = CliProcessor(command_map=None, config_file=None)

        # STEP #2 - Fail to parse the command map
        with self.assertRaises(InvalidInputError):
            sut = CliProcessor(command_map={'malformed': 'value'})

        # STEP #3 - Fail to load the configuration from file with fallback
        #           command map.
        with open(TEST_FILE_PATH, 'w') as file:
            file.write('malformed content')

        sut = CliProcessor(command_map=TEST_COMMAND_MAP,
                           config_file=TEST_FILE_PATH)

        # STEP #4 - Fail to load the configuration from file without a fallback
        #           command map.
        with self.assertRaises(InvalidInputError):
            sut = CliProcessor(config_file=TEST_FILE_PATH)

    @staticmethod
    def parser_callback(args: 'argparse.Namespace') -> None:

        """
        Callback function to test argument processing.
        """

        return

    def test_argument_parsing(self) -> None:

        """
        Tests that arguments are parsed correctly.
        """

        sut = CliProcessor(command_map=TEST_COMMAND_MAP)

        arguments = ['--switch-test', '--config-test2', 'testvalue']

        args = sut.process(
            args=arguments,
            cb_argument_processor=CliProcessorTest.parser_callback)

        self.assertTrue(args.switch_test)
        self.assertEquals(args.config_test2, 'testvalue')

        args = sut.process(
            args=arguments,
            cb_argument_processor=CliProcessorTest.parser_callback)

        self.assertTrue(args.switch_test)
        self.assertEquals(args.config_test2, 'testvalue')

def load_tests(loader, tests, pattern):

    """
    Registers the test suite with the test runner.
    """

    suite = unittest.TestSuite()

    suite.addTest(CliProcessorTest('test_creation_from_command_map'))
    suite.addTest(CliProcessorTest('test_creation_from_config_file'))
    suite.addTest(CliProcessorTest('test_creation_error_handling'))
    suite.addTest(CliProcessorTest('test_argument_parsing'))

    return suite