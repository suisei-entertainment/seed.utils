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
Contains the implementation of a basic singleton class.
"""

class Singleton:

    """
    A non-thread-safe helper class to ease implementing singletons.

    This should be used as a decorator -- not a metaclass -- to the class that
    should be a singleton.

    The decorated class can define one `__init__` function that takes only the
    `self` argument. Also, the decorated class cannot be inherited from. Other
    than that, there are no restrictions that apply to the decorated class.

    To get the singleton instance, use the `instance` method. Trying to use
    `__call__` will result in a `TypeError` being raised.

    Authors:
        Attila Kovacs
    """

    def __init__(self, decorated: object) -> None:

        """
        Creates a new Singleton instance.

        Args:
            decorated:      The actual class that is created as a singleton.

        Authors:
            Attila Kovacs
        """

        self._decorated = decorated

    def instance(self) -> object:

        """
        Returns the singleton instance. Upon its first call, it creates a
        new instance of the decorated class and calls its `__init__` method.
        On all subsequent calls, the already created instance is returned.

        Authors:
            Attila Kovacs
        """

        #pylint: disable=attribute-defined-outside-init

        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance

    def __call__(self) -> None:

        """
        Prevents direct calls to the singleton class.

        Raises:
            TypeError:      Called when someone tries to access the decorated
                            class outside the instance() call.

        Authors:
            Attila Kovacs
        """

        raise TypeError('Singletons must be accessed through `instance()`.')

    def __instancecheck__(self, inst: object) -> bool:

        """
        Checks whether or not an object is the instance of the decorated class.

        Args:
            inst:       The object instance to check.

        Returns:
            'True' if the object is an instance of the decorated calss, 'False'
            otherwise.

        Authors:
            Attila Kovacs
        """

        return isinstance(inst, self._decorated)
