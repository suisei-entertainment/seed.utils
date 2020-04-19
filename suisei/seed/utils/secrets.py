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
Contains the implementation of the Secrets class.
"""

# Platform Imports
import os

# SEED Imports
from suisei.seed.exceptions import InvalidInputError
from .jsonfile import JsonFile

class Secrets:

    """
    Simple utility class to load an encrypted JSON file from the application's
    configuration directory and read keys from it.

    To decrypt the secrets file the decryption key is read from an environment
    variable.

    Authors:
        Attila Kovacs
    """

    def __init__(self, config_directory: str) -> None:

        """
        Creates a new Secrets instance.

        Args:
            config_directory:       Path to the directory where application
                                    configuration is stored.

        Authors:
            Kovacs Attila
        """

        # Path to the directory where application configuration is stored.
        self._config_directory = config_directory

    @staticmethod
    def retrieve_key() -> str:

        """
        Callback function to retrieve the decryption key for the secrets.conf
        file.

        Returns:
            The decryption key as a string, or None if the key cannot be
            retrieved.

        Authors:
            Attila Kovacs
        """

        pwd = os.getenv('SEED_SECRETS_KEY')
        if not pwd:
            return None

        return pwd

    def get_secret(self, key: str) -> str:

        """
        Loads the secrets file to memory and reads the given key from it.

        Args:
            key:        The key to read from the file.

        Returns:
            The value of the given key, or None if the key cannot be retrieved.

        Authors:
            Attila Kovacs
        """

        file_path = os.path.abspath(os.path.expanduser(
            '{}/secrets.conf').format(self._config_directory))

        # Check whether or not the file exists
        if not os.path.isfile(file_path):
            return None

        # Load the file and decrypt it
        file = JsonFile(path=file_path, cb_retrieve_key=Secrets.retrieve_key)

        try:
            file.load()
        except InvalidInputError:
            return None

        try:
            return file.Content[key]
        except KeyError:
            return None
