import unittest

from builder.scheme.elements.carrier import Fuel, Profile
from builder.scheme.scheme import EnergySystemScheme
from builder.scheme.types import EnergyType


class BaseTestEnergySystemScheme(unittest.TestCase):

    def setUp(self) -> None:
        self.system = EnergySystemScheme(name='test_energy_system')
        self.coal, self.gas = Fuel('coal'), Fuel('gas')
        self.heat, self.ee, self.solar = EnergyType('heat'), EnergyType('electricity'), Profile('solar_energy')
