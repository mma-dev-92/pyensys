import builder.scheme.error as er
from builder.scheme.elements.carrier import Fuel
from builder.scheme.elements.grid import Grid
from builder.scheme.elements.unit.generator import Generator
from builder.scheme.elements.unit.gridnode import GridNode
from builder.scheme.elements.unit.storage import Storage
from builder.scheme.types import EnergyType, PlacementType
from test.test_builder.test_scheme import BaseTestEnergySystemScheme


class TestEnergySystemSchemeEnergyTypes(BaseTestEnergySystemScheme):

    def test_add_energy_type(self):
        et = EnergyType(name='heat')
        self.system.add_energy_type(et)
        self.assertTrue(self.system.energy_types[et.id] == et)

    def test_add_two_different_energy_types(self):
        heat, cooling = EnergyType('heat'), EnergyType('cooling')
        self.system.add_energy_type(heat)
        self.system.add_energy_type(cooling)
        self.assertTrue(self.system.energy_types[heat.id] == heat and self.system.energy_types[cooling.id] == cooling)

    def test_add_existing_energy_type_raises_error(self):
        et = EnergyType(name='heat')
        self.system.add_energy_type(et)
        with self.assertRaises(er.SchemeDuplicateError):
            self.system.add_energy_type(et)

    def test_remove_energy_type(self):
        et = EnergyType(name='heat')
        self.system.add_energy_type(et)
        removed_element = self.system.remove_energy_type(et.id)
        self.assertTrue(len(self.system.energy_types) == 0 and removed_element == et)

    def test_remove_non_existing_energy_type_raises_error(self):
        et = EnergyType(name='heat')
        self.system.add_energy_type(et)
        with self.assertRaises(er.SchemeElementNotFoundError):
            self.system.remove_energy_type(et.id + 1)

    def test_remove_energy_type_with_one_generator_of_other_energy_type_do_not_raise_error(self):
        heat, ee = EnergyType('heat'), EnergyType('ee')
        coal = Fuel('coal')
        gen = Generator(name='gen', placement=PlacementType.LOCAL, energy_type=heat, carrier_id=coal.id)
        self.system.add_energy_type(heat)
        self.system.add_energy_type(ee)
        self.system.add_carrier(coal)
        self.system.add_generator(gen)
        try:
            self.system.remove_energy_type(ee.id)
        except er.SchemeExistingReferenceError:
            self.fail()

    def test_remove_energy_type_of_existing_generator_raises_error(self):
        heat = EnergyType('heat')
        coal = Fuel('coal')
        gen = Generator(name='gen', placement=PlacementType.LOCAL, energy_type=heat, carrier_id=coal.id)
        self.system.add_energy_type(heat)
        self.system.add_carrier(coal)
        self.system.add_generator(gen)
        with self.assertRaises(er.SchemeExistingReferenceError):
            self.system.remove_energy_type(heat.id)

    def test_remove_energy_type_with_one_grid_node_of_other_energy_type_do_not_raise_error(self):
        heat, ee = EnergyType('heat'), EnergyType('ee')
        grid = Grid(name='grid', energy_type=heat, stacks=[])
        grid_node = GridNode('grid_node', placement=PlacementType.LOCAL, energy_type=heat, grid_id=grid.id)
        self.system.add_energy_type(heat)
        self.system.add_energy_type(ee)
        self.system.add_grid_system(grid)
        self.system.add_grid_node(grid_node)
        try:
            self.system.remove_energy_type(ee.id)
        except er.SchemeExistingReferenceError:
            self.fail()

    def test_remove_energy_type_of_existing_grid_node_raises_error(self):
        heat = EnergyType('heat')
        grid = Grid(name='grid', energy_type=heat, stacks=[])
        grid_node = GridNode('grid_node', placement=PlacementType.LOCAL, energy_type=heat, grid_id=grid.id)
        self.system.add_energy_type(heat)
        self.system.add_grid_system(grid)
        self.system.add_grid_node(grid_node)
        with self.assertRaises(er.SchemeExistingReferenceError):
            self.system.remove_energy_type(heat.id)

    def test_remove_energy_type_with_one_grid_of_other_energy_type_do_not_raise_error(self):
        heat, ee = EnergyType('heat'), EnergyType('ee')
        grid = Grid(name='grid', energy_type=heat, stacks=[])
        self.system.add_energy_type(heat)
        self.system.add_energy_type(ee)
        self.system.add_grid_system(grid)
        try:
            self.system.remove_energy_type(ee.id)
        except er.SchemeExistingReferenceError:
            self.fail()

    def test_remove_energy_type_of_existing_grid_raises_error(self):
        heat = EnergyType('heat')
        grid = Grid(name='grid', energy_type=heat, stacks=[])
        self.system.add_energy_type(heat)
        self.system.add_grid_system(grid)
        with self.assertRaises(er.SchemeExistingReferenceError):
            self.system.remove_energy_type(heat.id)

    def test_remove_energy_type_with_one_storage_of_other_energy_type_do_not_raise_error(self):
        heat, ee = EnergyType('heat'), EnergyType('ee')
        storage = Storage(name='storage', placement=PlacementType.CENTRAL, energy_type=heat)
        self.system.add_energy_type(heat)
        self.system.add_energy_type(ee)
        self.system.add_storage(storage)
        try:
            self.system.remove_energy_type(ee.id)
        except er.SchemeExistingReferenceError:
            self.fail()

    def test_remove_energy_type_of_existing_storage_raises_error(self):
        heat = EnergyType('heat')
        storage = Storage(name='storage', placement=PlacementType.CENTRAL, energy_type=heat)
        self.system.add_energy_type(heat)
        self.system.add_storage(storage)
        with self.assertRaises(er.SchemeExistingReferenceError):
            self.system.remove_energy_type(heat.id)
