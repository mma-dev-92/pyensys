from builder.scheme.elements.stack import Stack, StackTuple
from builder.scheme.elements.unit.generator import Generator
from builder.scheme.types import PlacementType
from test.test_builder.test_scheme import BaseTestEnergySystemScheme
import builder.scheme.error as err


class TestEnergySystemSchemeGenerators(BaseTestEnergySystemScheme):

    def setUp(self) -> None:
        super(TestEnergySystemSchemeGenerators, self).setUp()
        self.boiler = Generator(
            name='boiler', placement=PlacementType.LOCAL, energy_type=self.heat, carrier_id=self.coal.id)
        self.sol = Generator(
            name='pv', placement=PlacementType.LOCAL, energy_type=self.heat, carrier_id=self.solar.id)

    def test_add_generator(self):
        self.system.add_energy_type(self.heat)
        self.system.add_carrier(self.coal)
        self.system.add_generator(self.boiler)

        self.assertTrue(self.system.generators[self.boiler.id] == self.boiler)

    def test_add_two_different_generators(self):
        self.system.add_energy_type(self.heat)
        self.system.add_carrier(self.coal)
        self.system.add_carrier(self.solar)

        self.system.add_generator(self.sol)
        self.system.add_generator(self.boiler)

        self.assertTrue(
            self.system.generators[self.sol.id] == self.sol and self.system.generators[self.boiler.id] == self.boiler
        )

    def test_add_generator_that_is_already_in_the_system_raise_error(self):
        self.system.add_energy_type(self.heat)
        self.system.add_carrier(self.solar)
        self.system.add_generator(self.sol)

        with self.assertRaises(err.SchemeDuplicateError):
            self.system.add_generator(self.sol)

    def test_add_generator_before_adding_energy_type_raise_error(self):
        self.system.add_carrier(self.solar)
        with self.assertRaises(err.SchemeElementNotFoundError):
            self.system.add_generator(self.sol)

    def test_add_generator_before_adding_carrier_raise_error(self):
        self.system.add_energy_type(self.heat)
        with self.assertRaises(err.SchemeElementNotFoundError):
            self.system.add_generator(self.sol)

    def test_remove_generator(self):
        self.system.add_energy_type(self.heat)
        self.system.add_carrier(self.solar)
        self.system.add_generator(self.sol)
        removed_item = self.system.remove_generator(self.sol.id)
        self.assertTrue(removed_item == self.sol)
        self.assertTrue(len(self.system.generators) == 0)

    def test_remove_non_existing_generator(self):
        self.system.add_energy_type(self.heat)
        self.system.add_carrier(self.solar)
        self.system.add_generator(self.sol)
        with self.assertRaises(err.SchemeElementNotFoundError):
            self.system.remove_generator(self.boiler.id)

    def test_remove_generator_contained_in_existing_stack_raise_error(self):
        self.system.add_energy_type(self.heat)
        self.system.add_carrier(self.solar)
        self.system.add_generator(self.sol)

        test_stack = Stack(
            name='test_stack', members={self.heat: StackTuple(base=self.sol.id)}, placement=PlacementType.LOCAL)

        self.system.add_stack(test_stack)
        with self.assertRaises(err.SchemeExistingReferenceError):
            self.system.remove_generator(self.sol.id)

    def test_remove_generator_contained_in_non_existing_stack(self):

        self.system.add_energy_type(self.heat)
        self.system.add_carrier(self.solar)
        self.system.add_generator(self.sol)

        test_stack = Stack(
            name='test_stack', members={self.heat: StackTuple(base=self.sol.id)}, placement=PlacementType.LOCAL)
        self.system.add_stack(test_stack)
        self.system.remove_stack(test_stack.id)

        try:
            self.system.remove_generator(self.sol.id)
        except err.SchemeExistingReferenceError:
            self.fail()