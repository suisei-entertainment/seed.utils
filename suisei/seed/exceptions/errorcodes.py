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
Contains the list of error codes supported by the framework.
"""

# Platform Imports
from enum import IntEnum

class ErrorCodes(IntEnum):

    """
    Contains the list of error codes supported by the framework.

    Authors:
        Attila Kovacs
    """

    NOT_SET = 0             # Default value when an exact error code is not set

    INPUT_ERROR = 1         # Indicates an error in the input values
    PERMISSION_ERROR = 2    # Indicates a permission violation error
    RUNTIME_ERROR = 3       # Indicates a runtime error
    ALREADY_REGISTERED = 4  # Indicates that something has already beed
                            # registered
    ALREADY_EXISTS = 5      # Indicates that something already exists
    NOT_REGISTERED = 6      # Indicates that something is not registered
    UNCAUGHT_EXCEPTION = 7  # Indicates that an exception is not handled
                            # properly.
    MISSING_REQUIREMENT = 8 # Indicates that a required component is missing
    INSTALL_FAILED = 9      # Indicates that installation of a required
                            # component has failed.
