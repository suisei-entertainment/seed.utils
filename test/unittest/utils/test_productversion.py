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
Contains the unit tests of the ProductVersion class.
"""

# Platform Imports
import unittest

# Framework Imports
from suisei.seed.utils import ProductVersion
from suisei.seed.exceptions import InvalidInputError

# Test data
SIMPLE_TEST_VERSION = \
{
    'major': '1',
    'minor': '2',
    'patch': '3',
    'release': 'beta',
    'meta':
    {
        'codename': 'test',
        'scm': 'abcdef'
    }
}

BIGGER_TEST_VERSION = \
{
    'major': '2',
    'minor': '2',
    'patch': '3',
    'release': 'beta',
    'meta':
    {
        'codename': 'test',
        'scm': 'abcdef'
    }
}

SMALLER_TEST_VERSION = \
{
    'major': '0',
    'minor': '2',
    'patch': '3',
    'release': 'beta',
    'meta':
    {
        'codename': 'test',
        'scm': 'abcdef'
    }
}

INTERNAL_VERSION = \
{
    'major': '1',
    'minor': '2',
    'patch': '3',
    'release': 'internal',
    'meta':
    {
        'codename': 'test',
        'scm': 'abcdef'
    }
}

ALPHA_VERSION = \
{
    'major': '1',
    'minor': '2',
    'patch': '3',
    'release': 'alpha',
    'meta':
    {
        'codename': 'test',
        'scm': 'abcdef'
    }
}

EAP_VERSION = \
{
    'major': '1',
    'minor': '2',
    'patch': '3',
    'release': 'eap',
    'meta':
    {
        'codename': 'test',
        'scm': 'abcdef'
    }
}

RC_VERSION = \
{
    'major': '1',
    'minor': '2',
    'patch': '3',
    'release': 'rc',
    'meta':
    {
        'codename': 'test',
        'scm': 'abcdef'
    }
}

GA_VERSION = \
{
    'major': '1',
    'minor': '2',
    'patch': '3',
    'release': 'ga',
    'meta':
    {
        'codename': 'test',
        'scm': 'abcdef'
    }
}

INVALID_MAJOR_VERSION = \
{
    'major': 'invalid',
    'minor': '2',
    'patch': '3',
    'release': 'beta',
    'meta':
    {
        'codename': 'test',
        'scm': 'abcdef'
    }
}

NEGATIVE_MAJOR_VERSION = \
{
    'major': '-1',
    'minor': '2',
    'patch': '3',
    'release': 'beta',
    'meta':
    {
        'codename': 'test',
        'scm': 'abcdef'
    }
}

NO_MAJOR_VERSION = \
{
    'minor': '2',
    'patch': '3',
    'release': 'beta',
    'meta':
    {
        'codename': 'test',
        'scm': 'abcdef'
    }
}

INVALID_MINOR_VERSION = \
{
    'major': '1',
    'minor': 'invalid',
    'patch': '3',
    'release': 'beta',
    'meta':
    {
        'codename': 'test',
        'scm': 'abcdef'
    }
}

NEGATIVE_MINOR_VERSION = \
{
    'major': '1',
    'minor': '-2',
    'patch': '3',
    'release': 'beta',
    'meta':
    {
        'codename': 'test',
        'scm': 'abcdef'
    }
}

NO_MINOR_VERSION = \
{
    'major': '1',
    'patch': '3',
    'release': 'beta',
    'meta':
    {
        'codename': 'test',
        'scm': 'abcdef'
    }
}

INVALID_PATCH_LEVEL = \
{
    'major': '1',
    'minor': '2',
    'patch': 'invalid',
    'release': 'beta',
    'meta':
    {
        'codename': 'test',
        'scm': 'abcdef'
    }
}

NEGATIVE_PATCH_LEVEL = \
{
    'major': '1',
    'minor': '2',
    'patch': '-3',
    'release': 'beta',
    'meta':
    {
        'codename': 'test',
        'scm': 'abcdef'
    }
}

NO_PATCH_LEVEL = \
{
    'major': '1',
    'minor': '2',
    'release': 'beta',
    'meta':
    {
        'codename': 'test',
        'scm': 'abcdef'
    }
}

NO_RELEASE_LEVEL = \
{
    'major': '1',
    'minor': '2',
    'patch': '3',
    'meta':
    {
        'codename': 'test',
        'scm': 'abcdef'
    }
}

INVALID_RELEASE_LEVEL = \
{
    'major': '1',
    'minor': '2',
    'patch': '3',
    'release': 'invalid',
    'meta':
    {
        'codename': 'test',
        'scm': 'abcdef'
    }
}


ADDITIONAL_METADATA = \
{
    'major': '1',
    'minor': '2',
    'patch': '3',
    'release': 'beta',
    'meta':
    {
        'codename': 'test',
        'scm': 'abcdef',
        'additional': 'data'
    }
}

METADATA_NO_CODENAME = \
{
    'major': '1',
    'minor': '2',
    'patch': '3',
    'release': 'beta',
    'meta':
    {
        'scm': 'abcdef'
    }
}

METADATA_NO_SCM = \
{
    'major': '1',
    'minor': '2',
    'patch': '3',
    'release': 'beta',
    'meta':
    {
        'codename': 'test'
    }
}

NO_METADATA = \
{
    'major': '1',
    'minor': '2',
    'patch': '3',
    'release': 'beta'
}

VERSION_WITH_BUILD_NUMBER = \
{
    'major': '1',
    'minor': '2',
    'patch': '3',
    'release': 'beta',
    'meta':
    {
        'build': '1'
    }
}

class ProductVersionTest(unittest.TestCase):

    """
    Contains the unit tests for the ProductVersion class.
    """

    @classmethod
    def setUpClass(cls):

        print('')
        print('*******************************************************************************')
        print('     >>>>> ProductVersion <<<<<')
        print('*******************************************************************************')

    def test_product_version_creation(self):

        """
        Tests that a product version instance can be created successfully.
        """

        # STEP #1 - Product version can be created with normal config data
        sut = ProductVersion(SIMPLE_TEST_VERSION)

        self.assertEqual(sut.MajorVersion, 1)
        self.assertEqual(sut.MinorVersion, 2)
        self.assertEqual(sut.PatchLevel, 3)
        self.assertEqual(sut.ReleaseLevel, ProductVersion.ReleaseLevels.BETA)
        self.assertEqual(sut.Codename, 'test')
        self.assertEqual(sut.SCM, 'abcdef')
        self.assertEqual(sut.Build, '0')

        # STEP #2 - Product version can't be created with invalid major version
        with self.assertRaises(InvalidInputError):
            sut = ProductVersion(INVALID_MAJOR_VERSION)

        # STEP #3 - Product version can't be created with invalid minor version
        with self.assertRaises(InvalidInputError):
            sut = ProductVersion(INVALID_MINOR_VERSION)

        # STEP #4 - Product version can't be created with invalid patch level
        with self.assertRaises(InvalidInputError):
            sut = ProductVersion(INVALID_PATCH_LEVEL)

        # STEP #5 - Product version can be created without metadata
        sut = ProductVersion(NO_METADATA)
        self.assertEqual(sut.MajorVersion, 1)
        self.assertEqual(sut.MinorVersion, 2)
        self.assertEqual(sut.PatchLevel, 3)
        self.assertEqual(sut.ReleaseLevel, ProductVersion.ReleaseLevels.BETA)
        self.assertEqual(sut.Codename, 'UNKNOWN')
        self.assertEqual(sut.SCM, 'UNKNOWN')

        # STEP #6 - Product version can be created with partial metadata
        sut = ProductVersion(METADATA_NO_CODENAME)
        self.assertEqual(sut.MajorVersion, 1)
        self.assertEqual(sut.MinorVersion, 2)
        self.assertEqual(sut.PatchLevel, 3)
        self.assertEqual(sut.ReleaseLevel, ProductVersion.ReleaseLevels.BETA)
        self.assertEqual(sut.Codename, 'UNKNOWN')
        self.assertEqual(sut.SCM, 'abcdef')

        sut = ProductVersion(METADATA_NO_SCM)
        self.assertEqual(sut.MajorVersion, 1)
        self.assertEqual(sut.MinorVersion, 2)
        self.assertEqual(sut.PatchLevel, 3)
        self.assertEqual(sut.ReleaseLevel, ProductVersion.ReleaseLevels.BETA)
        self.assertEqual(sut.Codename, 'test')
        self.assertEqual(sut.SCM, 'UNKNOWN')

        # STEP #7 - Product version can't be created without major version
        with self.assertRaises(InvalidInputError):
            sut = ProductVersion(NO_MAJOR_VERSION)

        # STEP #8 - Product version can't be created without minor version
        with self.assertRaises(InvalidInputError):
            sut = ProductVersion(NO_MINOR_VERSION)

        # STEP #9 - Product version can't be created without patch leve
        with self.assertRaises(InvalidInputError):
            sut = ProductVersion(NO_PATCH_LEVEL)

        # STEP #10 - Product version can be created without a release level
        sut = ProductVersion(NO_RELEASE_LEVEL)
        self.assertEqual(sut.ReleaseLevel, ProductVersion.ReleaseLevels.GA)

        # STEP #11 - Product version can be created with various release levels
        sut = ProductVersion(INTERNAL_VERSION)
        self.assertEqual(sut.MajorVersion, 1)
        self.assertEqual(sut.MinorVersion, 2)
        self.assertEqual(sut.PatchLevel, 3)
        self.assertEqual(sut.ReleaseLevel,
                         ProductVersion.ReleaseLevels.INTERNAL)
        self.assertEqual(sut.Codename, 'test')
        self.assertEqual(sut.SCM, 'abcdef')

        sut = ProductVersion(ALPHA_VERSION)
        self.assertEqual(sut.MajorVersion, 1)
        self.assertEqual(sut.MinorVersion, 2)
        self.assertEqual(sut.PatchLevel, 3)
        self.assertEqual(sut.ReleaseLevel,
                         ProductVersion.ReleaseLevels.ALPHA)
        self.assertEqual(sut.Codename, 'test')
        self.assertEqual(sut.SCM, 'abcdef')

        sut = ProductVersion(EAP_VERSION)
        self.assertEqual(sut.MajorVersion, 1)
        self.assertEqual(sut.MinorVersion, 2)
        self.assertEqual(sut.PatchLevel, 3)
        self.assertEqual(sut.ReleaseLevel,
                         ProductVersion.ReleaseLevels.EAP)
        self.assertEqual(sut.Codename, 'test')
        self.assertEqual(sut.SCM, 'abcdef')

        sut = ProductVersion(RC_VERSION)
        self.assertEqual(sut.MajorVersion, 1)
        self.assertEqual(sut.MinorVersion, 2)
        self.assertEqual(sut.PatchLevel, 3)
        self.assertEqual(sut.ReleaseLevel,
                         ProductVersion.ReleaseLevels.RC)
        self.assertEqual(sut.Codename, 'test')
        self.assertEqual(sut.SCM, 'abcdef')

        sut = ProductVersion(GA_VERSION)
        self.assertEqual(sut.MajorVersion, 1)
        self.assertEqual(sut.MinorVersion, 2)
        self.assertEqual(sut.PatchLevel, 3)
        self.assertEqual(sut.ReleaseLevel,
                         ProductVersion.ReleaseLevels.GA)
        self.assertEqual(sut.Codename, 'test')
        self.assertEqual(sut.SCM, 'abcdef')

        # STEP #12 - Product version can't be created with invalid release
        #            level
        with self.assertRaises(InvalidInputError):
            sut = ProductVersion(INVALID_RELEASE_LEVEL)

        # STEP #13 - Product version can't be created with negative version
        #            numbers
        with self.assertRaises(InvalidInputError):
            sut = ProductVersion(NEGATIVE_MAJOR_VERSION)

        with self.assertRaises(InvalidInputError):
            sut = ProductVersion(NEGATIVE_MINOR_VERSION)

        with self.assertRaises(InvalidInputError):
            sut = ProductVersion(NEGATIVE_PATCH_LEVEL)

    def test_metadata_retrieval(self):

        """
        Tests that metadata can be retrieved from the product version
        """

        # STEP #1 - Metadata can be retrieved in a raw format
        sut = ProductVersion(SIMPLE_TEST_VERSION)
        self.assertEqual(sut.MetaData, {'codename': 'test', 'scm': 'abcdef'})

        # STEP #2 - Additional metadata fields can be accessed through the
        #           raw format
        sut = ProductVersion(ADDITIONAL_METADATA)
        self.assertEqual(
            sut.MetaData,
            {'codename': 'test', 'scm': 'abcdef', 'additional': 'data'})
        self.assertEqual(sut.Build, '0')
        self.assertEqual(sut.MetaData['additional'], 'data')

        # STEP #3 - Build number can be retrieved
        sut = ProductVersion(VERSION_WITH_BUILD_NUMBER)
        self.assertEqual(sut.Build, '1')

        sut = ProductVersion(NO_METADATA)
        self.assertEqual(sut.Build, '0')

    def test_version_string_conversion(self):

        """
        Tests string representations of the product version
        """

        # STEP #1 - Tests that the full product version is correct
        sut = ProductVersion(SIMPLE_TEST_VERSION)
        self.assertEqual(sut.VersionString, '1.2.3-BETA+test(abcdef)')

        sut = ProductVersion(NO_METADATA)
        self.assertEqual(sut.VersionString, '1.2.3-BETA')

        # STEP #2 - Tests that the short product version is correct
        sut = ProductVersion(SIMPLE_TEST_VERSION)
        self.assertEqual(sut.ShortVersionString, '1.2.3')

        # STEP #3 - Tests that the metadata conversion string is correct
        sut = ProductVersion(SIMPLE_TEST_VERSION)
        self.assertEqual(sut.MetaString, 'test(abcdef)')

        sut = ProductVersion(NO_METADATA)
        self.assertEqual(sut.MetaString, 'UNKNOWN(UNKNOWN)')

        sut = ProductVersion(METADATA_NO_CODENAME)
        self.assertEqual(sut.MetaString, 'UNKNOWN(abcdef)')

        sut = ProductVersion(METADATA_NO_SCM)
        self.assertEqual(sut.MetaString, 'test(UNKNOWN)')

        # STEP #4 - Tests that string conversion for various release levels is
        #           correct.
        sut = ProductVersion(INTERNAL_VERSION)
        self.assertEqual(sut.VersionString, '1.2.3-DEVELOPMENT+test(abcdef)')

        sut = ProductVersion(ALPHA_VERSION)
        self.assertEqual(sut.VersionString, '1.2.3-ALPHA+test(abcdef)')

        sut = ProductVersion(EAP_VERSION)
        self.assertEqual(sut.VersionString, '1.2.3-EAP+test(abcdef)')

        sut = ProductVersion(RC_VERSION)
        self.assertEqual(sut.VersionString, '1.2.3-RC+test(abcdef)')

        sut = ProductVersion(GA_VERSION)
        self.assertEqual(sut.VersionString, '1.2.3-GA+test(abcdef)')

    def test_product_version_operators(self):

        """
        Tests that product versions can be compared by using operators
        """

        sut = ProductVersion(SIMPLE_TEST_VERSION)
        sut_equal = ProductVersion(SIMPLE_TEST_VERSION)
        sut_smaller = ProductVersion(SMALLER_TEST_VERSION)
        sut_bigger = ProductVersion(BIGGER_TEST_VERSION)

        self.assertEqual(sut == sut_equal, True)
        self.assertEqual(sut == sut_smaller, False)
        self.assertEqual(sut != sut_equal, False)
        self.assertEqual(sut != sut_smaller, True)
        self.assertEqual(sut < sut_smaller, False)
        self.assertEqual(sut < sut_bigger, True)
        self.assertEqual(sut > sut_smaller, True)
        self.assertEqual(sut > sut_bigger, False)
        self.assertEqual(sut <= sut_smaller, False)
        self.assertEqual(sut <= sut_bigger, True)
        self.assertEqual(sut <= sut_equal, True)
        self.assertEqual(sut >= sut_smaller, True)
        self.assertEqual(sut >= sut_bigger, False)
        self.assertEqual(sut >= sut_equal, True)

        self.assertEqual(sut == 1, False)
        self.assertEqual(sut != 1, True)

        with self.assertRaises(TypeError):
            sut < 1

        with self.assertRaises(TypeError):
            sut > 1

        with self.assertRaises(TypeError):
            sut <= 1

        with self.assertRaises(TypeError):
            sut >= 1

        self.assertEqual(sut.__repr__(), 'ProductVersion(1.2.3-BETA+test(abcdef))')
        self.assertEqual(sut.__str__(), '1.2.3-BETA+test(abcdef)')
        self.assertEqual(sut.__hash__(), hash(sut.VersionString))

    def test_version_number_bumping(self):

        """
        Tests that version numbers can be bumped.
        """

        # STEP #1 - Bump major version
        sut = ProductVersion(SIMPLE_TEST_VERSION)
        sut.bump_major_version()
        self.assertEqual(sut.VersionString, '2.0.0-BETA+test(abcdef)')

        # STEP #2 - Bump minor version
        sut = ProductVersion(SIMPLE_TEST_VERSION)
        sut.bump_minor_version()
        self.assertEqual(sut.VersionString, '1.3.0-BETA+test(abcdef)')

        # STEP #3 - Bump patch level
        sut = ProductVersion(SIMPLE_TEST_VERSION)
        sut.bump_patch_level()
        self.assertEqual(sut.VersionString, '1.2.4-BETA+test(abcdef)')

        # STEP #4 - Bump build number
        sut = ProductVersion(VERSION_WITH_BUILD_NUMBER)
        sut.bump_build_number()
        self.assertEqual(sut.VersionString, '1.2.3-BETA+UNKNOWN(Build 2)')

        sut = ProductVersion(SIMPLE_TEST_VERSION)
        sut.bump_build_number()
        self.assertEqual(sut.VersionString, '1.2.3-BETA+test(abcdef)')

def load_tests(loader, tests, pattern):

    """
    Registers the test suite with the test runner.
    """

    suite = unittest.TestSuite()

    suite.addTest(
        ProductVersionTest('test_product_version_creation'))
    suite.addTest(
        ProductVersionTest('test_metadata_retrieval'))
    suite.addTest(
        ProductVersionTest('test_version_string_conversion'))
    suite.addTest(
        ProductVersionTest('test_product_version_operators'))
    suite.addTest(
        ProductVersionTest('test_version_number_bumping'))

    return suite
