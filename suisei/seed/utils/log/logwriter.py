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
Contains the implementation of the LogWriter class.
"""

# Platform Imports
from datetime import datetime

# SEED Imports
from suisei.seed.exceptions import InvalidInputError
from suisei.seed.utils import ServiceLocator
from .loglevels import LogLevels

class LogWriter:

    """
    Utility class that represents an object that wants to write into the log.

    Authors:
        Attila Kovacs
    """

    @property
    def LogLevel(self) -> LogLevels:

        """
        The current log level of the writer.

        Authors:
            Attila Kovacs
        """

        return self._log_level

    @property
    def IsLogLevelOverwritten(self) -> bool:

        """
        Whether or not the log level of the channel this writer logs to has
        been overwritten by the writer.

        Authors:
            Attila Kovacs
        """

        return self._log_level_overwritten

    def __init__(self, channel_name: str, cache_entries: bool = False) -> None:

        """
        Creates a new LogWriter instance.

        Args:
            channel_name:       Name of the channel this writer logs to.
            cache_entries:      Whether or not log entries should be cached if
                                the log service is not available.

        Authors:
            Attila Kovacs
        """

        # Whether or not log entries should be cached if the log servie is
        # unavailable.
        self._cache_entries = cache_entries

        # Stores cached log entries until they are sent to the log channel
        # after attach.
        self._cache = []

        # Name of the channel this writer logs to.
        self._channel_name = channel_name

        # The log channel object to log to.
        self._channel = self._attach()

        # Current log level of the writer.
        self._log_level = None

        # Whether or not the log level has been overwritten for this writer.
        self._log_level_overwritten = False

        self._attach()

    def overwrite_log_level(self, new_log_level: LogLevels) -> None:

        """
        Overwrites the log level of the writer.

        Args:
            new_log_level:      The new log level that will be used by the
                                writer.

        Authors:
            Attila Kovacs
        """

        self._log_level = new_log_level
        self._log_level_overwritten = True

    def reset_log_level(self) -> None:

        """
        Resets the log level of the writer to the default value set by its
        parent channel.

        Authors:
            Attila Kovacs
        """

        if self._channel:
            self._log_level = self._channel.DefaultLogLevel
        else:
            self._log_level = LogLevels.INFO

        self._log_level_overwritten = False

    def debug(self, message: str) -> None:

        """
        Writes a new debug level log message to the log channel, if the
        configured log level allows it.

        Args:
            message:        The log message to write.

        Authors:
            Attila Kovacs.
        """

        if self._log_level == LogLevels.DEBUG:
            entry = self._make_entry(level=LogLevels.DEBUG, message=message)
            self._log(entry=entry)

    def info(self, message: str) -> None:

        """
        Writes a new info level log message to the log channel, if the
        configured log level allows it.

        Args:
            message:        The log message to write.

        Authors:
            Attila Kovacs.
        """

        if self._log_level <= LogLevels.INFO:
            entry = self._make_entry(level=LogLevels.INFO, message=message)
            self._log(entry=entry)

    def notice(self, message: str) -> None:

        """
        Writes a new notice level log message to the log channel, if the
        configured log level allows it.

        Args:
            message:        The log message to write.

        Authors:
            Attila Kovacs.
        """

        if self._log_level <= LogLevels.NOTICE:
            entry = self._make_entry(level=LogLevels.NOTICE, message=message)
            self._log(entry=entry)

    def warning(self, message: str) -> None:

        """
        Writes a new warning level log message to the log channel, if the
        configured log level allows it.

        Args:
            message:        The log message to write.

        Authors:
            Attila Kovacs.
        """

        if self._log_level <= LogLevels.WARNING:
            entry = self._make_entry(level=LogLevels.WARNING, message=message)
            self._log(entry=entry)

    def error(self, message: str) -> None:

        """
        Writes a new error level log message to the log channel, if the
        configured log level allows it.

        Args:
            message:        The log message to write.

        Authors:
            Attila Kovacs.
        """

        if self._log_level <= LogLevels.ERROR:
            entry = self._make_entry(level=LogLevels.ERROR, message=message)
            self._log(entry=entry)

    def critical(self, message: str) -> None:

        """
        Writes a new critical level log message to the log channel, if the
        configured log level allows it.

        Args:
            message:        The log message to write.

        Authors:
            Attila Kovacs.
        """

        if self._log_level <= LogLevels.CRITICAL:
            entry = self._make_entry(level=LogLevels.CRITICAL, message=message)
            self._log(entry=entry)

    def alert(self, message: str) -> None:

        """
        Writes a new alert level log message to the log channel, if the
        configured log level allows it.

        Args:
            message:        The log message to write.

        Authors:
            Attila Kovacs.
        """

        if self._log_level <= LogLevels.ALERT:
            entry = self._make_entry(level=LogLevels.ALERT, message=message)
            self._log(entry=entry)

    def emergency(self, message: str) -> None:

        """
        Writes a new emergency level log message to the log channel, if the
        configured log level allows it.

        Args:
            message:        The log message to write.

        Authors:
            Attila Kovacs.
        """

        if self._log_level <= LogLevels.EMERGENCY:
            entry = self._make_entry(level=LogLevels.EMERGENCY, message=message)
            self._log(entry=entry)

    def _log(self, entry: LogEntry) -> None:

        """
        Adds a new log entry to the log.

        Args:
            entry:      The log entry to add.

        Authors:
            Attila Kovacs
        """

        # Try to attach to the log channel if not already attached
        if not self._channel:
                self._attach()

        if self._channel:
            # Empty the cache if there if there are cached entries
            self._flush_cache()
            self._channel.write(entry=entry)
        elif self._cache_entries:
            self._cache_entry(entry=entry)

    def _attach(self) -> 'LogChannel':

        """
        Attaches this log writer to a log channel the writer needs to write to.

        Returns:
            The log channel object that has been attached to.

        Authors:
            Attila Kovacs
        """

        channel = None

        # Get the channel based on its name
        log_service = ServiceLocator.instance().get_provider(LoggingService)

        if log_service:
            channel = log_service.get_channel(self._channel_name)

            if not channel:
                return None

            self._log_level = channel.DefaultLogLevel

        return channel

    def _make_entry(self, level: LogLevels, message: str) -> LogEntry:

        """
        Creates a new log entry.

        Args:
            level:      The log level the message was sent with.
            message:    The log message.

        Authors:
            Attila Kovacs
        """

        return LogEntry(level=level,
                        timestamp=datetime.utcnow(),
                        message=message,
                        classname=self.__class__.__name__):

    def _cache_entry(self, entry: LogEntry) -> None:

        """
        Adds a new entry to the log cache.

        Args:
            entry:      The log entry to cache.

        Authors:
            Attila Kovacs
        """

        self._cache.append(entry)

    def _flush_cache(self) -> None:

        """
        Sends all cached log entries to the channel.
        """

        for entry in self._cache:
            self._channel.write(entry)
        self._cache.clear()