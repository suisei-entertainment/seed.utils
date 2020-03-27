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
Contains the implementation of the CliProcessor class.
"""

# Platform Imports
import os
import argparse
from typing import Callable

# SEED Imports
from .jsonfile import JsonFile

class CliProcessor:

    """
    Utility class based on argparse to simplify the configuration and
    processing of CLI commands.

    Authors:
        Attila Kovacs
    """

    @property
    def Parser(self) -> argparse.ArgumentParser:

        """
        Provides access to the underlying ArgumentParser object.

        Authors:
            Attila Kovacs
        """

        return self._parser

    def __init__(self,
                 command_map: list = None,
                 config_file: str = None,
                 description_string: str = None,
                 usage_string: str = None,
                 epilog_string: str = None) -> None:

        """
        Creates a new CliProcessor instance.

        Args:
            command_map:            The command map to use to configure the
                                    class.
            config_file:            Optional path to config file containing the
                                    command map to use. If a path is provided,
                                    it will overwrite the command map.
            description_string:     Optional description string to pass to
                                    argparse.
            usage_string:           Optional usage string to pass to argparse.
            epilog_string:          Optional epilog string to pass to argparse.

        Authors:
            Attila Kovacs
        """

        # Check that either a command map or a config file is provided.
        if command_map is None and config_file is None:
            raise InvalidInputError(
                'Either a command map or a config file has to be provided to '
                'configure the command line processor.')

        # Basic setup of argument parser
        self._parser = argparse.ArgumentParser(
            description=description_string,
            usage=usage_string,
            epilog=epilog_string)

        # Load the config file if it is provided
        if config_file:
            config_file = os.path.abspath(os.path.expanduser(config_file))

        if config_file and os.path.isfile(config_file):
            conf = JsonFile(path=config_file)

            try:
                conf.load()
                command_map = conf.Content
            except InvalidInputError:
                # If the config file cannot be loaded, fall back to the command
                # map if it has been provided, only raise the exception if it's
                # not available.
                if not command_map:
                    raise

        # Configure commands
        try:
            self._register_commands(command_map)
        except InvalidInputError:
            raise

    def process(self,
                args: list,
                cb_argument_processor: Callable) -> argparse.Namespace:

        """
        Processes the command line arguments.

        Args:
            args:                   The list of command line arguments the
                                    application was called with.
            cb_argument_processor:  A callback function that will be called
                                    after the command line has been parsed.

        Returns:
            The processed command line arguments as an argparse Namespace
            object.

        Authors:
            Attila Kovacs
        """

        arguments = self._parser.parse_args(args=args)

        if arguments:
            cb_argument_processor(arguments)

        return arguments

    def _register_commands(self, command_map: list) -> None:

        """
        Registers all CLI commands from the command map with the argument
        parser.

        Args:
            command_map:        The command map to configure.

        Raises:
            InvalidInputError:  Raised when the type of a command map element
                                cannot be determined.

        Authors:
            Attila Kovacs
        """

        # Iterate over the command map and process the content
        for element in command_map:
            try:
                element_type = element['type']
            except KeyError:
                raise InvalidInputError(
                    'Failed to determine the type of an element in the '
                    'command map. No type field was found. Element: {}'.format(
                        element))
            if element_type == 'group':
                self._register_group(element)
            elif element_type == 'switch':
                self._register_switch(element=element, target=self._parser)
            elif element_type == 'config':
                self._register_config(element=element, target=self._parser)
            else:
                raise InvalidInputError(
                    'Unknown command type {} encountered.'.format(
                        element_type))

    def _register_group(self, element: dict) -> None:

        """
        Registers a new command group in the parser.

        Args:
            element:        The group descriptor to register.

        Raises:
            InvalidInputError:  Raised when the name or description of a
                                command group is not specified in the
                                configuration.
            InvalidInputError:  Raised when there is no command list specified
                                in the configuration.
            InvalidInputError:  Raised when there is no command type specified
                                for a command in the command group.
            InvalidInputError:  Raised when an invalid command tyhpe is
                                encountered.

        Authors:
            Attila Kovacs
        """

        # Get group parameters
        try:
            name = element['name']
            description = element['description']
        except KeyError:
            raise InvalidInputError(
                'Command group name or description was not found in '
                'element {}'.format(element))

        # Add the group to the parser
        group = self._parser.add_argument_group(name, description=description)

        # Add commands to the group
        commands = None

        # Get commands
        try:
            commands = element['commands']
        except KeyError:
            raise InvalidInputError(
                'No commands list was found in command group {}'.format(name))

        # Register all commands based on type
        for command in commands:

            try:
                command_type = command['type']
            except KeyError:
                raise InvalidInputError(
                    'No command type specified in command {}'.format(command))

            if command_type == 'switch':
                self._register_switch(element=command, target=group)
            elif command_type == 'config':
                self._register_config(element=command, target=group)
            else:
                raise InvalidInputError(
                    'Invalid command type {} encountered.'.format(
                        command_type))

    @staticmethod
    def _register_switch(element: dict, target: object) -> None:

        """
        Registers a new switch type command in the parser.

        Args:
            element:            The command descriptor to register.
            target:             Where the command will be registered. Either
                                the parser itself, or an argument group.

        Raises:
            InvalidInputError:  Raised when a mandatory parameter is missing
                                from the configuration.

        Authors:
            Attila Kovacs
        """

        short_key = None
        command = None
        helptext = None

        try:
            short_key = element['shortkey']
            command = element['command']
            helptext = element['help']
        except KeyError:
            raise InvalidInputError(
                'Missing parameters when processing switch command {}'.format(
                    element))

        default = None
        try:
            default = element['default']
        except KeyError:
            default = False

        if short_key == '':
            target.add_argument(command,
                                help=helptext,
                                action='store_true',
                                default=default)
        else:
            target.add_argument(short_key,
                                command,
                                help=helptext,
                                action='store_true',
                                default=default)

    @staticmethod
    def _register_config(element: dict, target: object) -> None:

        """
        Registers a new config option type command in the parser.

        Args:
            element:        The command descriptor to register.
            target:         Where the command will be registered. Either the
                            parser itself, or an argument group.

        Raises:
            InvalidInputError:  Raised when a mandatory parameter is missing
                                from the configuration.

        Authors:
            Attila Kovacs
        """

        short_key = None
        command = None
        helptext = None

        try:
            short_key = element['shortkey']
            command = element['command']
            helptext = element['help']
        except KeyError:
            raise InvalidInputError(
                'Missing parameters when processing switch command {}'.format(
                    element))

        metavar = None
        try:
            metavar = element['metavar']
        except KeyError:
            metavar = False

        if short_key == '':
            target.add_argument(command,
                                help=helptext,
                                action='store',
                                metavar=metavar)
        else:
            target.add_argument(short_key,
                                command,
                                help=helptext,
                                action='store',
                                metavar=metavar)
