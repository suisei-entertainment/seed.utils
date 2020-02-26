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
Contains the implementation of the basic exception class.
"""

# Platform Imports
import logging
import inspect

# Framework Imports
from .errorcodes import ErrorCodes

class FrameworkError(Exception):

    """
    The base class for all Murasame framework errors.

    Authors:
        Attila Kovacs
    """

    def __init__(self,
                 message: str = '',
                 errorcode: int = ErrorCodes.NOT_SET,
                 package: str = __package__,
                 file: str = '',
                 line: str = '',
                 function: str = '',
                 wrapped_exception: Exception = None,
                 inspect_caller: bool = True) -> None:

        """
        Creates a new Exception instance.

        Args:
            message:            The user message that clarifies the exception.
            errorcode:          The platform errorcode that identifies the
                                actual error.
            package:            Name of the Python package that raised the
                                exception.
            file:               Name of the source file where the exception was
                                raised.
            line:               The line number in the source code where the
                                exception was raised.
            function:           Name of the funtion that raised the exception.
            wrapped_exception:  Another, non-SEED exception that is wrapped
                                inside the SEED exception.
            inspect_caller:     Whether or not the caller should be inspected
                                to retrieve the raising location of the
                                exception. Should only be True in the topmost
                                exception in the inheritance tree, otherwise
                                should be passed down as False.

        Authors:
            Attila Kovacs
        """

        super().__init__(message)

        self.errorcode = errorcode
        """
        The platform error code that identifies the exact issue.
        """

        self.errormessage = message
        """
        Custom error message specified by the user when raising the exception.
        """

        self.package = package
        """
        Name of the package that raised the expcetion.
        """

        self.file = file
        """
        Name of the source file where the exception was raised.
        """

        self.line = line
        """
        The source line where the exception has been raised.
        """

        self.function = function
        """
        The function that raised the exception.
        """

        self.wrapped_exception = wrapped_exception
        """
        An exception that was asked to be wrapped within a SEED exception.
        """

        # When inspect_caller is set to True, then the caller function will be
        # inspected to retrieve the correct location of where the exception
        # was raised.
        if inspect_caller:
            self.file, self.function, self.line = self.inspect_exception()

        # Log the exception
        logger = logging.getLogger('suisei.seed.exceptions')
        logger.error('Framework exception was raised. Type: %s '
                     'Error Code: %s '
                     'Package: %s Location: %s (line %s) Function: %s() '
                     'Message: %s',
                     self.__class__.__name__,
                     self.errorcode,
                     self.package,
                     self.file,
                     self.line,
                     self.function,
                     self.errormessage)

    @staticmethod
    def inspect_exception() -> tuple:

        """
        Inspects the caller frame of the expcetion to determine the location
        in the code where it has been called.

        This function should be called in the constructor of the top level
        of the derived exception to generate the proper location info.

        Returns:
            The function returns three values, the first is the filename where
            the exception constructor was called, the second is the function
            that called the exception constructor, and the third is the line
            number of the source file where the exception was created.
        """

        caller_frame_record = inspect.stack()[2]
        frame = caller_frame_record[0]
        info = inspect.getframeinfo(frame)

        filename = info.filename
        function = info.function
        line = info.lineno

        return filename, function, line
