import unittest

from builder.scheme.scheme import EnergySystemScheme


class BaseTestEnergySystemScheme(unittest.TestCase):

    def setUp(self) -> None:
        self.system = EnergySystemScheme(name='test_energy_system')
