from builder.scheme.elements.stack import Stack, StackTuple
from builder.scheme.elements.unit.generator import Generator
from builder.scheme.elements.unit.storage import Storage
from builder.scheme.types import PlacementType
from test.test_builder.test_scheme import BaseTestEnergySystemScheme
import builder.scheme.error as err


class TestEnergySystemSchemeStorages(BaseTestEnergySystemScheme):

    def setUp(self) -> None:
        super(TestEnergySystemSchemeStorages, self).setUp()
        self.local_storage = Storage(name='local_storage', placement=PlacementType.LOCAL, energy_type=self.heat)
        self.central_storage = Storage(name='local_storage', placement=PlacementType.CENTRAL, energy_type=self.ee)

        self.system.add_energy_types(self.heat, self.ee)

    def test_add_storage(self):
        self.system.add_storages(self.local_storage, self.central_storage)
        self.assertTrue(
            self.local_storage.id in self.system.storages and self.central_storage.id in self.system.storages)

    def test_add_storage_with_non_existing_energy_type_raises_error(self):
        self.system.remove_energy_type(self.ee.id)
        self.assertTrue(self.ee.id not in self.system.energy_types)
        with self.assertRaises(err.SchemeNonExistingReferenceError):
            self.system.add_storages(self.central_storage)

    def test_add_duplicate_raises_error(self):
        self.system.add_storages(self.local_storage)
        self.assertTrue(self.local_storage.id in self.system.storages)
        with self.assertRaises(err.DuplicateError):
            self.system.add_storages(self.local_storage)

    def test_remove_storage(self):
        self.system.add_storages(self.local_storage, self.central_storage)
        removed_element = self.system.remove_storage(self.local_storage.id)
        self.assertTrue(removed_element == self.local_storage and self.local_storage.id not in self.system.storages)

    def test_remove_non_existing_storage_raises_error(self):
        self.system.add_storages(self.central_storage)
        self.assertTrue(self.central_storage.id in self.system.storages)
        with self.assertRaises(err.ElementNotFoundError):
            self.system.remove_storage(self.local_storage.id)

    def test_remove_storage_contained_in_existing_stack_raises_error(self):
        self.system.remove_energy_type(self.ee)
        self.system.add_carriers(self.coal)
        base = Generator(name='base', placement=PlacementType.LOCAL, energy_type=self.heat, carrier_id=self.coal)
        self.system.add_generators(base)
        self.system.add_storages(self.local_storage)
        self.system.add_stacks(Stack(
            name='test_stack',
            members={self.heat: StackTuple(base=base.id, peak=None, storage=self.local_storage.id)},
            placement=PlacementType.LOCAL
        ))
        with self.assertRaises(err.ExistingReferenceSchemeError):
            self.system.remove_storage(self.local_storage.id)
