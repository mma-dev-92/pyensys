from builder.scheme.elements.stack import Stack, StackTuple
from builder.scheme.elements.unit.generator import Generator
from builder.scheme.elements.unit.storage import Storage
from builder.scheme.elements.zone import Zone
from builder.scheme.types import PlacementType
from test.test_builder.test_scheme import BaseTestEnergySystemScheme
import builder.scheme.error as err


class TestEnergySystemSchemeStacks(BaseTestEnergySystemScheme):

    def setUp(self) -> None:
        super(TestEnergySystemSchemeStacks, self).setUp()
        self.base_central = Generator(
            name='central_base', placement=PlacementType.CENTRAL, energy_type=self.heat, carrier_id=self.coal)
        self.base_local = Generator(
            name='local_base', placement=PlacementType.LOCAL, energy_type=self.heat, carrier_id=self.gas)
        self.peak_central = Generator(
            name='central_peak', placement=PlacementType.CENTRAL, energy_type=self.heat, carrier_id=self.solar)
        self.peak_local = Generator(
            name='local_peak', placement=PlacementType.LOCAL, energy_type=self.heat, carrier_id=self.gas)
        self.storage_central = Storage(name='storage_central', placement=PlacementType.CENTRAL, energy_type=self.heat)
        self.storage_local = Storage(name='storage_local', placement=PlacementType.LOCAL, energy_type=self.heat)

        self.system.add_energy_types(self.heat)
        self.system.add_carriers(self.coal, self.gas, self.solar)
        self.system.add_generators(self.base_local, self.base_central, self.peak_local, self.peak_central)
        self.system.add_storages(self.storage_central, self.storage_local)

        self.simple_local_stack = Stack(
            name='simple_stack',
            members={
                self.heat: StackTuple(base=self.base_local.id, peak=self.peak_local.id, storage=self.storage_local.id)
            },
            placement=PlacementType.LOCAL
        )

    def test_add_stack(self):
        self.system.add_stacks(self.simple_local_stack)
        self.assertTrue(self.system.stacks[self.simple_local_stack.id] == self.simple_local_stack)

    def test_add_stack_with_non_existing_energy_type_raises_error(self):
        self.system.remove_energy_type(self.heat)
        self.assertTrue(len(self.system.energy_types) == 0)
        with self.assertRaises(err.SchemeNonExistingReferenceError):
            self.system.add_stacks(self.simple_local_stack)

    def test_add_duplicate_raises_error(self):
        self.system.add_stacks(self.simple_local_stack)
        with self.assertRaises(err.DuplicateError):
            self.system.add_stacks(self.simple_local_stack)

    def test_add_stack_with_non_existing_base_generator_raises_error(self):
        self.system.remove_generator(self.base_local.id)
        self.assertTrue(self.base_local.id not in self.system.generators)
        with self.assertRaises(err.SchemeNonExistingReferenceError):
            self.system.add_stacks(self.simple_local_stack)

    def test_add_stack_with_non_existing_peak_generator_raises_error(self):
        self.system.remove_generator(self.peak_local.id)
        self.assertTrue(self.peak_local.id not in self.system.generators)
        with self.assertRaises(err.SchemeNonExistingReferenceError):
            self.system.add_stacks(self.simple_local_stack)

    def test_add_stack_with_non_existing_storage_raises_error(self):
        self.system.remove_storage(self.storage_local.id)
        self.assertTrue(self.storage_local.id not in self.system.storages)
        with self.assertRaises(err.SchemeNonExistingReferenceError):
            self.system.add_stacks(self.simple_local_stack)

    def test_add_central_stack_with_local_storage_raises_error(self):
        with self.assertRaises(err.SchemeIncompatiblePlacementTypeError):
            self.system.add_stacks(Stack(
                name='err_stack',
                members={self.heat: StackTuple(self.base_central.id, peak=None, storage=self.storage_local.id)},
                placement=PlacementType.CENTRAL
            ))

    def test_remove_stack(self):
        self.system.add_stacks(self.simple_local_stack)
        self.assertTrue(self.simple_local_stack.id in self.system.stacks)
        removed_item = self.system.remove_stack(self.simple_local_stack.id)
        self.assertTrue(removed_item == self.simple_local_stack)

    def test_remove_non_existing_stack_raises_error(self):
        with self.assertRaises(err.ElementNotFoundError):
            self.system.remove_stack(self.simple_local_stack.id)

    def test_remove_stack_available_in_existing_zone_raises_error(self):
        self.system.add_stacks(self.simple_local_stack)
        self.system.add_zones(Zone(name='test_zone', available_stacks=[self.simple_local_stack.id, ]))
        with self.assertRaises(err.ExistingReferenceSchemeError):
            self.system.remove_stack(self.simple_local_stack.id)
