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
Contains the implementation of the LogTarget class.
"""

class LogTarget:

    """
    Common base class for log target implementations.
    """

    @property
    def Logger(self) -> 'Logger':

        """
        Provides access to the underlying logger object.
        """

        return self._logger

    def __init__(self, logger: 'Logger') -> None:

        """
        Creates a new ConsoleLogTarget entry.

        Args:
            logger:             The logger object that will be used for
                                logging.

        Authors:
            Attila Kovacs
        """

        # The logger object that will be used to write the logs to the console.
        self._logger = logger

    def write(self, entry: 'LogEntry') -> None:

        """
        Writes a log message to the target.

        This function does not do anything by default. It is here to provide a
        way for custom log target implementations to write their own log
        messages outside the Python logging infrastructure.

        Args:
            entry:      The log entry to write.

        Authors:
            Attila Kovacs
        """

        return