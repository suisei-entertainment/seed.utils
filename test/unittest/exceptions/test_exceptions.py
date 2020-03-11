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
Contains the unit tests of the exception classes.
"""

# Platform Imports
import unittest

# Framework Imports
import suisei.seed.exceptions

class ExceptionsTest(unittest.TestCase):

    """
    Contains the unit tests for the exception classes.
    """

    @classmethod
    def setUpClass(cls):

        print('')
        print('*******************************************************************************')
        print('     >>>>> Exceptions <<<<<')
        print('*******************************************************************************')

    def test_exception(self):

        """
        Contains tests for the base FrameworkError class.
        """

        # STEP 1 - Test that the exception can be raised.
        try:
            raise suisei.seed.exceptions.FrameworkError('test')
        except suisei.seed.exceptions.FrameworkError as error:
            self.assertEqual(error.errorcode,
                             suisei.seed.exceptions.ErrorCodes.NOT_SET)
            self.assertEqual(error.errormessage, 'test')

        # STEP 2 - Test that the exception can be raised without caller
        # inspection.
        try:
            raise suisei.seed.exceptions.FrameworkError(
                'test',
                inspect_caller=False)
        except suisei.seed.exceptions.FrameworkError as error:
            self.assertEqual(error.errorcode,
                             suisei.seed.exceptions.ErrorCodes.NOT_SET)
            self.assertEqual(error.errormessage, 'test')

    def test_access_violation_error(self):

        """
        Contains tests for the AccessViolationError class.
        """

        # STEP 1 - Test that the exception can be raised.
        try:
            raise suisei.seed.exceptions.AccessViolationError('test')
        except suisei.seed.exceptions.AccessViolationError as error:
            self.assertEqual(
                error.errorcode,
                suisei.seed.exceptions.ErrorCodes.PERMISSION_ERROR)
            self.assertEqual(error.errormessage, 'test')

        # STEP 2 - Test that the exception can be raised without caller
        # inspection.
        try:
            raise suisei.seed.exceptions.AccessViolationError(
                'test',
                inspect_caller=False)
        except suisei.seed.exceptions.AccessViolationError as error:
            self.assertEqual(
                error.errorcode,
                suisei.seed.exceptions.ErrorCodes.PERMISSION_ERROR)
            self.assertEqual(error.errormessage, 'test')

    def test_already_registered_error(self):

        """
        Contains tests for the AlreadyRegisteredError class.
        """

        # STEP 1 - Test that the exception can be raised.
        try:
            raise suisei.seed.exceptions.AlreadyRegisteredError('test')
        except suisei.seed.exceptions.AlreadyRegisteredError as error:
            self.assertEqual(
                error.errorcode,
                suisei.seed.exceptions.ErrorCodes.ALREADY_REGISTERED)
            self.assertEqual(error.errormessage, 'test')

        # STEP 2 - Test that the exception can be raised without caller
        # inspection.
        try:
            raise suisei.seed.exceptions.AlreadyRegisteredError(
                'test',
                inspect_caller=False)
        except suisei.seed.exceptions.AlreadyRegisteredError as error:
            self.assertEqual(
                error.errorcode,
                suisei.seed.exceptions.ErrorCodes.ALREADY_REGISTERED)
            self.assertEqual(error.errormessage, 'test')

    def test_already_exists_error(self):

        """
        Contains tests for the AlreadyExistsError class.
        """

        # STEP 1 - Test that the exception can be raised.
        try:
            raise suisei.seed.exceptions.AlreadyExistsError('test')
        except suisei.seed.exceptions.AlreadyExistsError as error:
            self.assertEqual(
                error.errorcode,
                suisei.seed.exceptions.ErrorCodes.ALREADY_EXISTS)
            self.assertEqual(error.errormessage, 'test')

        # STEP 2 - Test that the exception can be raised without caller
        # inspection.
        try:
            raise suisei.seed.exceptions.AlreadyExistsError(
                'test',
                inspect_caller=False)
        except suisei.seed.exceptions.AlreadyExistsError as error:
            self.assertEqual(
                error.errorcode,
                suisei.seed.exceptions.ErrorCodes.ALREADY_EXISTS)
            self.assertEqual(error.errormessage, 'test')

    def test_input_error(self):

        """
        Contains tests for the InvalidInputError class.
        """

        # STEP 1 - Test that the exception can be raised.
        try:
            raise suisei.seed.exceptions.InvalidInputError('test')
        except suisei.seed.exceptions.InvalidInputError as error:
            self.assertEqual(
                error.errorcode,
                suisei.seed.exceptions.ErrorCodes.INPUT_ERROR)
            self.assertEqual(error.errormessage, 'test')

        # STEP 2 - Test that the exception can be raised without caller
        # inspection.
        try:
            raise suisei.seed.exceptions.InvalidInputError(
                'test',
                inspect_caller=False)
        except suisei.seed.exceptions.InvalidInputError as error:
            self.assertEqual(
                error.errorcode,
                suisei.seed.exceptions.ErrorCodes.INPUT_ERROR)
            self.assertEqual(error.errormessage, 'test')

    def test_not_registered_error(self):

        """
        Contains tests for the NotRegisteredError class.
        """

        # STEP 1 - Test that the exception can be raised.
        try:
            raise suisei.seed.exceptions.NotRegisteredError('test')
        except suisei.seed.exceptions.NotRegisteredError as error:
            self.assertEqual(
                error.errorcode,
                suisei.seed.exceptions.ErrorCodes.NOT_REGISTERED)
            self.assertEqual(error.errormessage, 'test')

        # STEP 2 - Test that the exception can be raised without caller
        # inspection.
        try:
            raise suisei.seed.exceptions.NotRegisteredError(
                'test',
                inspect_caller=False)
        except suisei.seed.exceptions.NotRegisteredError as error:
            self.assertEqual(
                error.errorcode,
                suisei.seed.exceptions.ErrorCodes.NOT_REGISTERED)
            self.assertEqual(error.errormessage, 'test')

    def test_permission_error(self):

        """
        Contains tests for the AccessViolation class.
        """

        # STEP 1 - Test that the exception can be raised.
        try:
            raise suisei.seed.exceptions.AccessViolationError('test')
        except suisei.seed.exceptions.AccessViolationError as error:
            self.assertEqual(
                error.errorcode,
                suisei.seed.exceptions.ErrorCodes.PERMISSION_ERROR)
            self.assertEqual(error.errormessage, 'test')

        # STEP 2 - Test that the exception can be raised without caller
        # inspection.
        try:
            raise suisei.seed.exceptions.AccessViolationError(
                'test',
                inspect_caller=False)
        except suisei.seed.exceptions.AccessViolationError as error:
            self.assertEqual(
                error.errorcode,
                suisei.seed.exceptions.ErrorCodes.PERMISSION_ERROR)
            self.assertEqual(error.errormessage, 'test')

    def test_installation_failed_error(self):

        """
        Contains tests for the InstallationFailedError class.
        """

        # STEP 1 - Test that the exception can be raised.
        try:
            raise suisei.seed.exceptions.InstallationFailedError('test')
        except suisei.seed.exceptions.InstallationFailedError as error:
            self.assertEqual(
                error.errorcode,
                suisei.seed.exceptions.ErrorCodes.INSTALL_FAILED)
            self.assertEqual(error.errormessage, 'test')

        # STEP 2 - Test that the exception can be raised without caller
        # inspection.
        try:
            raise suisei.seed.exceptions.InstallationFailedError(
                'test',
                inspect_caller=False)
        except suisei.seed.exceptions.InstallationFailedError as error:
            self.assertEqual(
                error.errorcode,
                suisei.seed.exceptions.ErrorCodes.INSTALL_FAILED)
            self.assertEqual(error.errormessage, 'test')

    def test_missing_requirement_error(self):

        """
        Contains tests for the MissingRequirementError class.
        """

        # STEP 1 - Test that the exception can be raised.
        try:
            raise suisei.seed.exceptions.MissingRequirementError('test')
        except suisei.seed.exceptions.MissingRequirementError as error:
            self.assertEqual(
                error.errorcode,
                suisei.seed.exceptions.ErrorCodes.MISSING_REQUIREMENT)
            self.assertEqual(error.errormessage, 'test')

        # STEP 2 - Test that the exception can be raised without caller
        # inspection.
        try:
            raise suisei.seed.exceptions.MissingRequirementError(
                'test',
                inspect_caller=False)
        except suisei.seed.exceptions.MissingRequirementError as error:
            self.assertEqual(
                error.errorcode,
                suisei.seed.exceptions.ErrorCodes.MISSING_REQUIREMENT)
            self.assertEqual(error.errormessage, 'test')

    def test_uncaught_exception_error(self):

        """
        Contains tests for the UncaughtExceptionError class.
        """

        # STEP 1 - Test that the exception can be raised.
        try:
            raise suisei.seed.exceptions.UncaughtExceptionError('test')
        except suisei.seed.exceptions.UncaughtExceptionError as error:
            self.assertEqual(
                error.errorcode,
                suisei.seed.exceptions.ErrorCodes.UNCAUGHT_EXCEPTION)
            self.assertEqual(error.errormessage, 'test')

        # STEP 2 - Test that the exception can be raised without caller
        # inspection.
        try:
            raise suisei.seed.exceptions.UncaughtExceptionError(
                'test',
                inspect_caller=False)
        except suisei.seed.exceptions.UncaughtExceptionError as error:
            self.assertEqual(
                error.errorcode,
                suisei.seed.exceptions.ErrorCodes.UNCAUGHT_EXCEPTION)
            self.assertEqual(error.errormessage, 'test')

def load_tests(loader, tests, pattern):

    """
    Registers the test suite with the test runner.
    """

    suite = unittest.TestSuite()

    suite.addTest(ExceptionsTest('test_exception'))
    suite.addTest(ExceptionsTest('test_access_violation_error'))
    suite.addTest(ExceptionsTest('test_already_registered_error'))
    suite.addTest(ExceptionsTest('test_already_exists_error'))
    suite.addTest(ExceptionsTest('test_input_error'))
    suite.addTest(ExceptionsTest('test_not_registered_error'))
    suite.addTest(ExceptionsTest('test_permission_error'))
    suite.addTest(ExceptionsTest('test_installation_failed_error'))
    suite.addTest(ExceptionsTest('test_missing_requirement_error'))
    suite.addTest(ExceptionsTest('test_uncaught_exception_error'))

    return suite
