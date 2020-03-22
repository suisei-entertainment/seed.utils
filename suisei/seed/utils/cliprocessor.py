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
import argparse

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
                 command_map: list,
                 description_string: str = None,
                 usage_string: str = None,
                 epilog_string: str = None) -> None:

        """
        Creates a new CliProcessor instance.

        Args:
            command_map:            The command map to use to configure the
                                    class.
            description_string:     Optional description string to pass to
                                    argparse.
            usage_string:           Optional usage string to pass to argparse.
            epilog_string:          Optional epilog string to pass to argparse.

        Authors:
            Attila Kovacs
        """

        self._parser = argparse.ArgumentParser(
            description=description_string,
            usage=usage_string,
            epilog=epilog_string)

        self._register_commands(command_map)

    def process(self, args: list) -> argparse.Namespace:

        """
        Processes the command line arguments.

        Args:
            args:       The list of command line arguments the application was
                        called with.

        Returns:
            The processed command line arguments as an argparse Namespace
            object.

        Authors:
            Attila Kovacs
        """

        return self._parser.parse_args(args=args)

    def _register_commands(command_map: list) -> None:

        """
        Registers all CLI commands from the command map with the argument
        parser.

        Args:
            command_map:        The command map to configure.

        Authors:
            Attila Kovacs
        """

        return