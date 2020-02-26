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
Contains the unit tests of the basic file encryption and decryption functions.
"""

# Platform Imports
import unittest

# Framework Imports
from suisei.seed.utils import AESCipher

TEST_CONTENT = 'test string for encryption'

class FileEncryptionTest(unittest.TestCase):

    """
    Contains the unit tests for the content encryption functions.
    """

    @classmethod
    def setUpClass(cls):

        print('')
        print('*******************************************************************************')
        print('     >>>>> AESCipher <<<<<')
        print('*******************************************************************************')

    def test_content_encrpytion(self):

        """
        Tests that content can be encrpyted and decrypted successfully.
        """

        test_string = 'this is a test'
        key = 'secret test password'

        # STEP #1 - Encrypt and decrypt using the same AESCipher object.
        sut = AESCipher(key)
        encrypted = sut.encrypt(test_string)
        decrypted = sut.decrypt(encrypted)
        self.assertEqual(decrypted, test_string)

        # STEP #2 - Encrypt and decrypt using different AESCipher objects
        sut1 = AESCipher(key)
        encrypted = sut1.encrypt(test_string)

        sut2 = AESCipher(key)
        decrypted = sut2.decrypt(encrypted)
        self.assertEqual(decrypted, test_string)

def load_tests(loader, tests, pattern):

    """
    Registers the test suite with the test runner.
    """

    suite = unittest.TestSuite()

    suite.addTest(FileEncryptionTest('test_content_encrpytion'))

    return suite
