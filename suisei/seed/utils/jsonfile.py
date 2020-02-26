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
Utility class to help in parsing and handling JSON files.
"""

# Platform Imports
import os
import json
from typing import Callable

# Framework Imports
from suisei.seed.exceptions import InvalidInputError

from .aes import AESCipher

class JsonFile:

    """
    Represents a single JSON file on disk. The content of the file can be
    encrypted.

    Authors:
        Attila Kovacs
    """

    @property
    def Path(self) -> str:

        """
        Provides access to the path of the file.

        Authors:
            Attila Kovacs
        """

        return self._path

    @property
    def Content(self) -> dict:

        """
        Provides access to the content of the JSON file.

        Authors:
            Attila Kovacs
        """

        return self._content

    def __init__(self, path: str, cb_retrieve_key: Callable = None) -> None:

        """
        Creates a new JsonFile instance.

        Args:
            path:               Path to the JSON file on disk.
            cb_retrieve_key:    Optional callback function that will be called
                                to retrieve the key to decrypt the file.

        Authors:
            Attila Kovacs
        """

        self._path = os.path.abspath(path)
        """
        Path to the JSON file.
        """

        self._content = {}
        """
        The content of the JSON file.
        """

        self._cb_retrieve_key = cb_retrieve_key

    def load(self) -> None:

        """
        Attempts to load the file from disk. If the file doesn't exist, it will
        create an empty JSON structure in memory.

        Raises:
            InvalidInputError:      Raised when the file cannot be loaded from
                                    disk or its content cannot be parsed as a
                                    valid JSON.

        Authors:
            Attila Kovacs
        """

        if self._file_exists():

            if self._cb_retrieve_key is None:
                self._load_unencrypted()
            else:
                self._load_encrypted()
        else:
            # Just create an empty structure.
            self._content = {}

    def save(self, compact: bool = True) -> None:

        """
        Saves the content of the JSON file to disk.

        Args:
            compact:    Specifies whether or not the file should be saved in a
                        compact, less readable format, or in a properly
                        indented and formatted way. This has no effect on
                        encrypted JSON files.

        Raises:
            RuntimeError:       Raised when the file cannot be saved to disk.

        Authors:
            Attila Kovacs
        """

        if self._cb_retrieve_key is None:

            # Save the file unencrypted.
            try:
                with open(self._path, 'w+') as json_file:
                    if compact:
                        json.dump(self._content, json_file)
                    else:
                        json.dump(self._content,
                                  json_file,
                                  indent=4,
                                  separators=(',', ': '))
            except OSError:
                raise RuntimeError(
                    'Failed to save the content of JSON file to {}.'.format(
                        self._path))

        else:

            # Encrypt the file before saving
            cipher = AESCipher(self._cb_retrieve_key())
            encrypted_content = cipher.encrypt(json.dumps(self._content))

            try:
                with open(self._path, 'wb') as encrypted_file:
                    encrypted_file.write(encrypted_content)
            except OSError:
                raise RuntimeError(
                    'Failed to save the content of JSON file to {}.'.format(
                        self._path))

    def overwrite_content(self, content: dict) -> None:

        """
        Overwrites the content of the JSON file with the content of a
        dictionary.

        Args:
            content:            The new content of the JSON file.

        Authors:
            Attila Kovacs
        """

        self._content = content

    def _file_exists(self) -> bool:

        """
        Returns whether or not the file exists on disk.

        Returns:
            'True' if the file existsm 'False' otherwise.

        Authors:
            Attila Kovacs
        """

        return os.path.isfile(self._path)

    def _load_unencrypted(self) -> None:

        """
        Try to load the file as an unencrypted JSON file.

        Authors:
            Attila Kovacs
        """

        try:
            with open(self._path, 'r+') as json_file:
                # Parse the file and load the content to memory.
                self._content = json.load(json_file)
        except OSError:
            self._content = None
            raise InvalidInputError(
                'Failed to read the contents of JSON file {}.'.format(
                    self._path))
        except json.JSONDecodeError:
            self._content = None
            raise InvalidInputError(
                'Failed to parse the content of JSON file {}.'.format(
                    self._path))

    def _load_encrypted(self) -> None:

        """
        Try to load and decrypt the file.

        Authors:
            Attila Kovacs
        """

        raw_content = None
        try:
            with open(self._path, 'rb') as raw_file:
                raw_content = raw_file.read()
        except OSError:
            raise InvalidInputError(
                'Failed to read the file from disk: {}.'.format(
                    self._path))

        if raw_content is not None:

            # Try to load as a regular JSON file
            try:
                cipher = AESCipher(self._cb_retrieve_key())
                self._content = json.loads(
                    cipher.decrypt(raw_content))
            except json.JSONDecodeError:
                raise InvalidInputError(
                    'Failed to parse the content of JSON file {}. '
                    'Either the decryption key was wrong or the file '
                    'is not a valid JSON file.'.format(self._path))
