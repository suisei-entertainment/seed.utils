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
Contains the unit tests of PhysicalInterface class.
"""

# Platform Imports
import unittest

# SEED Imports
from suisei.seed.pal.host.hostnetworking import PhysicalInterface

class PhysicalInterfaceTest(unittest.TestCase):

    """
    Contains the unit tests of PhysicalInterface class.
    """

    @classmethod
    def setUpClass(cls):

        print('')
        print('*******************************************************************************')
        print('     >>>>> PhysicalInterface <<<<<')
        print('*******************************************************************************')

    def test_creation(self):

        """
        Tests that a PhysicalInterface instance can be created.
        """

        sut = PhysicalInterface(interface_name='test')
        self.assertEqual(sut.Name, 'test')

    def test_link_address_handling(self):

        """
        Tests that link adddresses are handled correctly.
        """

        sut = PhysicalInterface(interface_name='test')
        self.assertEqual(sut.has_link_address('00:0A:95:9D:68:16'), False)
        sut.add_link_address(address='00:0A:95:9D:68:16')
        self.assertEqual(sut.has_link_address('00:0A:95:9D:68:16'), True)
        self.assertEqual(sut.has_link_address('00:0A:95:9D:68:FF'), False)
        sut.add_link_address(address='00:0A:95:9D:68:16')

    def test_ipv4_address_handling(self):

        """
        Tests that IPv4 addresses are handled correctly.
        """

        sut = PhysicalInterface(interface_name='test')
        self.assertEqual(sut.has_ipv4_address('192.168.0.1'), False)
        sut.add_ipv4_address(address='192.168.0.1',
                             netmask='255.255.255.0',
                             broadcast_address='192.168.0.255',
                             is_localhost=False,
                             is_link_local_address=False)
        self.assertEqual(sut.has_ipv4_address('192.168.0.1'), True)
        self.assertEqual(sut.has_ipv4_address('192.168.0.2'), False)
        sut.add_ipv4_address(address='192.168.0.1',
                             netmask='255.255.255.0',
                             broadcast_address='192.168.0.255',
                             is_localhost=False,
                             is_link_local_address=False)

    def test_ipv6_address_handling(self):

        """
        Tests that IPv6 addresses are handled correctly.
        """

        sut = PhysicalInterface(interface_name='test')
        self.assertEqual(
            sut.has_ipv6_address('2001:0db8:85a3:0000:0000:8a2e:0370:7334'),
            False)
        sut.add_ipv6_address(address='2001:0db8:85a3:0000:0000:8a2e:0370:7334',
                             netmask='ffff:ffff:ffff::',
                             broadcast_address='',
                             is_localhost=False,
                             is_link_local_address=False)
        self.assertEqual(
            sut.has_ipv6_address('2001:0db8:85a3:0000:0000:8a2e:0370:7334'),
            True)
        self.assertEqual(
            sut.has_ipv6_address('2001:0db8:85a3:0000:0000:8a2e:0370:7335'),
            False)
        sut.add_ipv6_address(address='2001:0db8:85a3:0000:0000:8a2e:0370:7334',
                             netmask='ffff:ffff:ffff::',
                             broadcast_address='',
                             is_localhost=False,
                             is_link_local_address=False)

def load_tests(loader, tests, pattern):

    """
    Registers the test suite with the test runner.
    """

    suite = unittest.TestSuite()

    suite.addTest(PhysicalInterfaceTest('test_creation'))
    suite.addTest(PhysicalInterfaceTest('test_link_address_handling'))
    suite.addTest(PhysicalInterfaceTest('test_ipv4_address_handling'))
    suite.addTest(PhysicalInterfaceTest('test_ipv6_address_handling'))

    return suite
