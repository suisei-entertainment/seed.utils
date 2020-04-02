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
Contains implementation of the LogChannel class.
"""

# SEED Imports
from .loglevels import LogLevels, LOG_LEVEL_CONVERSION_MAP

class LogChannel:

    """
    Represents a single log channel.

    Authors:
        Attila Kovacs
    """

    @property
    def Name(self) -> str:

        """
        The name of the channel.

        Authors:
            Attila Kovacs
        """

        return self._name

    @property
    def DefaultLogLevel(self) -> LogLevels:

        """
        The default log level of the channel.

        Authors:
            Attila Kovacs
        """

        return self._default_log_level

    def __init__(self, configuration: dict) -> None:

        """
        Creates a new log channel instance.

        Args:
            configuration:      The configuration of the channel.

        Authors:
            Attila Kovacs
        """

        # The name of the channel.
        self._name = None

        # The default log level for the channel.
        self._default_log_level = None

        # List of log targets this channel is writing to.
        self._targets = []

    def write(self, entry: LogEntry) -> None:

        """
        Writes a new log entry to the channel.

        Args:
            entry:          The log entry to write.

        Authors:
            Attila Kovacs
        """

        # Send the message to all targets
        for target in self._targets:
            target.write(entry=entry)

    def _load_configuration(self, configuration: dict) -> None:

        """
        Loads the configuration of the channel from its serialized version.

        Args:
            configuration:      The configuration of the channel.

        Raises:
            InvalidInputError:  Raised when there is no channel name found in
                                the configuration.

        Authors:
            Attila Kovacs
        """

        # Load channel name
        try:
            self._name = configuration['name']
        except KeyError:
            raise InvalidInputError(
                'No channel name found while trying to load the '
                'configuration of a log channel.')

        # Load default log level
        try:
            self._default_log_level = \
                LOG_LEVEL_CONVERSION_MAP[configuration['defaultloglevel']]
        except KeyError:
            # Use the default value if there is none specified in the
            # configuraiton.
            self._default_log_level = LogLevels.INFO

        # Load targets
        try:
            channels = configuration['targets']
        except KeyError:
            raise InvalidInputError(
                'No log targets were found for channel {}'.format(self._name))

        for target in targets:

            # Determine target type
            target_type = None
            try:
                target_type = target['type']
            except KeyError:
                # Jump to the next target if there is no type specified for
                # the current one.
                continue

            log_target = None

            # Load the target based on type
            try:
                if target_type == 'console':
                    log_target = ConsoleLogTarget(configuration=target)
                elif target_type == 'file':
                    log_target = FileLogTarget(configuration=target)
                elif target_type == 'syslog':
                    log_target = SyslogTarget(configuration=target)
                elif target_type == 'database':
                    log_target = DatabaseLogTarget(configuration=target)
                elif target_type == 'structured':
                    log_target = StructuredLogTarget(configuration=target)
            except InvalidInputError:
                # Don't fail if the configuration of a target is wrong.
                continue

            if log_target is not None:
                self._targets.append(log_target)
