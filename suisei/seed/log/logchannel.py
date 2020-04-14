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

# Platform Imports
import logging

# SEED Imports
from suisei.seed.exceptions import InvalidInputError

from .loglevels import LogLevels, LOG_LEVEL_CONVERSION_MAP
from .logentry import LogEntry
from .consolelogtarget import ConsoleLogTarget

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

        self._load_configuration(configuration)

        # Get a reference to the wrapped Python logger object.
        self._logger = logging.getLogger(self._name)

        # Set the log level to DEBUG, so all log messages would be written to
        # the logger by default. Actual log level will be controlled by the
        # writers.
        self._logger.setLevel(logging.DEBUG)

        self._load_targets(configuration)

    def write(self, entry: LogEntry) -> None:

        """
        Writes a new log entry to the channel.

        Args:
            entry:          The log entry to write.

        Authors:
            Attila Kovacs
        """

        # Send the message to the central logger
        if entry.LogLevel == LogLevels.DEBUG:
            self._logger.debug(entry.Message)
        elif entry.LogLevel in (LogLevels.INFO, LogLevels.NOTICE):
            self._logger.info(entry.Message)
        elif entry.LogLevel == LogLevels.NOTICE:
            self._logger.info(entry.Message)
        elif entry.LogLevel == LogLevels.WARNING:
            self._logger.warning(entry.Message)
        elif entry.LogLevel == LogLevels.ERROR:
            self._logger.error(entry.Message)
        elif entry.LogLevel in (LogLevels.CRITICAL, LogLevels.ALERT, LogLevels.EMERGENCY):
            self._logger.fatal(entry.Message)

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

    def _load_targets(self, configuration: dict) -> None:

        """
        Loads the log targets of the channel from its serialized version.

        Args:
            configuration:      The configuration of the channel.

        Authors:
            Attila Kovacs
        """

        # Remove all existing log handlers
        self._logger.handlers = []

        targets = []

        # Load targets
        try:
            targets = configuration['targets']
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
                    log_target = ConsoleLogTarget(logger=self._logger,
                                                  configuration=target)
                elif target_type == 'file':
                    log_target = FileLogTarget(logger=self._logger,
                                               configuration=target)
                elif target_type == 'syslog':
                    log_target = SyslogTarget(logger=self._logger,
                                              configuration=target)
                elif target_type == 'database':
                    log_target = DatabaseLogTarget(logger=self._logger,
                                                   configuration=target)
                elif target_type == 'structured':
                    log_target = StructuredLogTarget(logger=self._logger,
                                                     configuration=target)
            except InvalidInputError:
                # Don't fail if the configuration of a target is wrong.
                continue

            if log_target is not None:
                self._targets.append(log_target)
