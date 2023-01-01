import builder.scheme.error as er
from builder.scheme.elements.grid import Grid
from builder.scheme.elements.unit.generator import Generator
from builder.scheme.elements.unit.gridnode import GridNode
from builder.scheme.elements.unit.storage import Storage
from builder.scheme.types import PlacementType
from test.test_builder.test_scheme import BaseTestEnergySystemScheme


class TestEnergySystemSchemeEnergyTypes(BaseTestEnergySystemScheme):

    def test_add_energy_type(self):
        self.system.add_energy_types(self.heat)
        self.assertTrue(self.system.energy_types[self.heat.id] == self.heat)

    def test_add_two_different_energy_types(self):
        self.system.add_energy_types(self.heat, self.ee)
        self.assertTrue(
            self.system.energy_types[self.heat.id] == self.heat and self.system.energy_types[self.ee.id] == self.ee)

    def test_add_existing_energy_type_raises_error(self):
        self.system.add_energy_types(self.heat)
        with self.assertRaises(er.DuplicateError):
            self.system.add_energy_types(self.heat)

    def test_remove_energy_type(self):
        self.system.add_energy_types(self.heat)
        removed_element = self.system.remove_energy_type(self.heat.id)
        self.assertTrue(len(self.system.energy_types) == 0 and removed_element == self.heat)

    def test_remove_non_existing_energy_type_raises_error(self):
        self.system.add_energy_types(self.heat)
        with self.assertRaises(er.ElementNotFoundError):
            self.system.remove_energy_type(self.heat.id + 1)

    def test_remove_energy_type_with_one_generator_of_other_energy_type_do_not_raises_error(self):
        gen = Generator(name='gen', placement=PlacementType.LOCAL, energy_type=self.heat, carrier_id=self.coal)
        self.system.add_energy_types(self.heat, self.ee)
        self.system.add_carriers(self.coal)
        self.system.add_generators(gen)
        try:
            self.system.remove_energy_type(self.ee.id)
        except er.ExistingReferenceSchemeError:
            self.fail()

    def test_remove_energy_type_of_existing_generator_raises_error(self):
        gen = Generator(name='gen', placement=PlacementType.LOCAL, energy_type=self.heat, carrier_id=self.coal)
        self.system.add_energy_types(self.heat)
        self.system.add_carriers(self.coal)
        self.system.add_generators(gen)
        with self.assertRaises(er.ExistingReferenceSchemeError):
            self.system.remove_energy_type(self.heat.id)

    def test_remove_energy_type_with_one_grid_node_of_other_energy_type_do_not_raises_error(self):
        grid = Grid(name='grid', energy_type=self.heat, stacks=[])
        grid_node = GridNode('grid_node', placement=PlacementType.LOCAL, energy_type=self.heat, grid_id=grid.id)
        self.system.add_energy_types(self.heat, self.ee)
        self.system.add_grid_systems(grid)
        self.system.add_grid_nodes(grid_node)
        try:
            self.system.remove_energy_type(self.ee.id)
        except er.ExistingReferenceSchemeError:
            self.fail()

    def test_remove_energy_type_of_existing_grid_node_raises_error(self):
        grid = Grid(name='grid', energy_type=self.heat, stacks=[])
        grid_node = GridNode('grid_node', placement=PlacementType.LOCAL, energy_type=self.heat, grid_id=grid.id)
        self.system.add_energy_types(self.heat)
        self.system.add_grid_systems(grid)
        self.system.add_grid_nodes(grid_node)
        with self.assertRaises(er.ExistingReferenceSchemeError):
            self.system.remove_energy_type(self.heat.id)

    def test_remove_energy_type_with_one_grid_of_other_energy_type_do_not_raises_error(self):
        grid = Grid(name='grid', energy_type=self.heat, stacks=[])
        self.system.add_energy_types(self.heat, self.ee)
        self.system.add_grid_systems(grid)
        try:
            self.system.remove_energy_type(self.ee.id)
        except er.ExistingReferenceSchemeError:
            self.fail()

    def test_remove_energy_type_of_existing_grid_raises_error(self):
        grid = Grid(name='grid', energy_type=self.heat, stacks=[])
        self.system.add_energy_types(self.heat)
        self.system.add_grid_systems(grid)
        with self.assertRaises(er.ExistingReferenceSchemeError):
            self.system.remove_energy_type(self.heat.id)

    def test_remove_energy_type_with_one_storage_of_other_energy_type_do_not_raises_error(self):
        storage = Storage(name='storage', placement=PlacementType.CENTRAL, energy_type=self.heat)
        self.system.add_energy_types(self.heat, self.ee)
        self.system.add_storages(storage)
        try:
            self.system.remove_energy_type(self.ee.id)
        except er.ExistingReferenceSchemeError:
            self.fail()

    def test_remove_energy_type_of_existing_storage_raises_error(self):
        storage = Storage(name='storage', placement=PlacementType.CENTRAL, energy_type=self.heat)
        self.system.add_energy_types(self.heat)
        self.system.add_storages(storage)
        with self.assertRaises(er.ExistingReferenceSchemeError):
            self.system.remove_energy_type(self.heat.id)
