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
Contains the implementation of the LogEntry class.
"""

class LogEntry:

    """
    Representation of a single log entry.

    Authors:
        Attila Kovacs
    """

    @property
    def LogLevel(self) -> 'LogLevels':

        """
        The log level of the entry.

        Authors:
            Attila Kovacs
        """

        return self._level

    @property
    def Timestamp(self) -> 'datetime':

        """
        The time when the entry has been created.

        Authors:
            Attila Kovacs
        """

        return self._timestamp

    @property
    def Message(self) -> str:

        """
        The actual log message.

        Authors:
            Attila Kovacs
        """

        return self._message

    @property
    def Classname(self) -> str:

        """
        Name of the class that created the log entry.

        Authors:
            Attila Kovacs
        """

        return self._classname

    def __init__(self,
                 level: 'LogLevels',
                 timestamp: 'datetime',
                 message: str,
                 classname: str) -> None:

        """
        Creates a new LogEntry instance.

        Args:
            level:      The log level of the entry.
            timestamp:  The time when the entry has been created.
            message:    The actual log message.
            classname:  Name of the class that created the log entry.

        Authors:
            Attila Kovacs
        """

        # The log level of the entry
        self._level = level

        # The time when the entry has been created
        self._timestamp = timestamp

        # The actual log message
        self._message = message

        # Name of the class that sent the message
        self._classname = classname
