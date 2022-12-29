import builder.scheme.error as er
from builder.scheme.elements.grid import Grid
from builder.scheme.elements.unit.generator import Generator
from builder.scheme.elements.unit.gridnode import GridNode
from builder.scheme.elements.unit.storage import Storage
from builder.scheme.types import PlacementType
from test.test_builder.test_scheme import BaseTestEnergySystemScheme


class TestEnergySystemSchemeEnergyTypes(BaseTestEnergySystemScheme):

    def test_add_energy_type(self):
        self.system.add_energy_type(self.heat)
        self.assertTrue(self.system.energy_types[self.heat.id] == self.heat)

    def test_add_two_different_energy_types(self):
        self.system.add_energy_type(self.heat)
        self.system.add_energy_type(self.ee)
        self.assertTrue(
            self.system.energy_types[self.heat.id] == self.heat and self.system.energy_types[self.ee.id] == self.ee)

    def test_add_existing_energy_type_raises_error(self):
        self.system.add_energy_type(self.heat)
        with self.assertRaises(er.SchemeDuplicateError):
            self.system.add_energy_type(self.heat)

    def test_remove_energy_type(self):
        self.system.add_energy_type(self.heat)
        removed_element = self.system.remove_energy_type(self.heat.id)
        self.assertTrue(len(self.system.energy_types) == 0 and removed_element == self.heat)

    def test_remove_non_existing_energy_type_raises_error(self):
        self.system.add_energy_type(self.heat)
        with self.assertRaises(er.SchemeElementNotFoundError):
            self.system.remove_energy_type(self.heat.id + 1)

    def test_remove_energy_type_with_one_generator_of_other_energy_type_do_not_raise_error(self):
        gen = Generator(name='gen', placement=PlacementType.LOCAL, energy_type=self.heat, carrier_id=self.coal.id)
        self.system.add_energy_type(self.heat)
        self.system.add_energy_type(self.ee)
        self.system.add_carrier(self.coal)
        self.system.add_generator(gen)
        try:
            self.system.remove_energy_type(self.ee.id)
        except er.SchemeExistingReferenceError:
            self.fail()

    def test_remove_energy_type_of_existing_generator_raises_error(self):
        gen = Generator(name='gen', placement=PlacementType.LOCAL, energy_type=self.heat, carrier_id=self.coal.id)
        self.system.add_energy_type(self.heat)
        self.system.add_carrier(self.coal)
        self.system.add_generator(gen)
        with self.assertRaises(er.SchemeExistingReferenceError):
            self.system.remove_energy_type(self.heat.id)

    def test_remove_energy_type_with_one_grid_node_of_other_energy_type_do_not_raise_error(self):
        grid = Grid(name='grid', energy_type=self.heat, stacks=[])
        grid_node = GridNode('grid_node', placement=PlacementType.LOCAL, energy_type=self.heat, grid_id=grid.id)
        self.system.add_energy_type(self.heat)
        self.system.add_energy_type(self.ee)
        self.system.add_grid_system(grid)
        self.system.add_grid_node(grid_node)
        try:
            self.system.remove_energy_type(self.ee.id)
        except er.SchemeExistingReferenceError:
            self.fail()

    def test_remove_energy_type_of_existing_grid_node_raises_error(self):
        grid = Grid(name='grid', energy_type=self.heat, stacks=[])
        grid_node = GridNode('grid_node', placement=PlacementType.LOCAL, energy_type=self.heat, grid_id=grid.id)
        self.system.add_energy_type(self.heat)
        self.system.add_grid_system(grid)
        self.system.add_grid_node(grid_node)
        with self.assertRaises(er.SchemeExistingReferenceError):
            self.system.remove_energy_type(self.heat.id)

    def test_remove_energy_type_with_one_grid_of_other_energy_type_do_not_raise_error(self):
        grid = Grid(name='grid', energy_type=self.heat, stacks=[])
        self.system.add_energy_type(self.heat)
        self.system.add_energy_type(self.ee)
        self.system.add_grid_system(grid)
        try:
            self.system.remove_energy_type(self.ee.id)
        except er.SchemeExistingReferenceError:
            self.fail()

    def test_remove_energy_type_of_existing_grid_raises_error(self):
        grid = Grid(name='grid', energy_type=self.heat, stacks=[])
        self.system.add_energy_type(self.heat)
        self.system.add_grid_system(grid)
        with self.assertRaises(er.SchemeExistingReferenceError):
            self.system.remove_energy_type(self.heat.id)

    def test_remove_energy_type_with_one_storage_of_other_energy_type_do_not_raise_error(self):
        storage = Storage(name='storage', placement=PlacementType.CENTRAL, energy_type=self.heat)
        self.system.add_energy_type(self.heat)
        self.system.add_energy_type(self.ee)
        self.system.add_storage(storage)
        try:
            self.system.remove_energy_type(self.ee.id)
        except er.SchemeExistingReferenceError:
            self.fail()

    def test_remove_energy_type_of_existing_storage_raises_error(self):
        storage = Storage(name='storage', placement=PlacementType.CENTRAL, energy_type=self.heat)
        self.system.add_energy_type(self.heat)
        self.system.add_storage(storage)
        with self.assertRaises(er.SchemeExistingReferenceError):
            self.system.remove_energy_type(self.heat.id)
