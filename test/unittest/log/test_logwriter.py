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
Contains the unit tests of the LogWriter class.
"""

# Platform Imports
import os
import unittest

# SEED Imports
from suisei.seed.utils import ServiceLocator
from suisei.seed.log import LogWriter, LogLevels, LoggingService

class TestLoggingService:
    def __init__(self):
        ServiceLocator.instance().register_provider(LoggingService, self)
    def get_channel(self, name):
        return self
    @property
    def DefaultLogLevel(self):
        return LogLevels.INFO
    def write(self, entry):
        return

class LogWriterTest(unittest.TestCase):

    """
    Contains all unit tests of the LogWriter class.
    """

    @classmethod
    def setUpClass(cls):

        print('')
        print('*******************************************************************************')
        print('     >>>>> LogWriter <<<<<')
        print('*******************************************************************************')

    def test_creation(self):

        """
        Tests that a log writer can be created.
        """

        # STEP #1 - Log writer can be created without a logging service if
        #           caching is enabled
        sut = LogWriter(channel_name='test', cache_entries=True)
        self.assertIsNone(sut.LogLevel)

        # STEP #2 - Log writer can be created without a logging service if
        #           caching is not enabled
        sut = LogWriter(channel_name='test', cache_entries=False)
        self.assertIsNone(sut.LogLevel)

        # STEP #3 - Log writer can be created if there is a logging service
        service = TestLoggingService()
        sut = LogWriter(channel_name='test')
        self.assertEquals(sut.LogLevel, LogLevels.INFO)
        ServiceLocator.instance().reset()

    def test_log_level_overwrite(self):

        """
        Tests that log levels can be overwritten in the log writer.
        """

        # STEP #1 - Log level can be overwritten.
        sut = LogWriter(channel_name='test', cache_entries=False)
        self.assertIsNone(sut.LogLevel)
        sut.overwrite_log_level(new_log_level=LogLevels.WARNING)
        self.assertEquals(sut.LogLevel, LogLevels.WARNING)
        self.assertTrue(sut.IsLogLevelOverwritten)

        # STEP #2 - Log level overwrite can be disabled
        sut.reset_log_level()
        self.assertEquals(sut.LogLevel, LogLevels.INFO)
        self.assertFalse(sut.IsLogLevelOverwritten)

        # STEP #3 - Log level can be reset when there is a channel attached
        service = TestLoggingService()
        sut = LogWriter(channel_name='test')
        sut.overwrite_log_level(LogLevels.EMERGENCY)
        self.assertEquals(sut.LogLevel, LogLevels.EMERGENCY)
        sut.reset_log_level()
        self.assertEquals(sut.LogLevel, LogLevels.INFO)
        ServiceLocator.instance().reset()

    def test_debug_message(self):

        """
        Tests that DEBUG level messages are handled correctly.
        """

        # STEP #1 - Message is written if log level is DEBUG
        sut = LogWriter(channel_name='test', cache_entries=True)
        sut.overwrite_log_level(new_log_level=LogLevels.DEBUG)
        sut.debug(message='test')
        self.assertEquals(sut.CachedLogEntries[0].Message, 'test')

        # STEP #2 - Message is not writen if log level is above DEBUG
        sut = LogWriter(channel_name='test', cache_entries=True)
        sut.overwrite_log_level(new_log_level=LogLevels.INFO)
        sut.debug(message='test')
        self.assertFalse(sut.CachedLogEntries)

        # STEP #3 - Message is not writen if logging has been suspended
        sut = LogWriter(channel_name='test', cache_entries=True)
        sut.overwrite_log_level(new_log_level=LogLevels.DEBUG)
        sut.suspend_logging()
        sut.debug(message='test')
        self.assertFalse(sut.CachedLogEntries)

    def test_info_message(self):

        """
        Tests that INFO level messages are handled correctly.
        """

        # STEP #1 - Message is written if log level is below INFO
        sut = LogWriter(channel_name='test', cache_entries=True)
        sut.overwrite_log_level(new_log_level=LogLevels.DEBUG)
        sut.info(message='test')
        self.assertEquals(sut.CachedLogEntries[0].Message, 'test')

        # STEP #2 - Message is written if log level is INFO
        sut = LogWriter(channel_name='test', cache_entries=True)
        sut.overwrite_log_level(new_log_level=LogLevels.INFO)
        sut.info(message='test')
        self.assertEquals(sut.CachedLogEntries[0].Message, 'test')

        # STEP #3 - Message is not writen if log level is above INFO
        sut = LogWriter(channel_name='test', cache_entries=True)
        sut.overwrite_log_level(new_log_level=LogLevels.EMERGENCY)
        sut.info(message='test')
        self.assertFalse(sut.CachedLogEntries)

        # STEP #4 - Message is not writen if logging has been suspended
        sut = LogWriter(channel_name='test', cache_entries=True)
        sut.overwrite_log_level(new_log_level=LogLevels.DEBUG)
        sut.suspend_logging()
        sut.info(message='test')
        self.assertFalse(sut.CachedLogEntries)

    def test_notice_message(self):

        """
        Tests that NOTICE level messages are handled correctly.
        """

        # STEP #1 - Message is written if log level is below NOTICE
        sut = LogWriter(channel_name='test', cache_entries=True)
        sut.overwrite_log_level(new_log_level=LogLevels.DEBUG)
        sut.notice(message='test')
        self.assertEquals(sut.CachedLogEntries[0].Message, 'test')

        # STEP #2 - Message is written if log level is NOTICE
        sut = LogWriter(channel_name='test', cache_entries=True)
        sut.overwrite_log_level(new_log_level=LogLevels.NOTICE)
        sut.notice(message='test')
        self.assertEquals(sut.CachedLogEntries[0].Message, 'test')

        # STEP #3 - Message is not writen if log level is above NOTICE
        sut = LogWriter(channel_name='test', cache_entries=True)
        sut.overwrite_log_level(new_log_level=LogLevels.EMERGENCY)
        sut.notice(message='test')
        self.assertFalse(sut.CachedLogEntries)

        # STEP #4 - Message is not writen if logging has been suspended
        sut = LogWriter(channel_name='test', cache_entries=True)
        sut.overwrite_log_level(new_log_level=LogLevels.DEBUG)
        sut.suspend_logging()
        sut.notice(message='test')
        self.assertFalse(sut.CachedLogEntries)

    def test_warning_message(self):

        """
        Tests that NOTICE level messages are handled correctly.
        """

        # STEP #1 - Message is written if log level is below WARNING
        sut = LogWriter(channel_name='test', cache_entries=True)
        sut.overwrite_log_level(new_log_level=LogLevels.DEBUG)
        sut.warning(message='test')
        self.assertEquals(sut.CachedLogEntries[0].Message, 'test')

        # STEP #2 - Message is written if log level is WARNING
        sut = LogWriter(channel_name='test', cache_entries=True)
        sut.overwrite_log_level(new_log_level=LogLevels.WARNING)
        sut.warning(message='test')
        self.assertEquals(sut.CachedLogEntries[0].Message, 'test')

        # STEP #3 - Message is not writen if log level is above WARNING
        sut = LogWriter(channel_name='test', cache_entries=True)
        sut.overwrite_log_level(new_log_level=LogLevels.EMERGENCY)
        sut.warning(message='test')
        self.assertFalse(sut.CachedLogEntries)

        # STEP #4 - Message is not writen if logging has been suspended
        sut = LogWriter(channel_name='test', cache_entries=True)
        sut.overwrite_log_level(new_log_level=LogLevels.DEBUG)
        sut.suspend_logging()
        sut.warning(message='test')
        self.assertFalse(sut.CachedLogEntries)

    def test_error_message(self):

        """
        Tests that ERROR level messages are handled correctly.
        """

        # STEP #1 - Message is written if log level is below ERROR
        sut = LogWriter(channel_name='test', cache_entries=True)
        sut.overwrite_log_level(new_log_level=LogLevels.DEBUG)
        sut.error(message='test')
        self.assertEquals(sut.CachedLogEntries[0].Message, 'test')

        # STEP #2 - Message is written if log level is ERROR
        sut = LogWriter(channel_name='test', cache_entries=True)
        sut.overwrite_log_level(new_log_level=LogLevels.ERROR)
        sut.error(message='test')
        self.assertEquals(sut.CachedLogEntries[0].Message, 'test')

        # STEP #3 - Message is not writen if log level is above ERROR
        sut = LogWriter(channel_name='test', cache_entries=True)
        sut.overwrite_log_level(new_log_level=LogLevels.EMERGENCY)
        sut.error(message='test')
        self.assertFalse(sut.CachedLogEntries)

        # STEP #5 - Message is not writen if logging has been suspended
        sut = LogWriter(channel_name='test', cache_entries=True)
        sut.overwrite_log_level(new_log_level=LogLevels.DEBUG)
        sut.suspend_logging()
        sut.error(message='test')
        self.assertFalse(sut.CachedLogEntries)

    def test_critical_message(self):

        """
        Tests that CRITICAL level messages are handled correctly.
        """

        # STEP #1 - Message is written if log level is below CRITICAL
        sut = LogWriter(channel_name='test', cache_entries=True)
        sut.overwrite_log_level(new_log_level=LogLevels.DEBUG)
        sut.critical(message='test')
        self.assertEquals(sut.CachedLogEntries[0].Message, 'test')

        # STEP #2 - Message is written if log level is CRITICAL
        sut = LogWriter(channel_name='test', cache_entries=True)
        sut.overwrite_log_level(new_log_level=LogLevels.CRITICAL)
        sut.critical(message='test')
        self.assertEquals(sut.CachedLogEntries[0].Message, 'test')

        # STEP #3 - Message is not writen if log level is above CRITICAL
        sut = LogWriter(channel_name='test', cache_entries=True)
        sut.overwrite_log_level(new_log_level=LogLevels.EMERGENCY)
        sut.critical(message='test')
        self.assertFalse(sut.CachedLogEntries)

        # STEP #4 - Message is not writen if logging has been suspended
        sut = LogWriter(channel_name='test', cache_entries=True)
        sut.overwrite_log_level(new_log_level=LogLevels.DEBUG)
        sut.suspend_logging()
        sut.critical(message='test')
        self.assertFalse(sut.CachedLogEntries)

    def test_alert_message(self):

        """
        Tests that ALERT level messages are handled correctly.
        """

        # STEP #1 - Message is written if log level is below ALERT
        sut = LogWriter(channel_name='test', cache_entries=True)
        sut.overwrite_log_level(new_log_level=LogLevels.DEBUG)
        sut.alert(message='test')
        self.assertEquals(sut.CachedLogEntries[0].Message, 'test')

        # STEP #2 - Message is written if log level is ALERT
        sut = LogWriter(channel_name='test', cache_entries=True)
        sut.overwrite_log_level(new_log_level=LogLevels.ALERT)
        sut.alert(message='test')
        self.assertEquals(sut.CachedLogEntries[0].Message, 'test')

        # STEP #3 - Message is not writen if log level is above ALERT
        sut = LogWriter(channel_name='test', cache_entries=True)
        sut.overwrite_log_level(new_log_level=LogLevels.EMERGENCY)
        sut.alert(message='test')
        self.assertFalse(sut.CachedLogEntries)

        # STEP #4 - Message is not writen if logging has been suspended
        sut = LogWriter(channel_name='test', cache_entries=True)
        sut.overwrite_log_level(new_log_level=LogLevels.DEBUG)
        sut.suspend_logging()
        sut.alert(message='test')
        self.assertFalse(sut.CachedLogEntries)

    def test_emergency_message(self):

        """
        Tests that EMERGENCY level messages are handled correctly.
        """

        # STEP #1 - Message is written if log level is below EMERGENCY
        sut = LogWriter(channel_name='test', cache_entries=True)
        sut.overwrite_log_level(new_log_level=LogLevels.DEBUG)
        sut.emergency(message='test')
        self.assertEquals(sut.CachedLogEntries[0].Message, 'test')

        # STEP #2 - Message is written if log level is EMERGENCY
        sut = LogWriter(channel_name='test', cache_entries=True)
        sut.overwrite_log_level(new_log_level=LogLevels.EMERGENCY)
        sut.emergency(message='test')
        self.assertEquals(sut.CachedLogEntries[0].Message, 'test')

        # STEP #3 - Message is not writen if logging has been suspended
        sut = LogWriter(channel_name='test', cache_entries=True)
        sut.overwrite_log_level(new_log_level=LogLevels.DEBUG)
        sut.suspend_logging()
        sut.emergency(message='test')
        self.assertFalse(sut.CachedLogEntries)

    def test_logging_suspension(self):

        """
        Tests that logging can be suspended and resumed.
        """

        # STEP #1 - Logging can be suspended
        sut = LogWriter(channel_name='test', cache_entries=True)
        sut.suspend_logging()
        self.assertTrue(sut.IsLoggingSuspended)

        # STEP #2 - Logging can be resumed
        sut.resume_logging()
        self.assertFalse(sut.IsLoggingSuspended)

def load_tests(loader, tests, pattern):

    """
    Registers the test suite with the test runner.
    """

    suite = unittest.TestSuite()

    suite.addTest(LogWriterTest('test_creation'))
    suite.addTest(LogWriterTest('test_log_level_overwrite'))
    suite.addTest(LogWriterTest('test_debug_message'))
    suite.addTest(LogWriterTest('test_info_message'))
    suite.addTest(LogWriterTest('test_notice_message'))
    suite.addTest(LogWriterTest('test_warning_message'))
    suite.addTest(LogWriterTest('test_error_message'))
    suite.addTest(LogWriterTest('test_critical_message'))
    suite.addTest(LogWriterTest('test_alert_message'))
    suite.addTest(LogWriterTest('test_emergency_message'))
    suite.addTest(LogWriterTest('test_logging_suspension'))

    return suite
