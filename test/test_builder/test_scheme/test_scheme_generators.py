from builder.scheme.elements.stack import Stack, StackTuple
from builder.scheme.elements.unit.generator import Generator
from builder.scheme.types import PlacementType
from test.test_builder.test_scheme import BaseTestEnergySystemScheme
import builder.scheme.error as err


class TestEnergySystemSchemeGenerators(BaseTestEnergySystemScheme):

    def setUp(self) -> None:
        super(TestEnergySystemSchemeGenerators, self).setUp()
        self.boiler = Generator(
            name='boiler', placement=PlacementType.LOCAL, energy_type=self.heat, carrier_id=self.coal)
        self.sol = Generator(
            name='pv', placement=PlacementType.LOCAL, energy_type=self.heat, carrier_id=self.solar)

    def test_add_generator(self):
        self.system.add_energy_types(self.heat)
        self.system.add_carriers(self.coal)
        self.system.add_generators(self.boiler)

        self.assertTrue(self.system.generators[self.boiler.id] == self.boiler)

    def test_add_two_different_generators(self):
        self.system.add_energy_types(self.heat)
        self.system.add_carriers(self.coal, self.solar)
        self.system.add_generators(self.sol, self.boiler)

        self.assertTrue(
            self.system.generators[self.sol.id] == self.sol and self.system.generators[self.boiler.id] == self.boiler
        )

    def test_add_generator_that_is_already_in_the_system_raises_error(self):
        self.system.add_energy_types(self.heat)
        self.system.add_carriers(self.solar)
        self.system.add_generators(self.sol)

        with self.assertRaises(err.DuplicateError):
            self.system.add_generators(self.sol)

    def test_add_generator_before_adding_energy_type_raises_error(self):
        self.system.add_carriers(self.solar)
        with self.assertRaises(err.SchemeNonExistingReferenceError):
            self.system.add_generators(self.sol)

    def test_add_generator_before_adding_carrier_raises_error(self):
        self.system.add_energy_types(self.heat)
        with self.assertRaises(err.SchemeNonExistingReferenceError):
            self.system.add_generators(self.sol)

    def test_remove_generator(self):
        self.system.add_energy_types(self.heat)
        self.system.add_carriers(self.solar)
        self.system.add_generators(self.sol)
        removed_item = self.system.remove_generator(self.sol.id)
        self.assertTrue(removed_item == self.sol)
        self.assertTrue(len(self.system.generators) == 0)

    def test_remove_non_existing_generator(self):
        self.system.add_energy_types(self.heat)
        self.system.add_carriers(self.solar)
        self.system.add_generators(self.sol)
        with self.assertRaises(err.ElementNotFoundError):
            self.system.remove_generator(self.boiler.id)

    def test_remove_generator_contained_in_existing_stack_raises_error(self):
        self.system.add_energy_types(self.heat)
        self.system.add_carriers(self.solar)
        self.system.add_generators(self.sol)

        test_stack = Stack(
            name='test_stack', members={self.heat: StackTuple(base=self.sol.id)}, placement=PlacementType.LOCAL)

        self.system.add_stacks(test_stack)
        with self.assertRaises(err.ExistingReferenceSchemeError):
            self.system.remove_generator(self.sol.id)

    def test_remove_generator_contained_in_non_existing_stack(self):

        self.system.add_energy_types(self.heat)
        self.system.add_carriers(self.solar)
        self.system.add_generators(self.sol)

        test_stack = Stack(
            name='test_stack', members={self.heat: StackTuple(base=self.sol.id)}, placement=PlacementType.LOCAL)
        self.system.add_stacks(test_stack)
        self.system.remove_stack(test_stack.id)

        try:
            self.system.remove_generator(self.sol.id)
        except err.ExistingReferenceSchemeError:
            self.fail()
