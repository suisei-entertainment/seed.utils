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
Contains the unit tests of IpAddress class.
"""

# Platform Imports
import unittest

# SEED Imports
from suisei.seed.pal.host.ipaddress import IPAddress
from suisei.seed.pal.host.ipv4address import IPv4Address
from suisei.seed.pal.host.ipv6address import IPv6Address

class IPAddressTest(unittest.TestCase):

    """
    Contains the unit tests of IpAddress class.
    """

    @classmethod
    def setUpClass(cls):

        print('')
        print('*******************************************************************************')
        print('     >>>>> IPAddress <<<<<')
        print('*******************************************************************************')

    def test_creation(self):

        """
        Tests that a IpAddress instance can be created.
        """

        sut = IPAddress(address='192.168.0.1',
                        netmask='255.255.255.0',
                        broadcast_address='192.168.0.255',
                        is_localhost=False,
                        is_link_local_address=False)

        self.assertEqual(sut.Address, '192.168.0.1')
        self.assertEqual(sut.Netmask, '255.255.255.0')
        self.assertEqual(sut.BroadcastAddress, '192.168.0.255')
        self.assertEqual(sut.is_localhost(), False)
        self.assertEqual(sut.is_link_local_address(), False)

        sut = IPv4Address(address='192.168.0.1',
                          netmask='255.255.255.0',
                          broadcast_address='192.168.0.255',
                          is_localhost=False,
                          is_link_local_address=False)

        self.assertEqual(sut.Address, '192.168.0.1')
        self.assertEqual(sut.Netmask, '255.255.255.0')
        self.assertEqual(sut.BroadcastAddress, '192.168.0.255')
        self.assertEqual(sut.is_localhost(), False)
        self.assertEqual(sut.is_link_local_address(), False)

        sut = IPv6Address(address='2001:0db8:85a3:0000:0000:8a2e:0370:7334',
                          netmask='ffff:ffff:ffff::',
                          broadcast_address='',
                          is_localhost=False,
                          is_link_local_address=False)

        self.assertEqual(sut.Address, '2001:0db8:85a3:0000:0000:8a2e:0370:7334')
        self.assertEqual(sut.Netmask, 'ffff:ffff:ffff::')
        self.assertEqual(sut.BroadcastAddress, '')
        self.assertEqual(sut.is_localhost(), False)
        self.assertEqual(sut.is_link_local_address(), False)

def load_tests(loader, tests, pattern):

    """
    Registers the test suite with the test runner.
    """

    suite = unittest.TestSuite()

    suite.addTest(IPAddressTest('test_creation'))

    return suite
