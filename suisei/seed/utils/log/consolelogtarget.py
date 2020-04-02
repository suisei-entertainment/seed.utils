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
Contains the implementation of the ConsoleLogTarget class.
"""

class ConsoleLogTarget(LogTarget):

    """
    Represents a log target that writes messages to the system console.

    Authors:
        Attila Kovacs
    """

    def __init__(self, configuration: dict) -> None:

        """
        Creates a new ConsoleLogTarget entry.

        Args:
            configuration:      The configuration of the target in serialized
                                format.

        Authors:
            Attila Kovacs
        """

        return

    def write(self, entry: LogEntry) -> None:

        """
        Writes a log entry to the target.

        Args:
            entry:      The log entry to write.

        Authors:
            Attila Kovacs
        """

        return
