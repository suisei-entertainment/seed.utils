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
Contains the implementation of the LogLevels class.
"""

# Platform Imports
from enum import IntEnum

class LogLevels(IntEnum):

    """
    Contains the list of supported log levels. This maps to log levels
    supported by syslog. For Python logging, some log levels are merged
    according to the following table:

    SEED Log Level | Syslog Log Level | Python Log Level
    =====================================================
     DEBUG         |      DEBUG       |     DEBUG
     INFO          |      INFO        |     INFO
     NOTICE        |      NOTICE      |     INFO
     WARNING       |      WARNING     |     WARNING
     ERROR         |      ERROR       |     ERROR
     CRITICAL      |      CRITICAL    |     FATAL
     ALERT         |      ALERT       |     FATAL
     EMERGENCY     |      EMERGENCY   |     FATAL

    Authors:
        Attila Kovacs
    """

    DEBUG = 0
    INFO = 1
    NOTICE = 2
    WARNING = 3
    ERROR = 4
    CRITICAL = 5
    ALERT = 6
    EMERGENCY = 7

# Conversion map to use when reading the log level from a string.
LOG_LEVEL_CONVERSION_MAP = \
{
    'DEBUG': LogLevels.DEBUG,
    'INFO': LogLevels.INFO,
    'NOTICE': LogLevels.NOTICE,
    'WARNING': LogLevels.WARNING,
    'ERROR': LogLevels.ERROR,
    'CRITICAL': LogLevels.CRITICAL,
    'ALERT': LogLevels.ALERT,
    'EMERGENCY': LogLevels.EMERGENCY
}
