from builder.scheme.elements.unit.generator import Generator
from builder.scheme.types import PlacementType, CarrierType
from test.test_builder.test_scheme import BaseTestEnergySystemScheme
import builder.scheme.error as err


class TestEnergySystemSchemeCarriers(BaseTestEnergySystemScheme):

    def test_add_fuel(self):
        self.system.add_carrier(self.coal)
        self.assertTrue(self.system.carriers[CarrierType.FUEL][self.coal.id] == self.coal)

    def test_add_profile(self):
        self.system.add_carrier(self.solar)
        self.assertTrue(self.system.carriers[CarrierType.PROFILE][self.solar.id] == self.solar)

    def test_add_one_fuel_one_profile(self):
        self.system.add_carrier(self.solar)
        self.system.add_carrier(self.coal)
        self.assertTrue(self.system.carriers[CarrierType.FUEL][self.coal.id] == self.coal)
        self.assertTrue(self.system.carriers[CarrierType.PROFILE][self.solar.id] == self.solar)

    def test_remove_fuel(self):
        self.system.add_carrier(self.coal)
        removed_element = self.system.remove_carrier(self.coal.id)
        self.assertTrue(len(self.system.carriers) == 0 and removed_element == self.coal)

    def test_remove_non_existing_fuel(self):
        self.system.add_carrier(self.coal)
        with self.assertRaises(err.SchemeElementNotFoundError):
            self.system.remove_carrier(self.coal.id + 1)

    def test_remove_fuel_of_existing_generator_raises_error(self):
        gen = Generator(name='boiler', placement=PlacementType.LOCAL, energy_type=self.heat, carrier_id=self.coal.id)
        self.system.add_energy_type(self.heat)
        self.system.add_carrier(self.coal)
        self.system.add_generator(gen)
        with self.assertRaises(err.SchemeExistingReferenceError):
            self.system.remove_carrier(self.coal.id)

    def test_remove_fuel_with_one_generator_of_other_fuel_do_not_raise_error(self):
        gen = Generator(name='boiler', placement=PlacementType.LOCAL, energy_type=self.heat, carrier_id=self.coal.id)
        self.system.add_energy_type(self.heat)
        self.system.add_carrier(self.gas)
        self.system.add_carrier(self.coal)
        self.system.add_generator(gen)
        try:
            removed_element = self.system.remove_carrier(self.gas.id)
        except err.SchemeExistingReferenceError:
            self.fail()
        self.assertTrue(removed_element == self.gas)
