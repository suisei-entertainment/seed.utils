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
Contains the unit tests of HostCPU class.
"""

# Platform Imports
import unittest

# SEED Imports
from suisei.seed.pal.host.hostcpu import HostCPU

# Test data
TEST_DATA = \
{
    'python_version': '3.7.1.final.0 (64 bit)',
    'cpuinfo_version': (4, 0, 0),
    'arch': 'X86_64',
    'bits': 64,
    'count': 16,
    'raw_arch_string': 'x86_64',
    'vendor_id': 'GenuineIntel',
    'brand': 'Intel(R) Xeon(R) CPU E5-2670 0 @ 2.60GHz',
    'hz_advertised': '2.6000 GHz',
    'hz_actual': '2.6000 GHz',
    'hz_advertised_raw': (2600000000, 0),
    'hz_actual_raw': (2600000000, 0),
    'stepping': 7,
    'model': 45,
    'family': 6,
    'flags':
    [   'aes',
        'aperfmperf',
        'apic',
        'arat',
        'arch_perfmon',
        'avx',
        'bts',
        'clflush',
        'cmov',
        'constant_tsc',
        'cpuid',
        'cx16',
        'cx8',
        'de',
        'dtherm',
        'dts',
        'epb',
        'fpu',
        'fxsr',
        'ht',
        'hypervisor',
        'ida',
        'lahf_lm',
        'lm',
        'mca',
        'mce',
        'mmx',
        'msr',
        'mtrr',
        'nonstop_tsc',
        'nopl',
        'nx',
        'osxsave',
        'pae',
        'pat',
        'pcid',
        'pclmulqdq',
        'pebs',
        'pge',
        'pln',
        'pni',
        'popcnt',
        'pse',
        'pse36',
        'pti',
        'pts',
        'rdtscp',
        'sep',
        'ss',
        'sse',
        'sse2',
        'sse4_1',
        'sse4_2',
        'ssse3',
        'syscall',
        'tsc',
        'tsc_adjust',
        'tsc_deadline_timer',
        'tsc_reliable',
        'tscdeadline',
        'vme',
        'x2apic',
        'xsave',
        'xtopology'
    ],
    'l3_cache_size': '20480 KB',
    'l2_cache_size': '256 KB',
    'l1_data_cache_size': '32 KB',
    'l1_instruction_cache_size': '32 KB',
    'l2_cache_line_size': 6,
    'l2_cache_associativity': '0x100',
    'extended_model': 2
}

class CPUDetectionTest(unittest.TestCase):

    """
    Contains the unit tests of HostCPU class.
    """

    @classmethod
    def setUpClass(cls):

        print('')
        print('*******************************************************************************')
        print('     >>>>> HostCPU <<<<<')
        print('*******************************************************************************')

    def test_creation(self):

        """
        Tests that the HostCPU object can be created without errors.
        """

        sut = HostCPU()

    def test_architecture_detection(self):

        """
        Tests that the host CPU architecture can be detected correctly.
        """

        # STEP #1 - Normal detection through cpuinfo
        sut = HostCPU()
        sut._detect_architecture(TEST_DATA)
        self.assertTrue(sut.Architecture in ('X86_64', 'AARCH64'))

        # STEP #2 - Fallback detection through platform
        sut = HostCPU()
        sut._detect_architecture({})
        self.assertTrue(sut.Architecture in ('X86_64', 'AARCH64'))

    def test_cpu_count_detection(self):

        """
        Tests that the amount of CPU cores can be detected correctly.
        """

        # STEP #1 - Normal detection through cpuinfo
        sut = HostCPU()
        sut._detect_cpu_count(TEST_DATA)
        self.assertEqual(sut.NumCores, 16)
        self.assertNotEqual(sut.NumPhysicalCores, -1)

        # STEP #2 - Fallback detection through multiprocessing
        sut = HostCPU()
        sut._detect_cpu_count({})
        self.assertNotEqual(sut.NumCores, -1)
        self.assertNotEqual(sut.NumPhysicalCores, -1)

    def test_cpu_type_detection(self):

        """
        Tests that the CPU type can be detected correctly.
        """

        # STEP #1 - Normal detection through cpuinfo
        sut = HostCPU()
        sut._detect_cpu_type(TEST_DATA)
        self.assertEqual(sut.VendorID, 'GenuineIntel')
        self.assertEqual(sut.Name, 'Intel(R) Xeon(R) CPU E5-2670 0 @ 2.60GHz')
        self.assertEqual(sut.Stepping, 7)
        self.assertEqual(sut.Model, 45)
        self.assertEqual(sut.ExtendedModel, 2)
        self.assertEqual(sut.Family, 6)

        # STEP #2 - Missing cpuinfo data
        sut = HostCPU()
        sut._detect_cpu_type({})
        self.assertEqual(sut.VendorID, 'UNKNOWN')
        self.assertEqual(sut.Name, 'UNKNOWN')
        self.assertEqual(sut.Stepping, -1)
        self.assertEqual(sut.Model, -1)
        self.assertEqual(sut.ExtendedModel, -1)
        self.assertEqual(sut.Family, -1)

    def test_cpu_speed_detection(self):

        """
        Tests that the CPU speed can be detected correctly.
        """

        # STEP #1 - Normal detection through cpuinfo
        sut = HostCPU()
        sut._detect_cpu_speed(TEST_DATA)
        self.assertEqual(sut.MaxSpeed, '2.6000 GHz')

        # STEP #2 - Detection with empty cpuinfo
        sut = HostCPU()
        sut._detect_cpu_speed({})
        self.assertEqual(sut.MaxSpeed, 'UNKNOWN')

    def test_cpu_cache_detection(self):

        """
        Tests that the CPU cache size can be detected correctly.
        """

        # STEP #1 - Normal detection through cpuinfo
        sut = HostCPU()
        sut._detect_cache_data(TEST_DATA)
        self.assertEqual(sut.L2CacheSize, '256 KB')

        # STEP #2 - Detection with empty cpuinfo
        sut = HostCPU()
        sut._detect_cache_data({})
        self.assertEqual(sut.L2CacheSize, 'UNKNOWN')

def load_tests(loader, tests, pattern):

    """
    Registers the test suite with the test runner.
    """

    suite = unittest.TestSuite()

    suite.addTest(CPUDetectionTest('test_creation'))
    suite.addTest(CPUDetectionTest('test_architecture_detection'))
    suite.addTest(CPUDetectionTest('test_cpu_count_detection'))
    suite.addTest(CPUDetectionTest('test_cpu_type_detection'))
    suite.addTest(CPUDetectionTest('test_cpu_speed_detection'))
    suite.addTest(CPUDetectionTest('test_cpu_cache_detection'))

    return suite