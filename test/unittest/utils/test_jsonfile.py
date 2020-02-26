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
Contains the unit tests of the JsonFile class.
"""

# Platform Imports
import os
import unittest

# Framework Imports
from suisei.seed.exceptions import InvalidInputError
from suisei.seed.utils import JsonFile

TEST_FILE_PATH = os.path.abspath('./.sde/testfiles/json_test.json')

INVALID_TEST_FILE_PATH = os.path.abspath('./.sde/testfiles/nonexistent.json')

MALFORMED_FILE_PATH = os.path.abspath('./.sde/testfiles/malformed.json')

def get_password():

    """
    Utility function for returning a password for file encryption tests.

    Returns:
        The test password.
    """

    return 'testpassword'

class JsonFileTest(unittest.TestCase):

    """
    Contains all unit tests of the JsonFile class.
    """

    @classmethod
    def setUpClass(cls):

        print('')
        print('*******************************************************************************')
        print('     >>>>> JsonFile <<<<<')
        print('*******************************************************************************')

    def test_creation(self):

        """
        Tests that a JsonFile object can be created.
        """

        # STEP 1 - Create file
        sut = JsonFile(path=TEST_FILE_PATH)
        self.assertNotEqual(sut.Path, None)
        self.assertEqual(sut.Content, {})

    def test_saving_and_loading_json_file(self):

        """
        Tests that JSON content can be saved to and loaded from a file on disk.
        """

        # STEP #1 - Compacted JSON file
        sut1 = JsonFile(path=TEST_FILE_PATH)
        sut1.Content['test'] = 'test content'
        sut1.save()
        del sut1

        sut2 = JsonFile(path=TEST_FILE_PATH)
        sut2.load()
        self.assertEqual(sut2.Content['test'], 'test content')

        # STEP #2 - Formatted JSON file
        sut1 = JsonFile(path=TEST_FILE_PATH)
        sut1.Content['test'] = 'test content'
        sut1.save(compact=False)
        del sut1

        sut2 = JsonFile(path=TEST_FILE_PATH)
        sut2.load()
        self.assertEqual(sut2.Content['test'], 'test content')

    def test_saving_and_loading_encrypted_json_file(self):

        """
        Tests that JSON content can be saved to and loaded from an encrypted
        file on disk.
        """

        sut1 = JsonFile(path=TEST_FILE_PATH, cb_retrieve_key=get_password)
        sut1.Content['test'] = 'test content'
        sut1.save()

        sut2 = JsonFile(path=TEST_FILE_PATH, cb_retrieve_key=get_password)
        sut2.load()
        self.assertEqual(sut2.Content['test'], 'test content')

    def test_loading_non_existent_file(self):

        """
        Tests loading a non-existent JSON file is handled properly.
        """

        sut = JsonFile(path=INVALID_TEST_FILE_PATH)
        sut.load()
        self.assertEqual(sut.Content, {})

    def test_savig_file_to_invalid_location(self):

        """
        Tests that the file is not saved to an invalid location.
        """

        # STEP #1 - Unencrypted JSON file
        sut = JsonFile(path='/invalid/path/to/somewhere/file.json')
        with self.assertRaises(RuntimeError):
            sut.save()

        # STEP #2 - Encrypted JSON file
        sut = JsonFile(path='/invalid/path/to/somewhere/file.json',
                       cb_retrieve_key=get_password)
        with self.assertRaises(RuntimeError):
            sut.save()

    def test_loading_malformed_json_file(self):

        # Create a malformed file
        malformed_json = '{invalid json: [}'
        with open(MALFORMED_FILE_PATH, 'w+') as malformed:
            malformed.write(malformed_json)

        # STEP 1 - Trying to load a malformed JSON file results in
        # an exception
        sut = JsonFile(path=MALFORMED_FILE_PATH)
        with self.assertRaises(InvalidInputError):
            sut.load()

        # Create a malformed file and encrypt it
        from suisei.seed.common.util import AESCipher
        cipher = AESCipher(get_password())
        content = cipher.encrypt(malformed_json)
        with open(MALFORMED_FILE_PATH, 'wb') as malformed:
            malformed.write(content)

        # STEP #2 - Trying to load an encrypted and malformed JSON file results
        # in an exception

        sut = JsonFile(path=MALFORMED_FILE_PATH, cb_retrieve_key=get_password)
        with self.assertRaises(InvalidInputError):
            sut.load()

    def test_overwrite_json_file_content(self):

        sut1 = JsonFile(path=TEST_FILE_PATH)
        sut1.Content['test'] = 'test content'
        sut1.overwrite_content({'test': 'overwritten'})
        self.assertEqual(sut1.Content['test'], 'overwritten')

def load_tests(loader, tests, pattern):

    """
    Registers the test suite with the test runner.
    """

    suite = unittest.TestSuite()

    suite.addTest(JsonFileTest('test_creation'))
    suite.addTest(JsonFileTest('test_saving_and_loading_json_file'))
    suite.addTest(JsonFileTest('test_saving_and_loading_encrypted_json_file'))
    suite.addTest(JsonFileTest('test_loading_non_existent_file'))
    suite.addTest(JsonFileTest('test_savig_file_to_invalid_location'))
    suite.addTest(JsonFileTest('test_loading_malformed_json_file'))
    suite.addTest(JsonFileTest('test_overwrite_json_file_content'))

    return suite
