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
Contains the implementation of the AlreadyExistsError exception.
"""

# Framework Imports
from .errorcodes import ErrorCodes
from .exception import FrameworkError

class AlreadyExistsError(FrameworkError):

    """
    Exception raised when trying to add something twice to e.g. a list or
    dictionary.

    Authors:
        Attila Kovacs
    """

    def __init__(self,
                 message: str = '',
                 errorcode: int = ErrorCodes.ALREADY_EXISTS,
                 package: str = __package__,
                 file: str = '',
                 line: str = '',
                 function: str = '',
                 wrapped_exception: Exception = None,
                 inspect_caller: bool = True) -> None:

        """
        Creates a new AlreadyExistsError instance.

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

        # Inspect the caller if requested
        if inspect_caller:
            file, function, line = self.inspect_exception()

        super().__init__(message=message,
                         errorcode=errorcode,
                         package=package,
                         file=file,
                         line=line,
                         function=function,
                         wrapped_exception=wrapped_exception,
                         inspect_caller=False)
