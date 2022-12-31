from builder.scheme.elements.grid import Grid
from builder.scheme.elements.stack import Stack, StackTuple
from builder.scheme.elements.unit.generator import Generator
from builder.scheme.elements.unit.gridnode import GridNode
from builder.scheme.types import PlacementType
from test.test_builder.test_scheme import BaseTestEnergySystemScheme
import builder.scheme.error as err


class TestEnergySystemSchemeGrids(BaseTestEnergySystemScheme):

    def setUp(self) -> None:
        self.mpc = Generator(name='mpc', placement=PlacementType.LOCAL, energy_type=self.heat, carrier_id=self.coal.id)
        self.chp = Generator(name='chp', placement=PlacementType.LOCAL, energy_type=self.heat, carrier_id=self.gas.id)

        self.mpc_stack = Stack(
            name='mpc_stack', members={self.heat: StackTuple(base=self.mpc.id)}, placement=PlacementType.CENTRAL)
        self.chp_stack = Stack(
            name='chp_stack', members={self.heat: StackTuple(base=self.chp.id)}, placement=PlacementType.CENTRAL
        )
        self.grid = Grid(name='heating_sector', energy_type=self.heat, stacks=[self.mpc_stack.id, self.chp_stack.id])
        self.empty_grid = Grid(name='empty_grid', energy_type=self.heat, stacks=[])

        self.system.add_energy_types(self.heat)

    def test_add_grid(self):
        self.system.add_generators(self.mpc, self.chp)
        self.system.add_stacks(self.mpc_stack, self.chp_stack)
        self.system.add_grid_systems(self.grid)
        self.assertTrue(self.system.grid_systems[self.grid.id] == self.grid)

    def test_add_grid_with_non_existing_stack_raises_error(self):
        self.system.add_generators(self.mpc)
        self.system.add_stacks(self.mpc_stack)
        with self.assertRaises(err.SchemeNonExistingReferenceError):
            self.system.add_grid_systems(self.grid)

    def test_add_grid_with_non_existing_energy_type_raises_error(self):
        self.system.remove_energy_type(self.heat.id)
        with self.assertRaises(err.SchemeNonExistingReferenceError):
            self.system.add_grid_systems(self.empty_grid)

    def test_add_two_grids_with_same_central_stack_raises_error(self):
        one_stack_grid = Grid(name='one_stack_grid', energy_type=self.heat, stacks=[self.mpc_stack.id, ])
        self.system.add_generators(self.mpc, self.chp)
        self.system.add_stacks(self.mpc_stack, self.chp_stack)
        self.system.add_grid_systems(self.grid.id)
        with self.assertRaises(err.SchemeOneToManyViolationError):
            self.system.add_grid_systems(one_stack_grid.id)

    def test_add_grid_with_many_stacks_and_one_non_existing_raises_error(self):
        self.system.add_generators(self.mpc)
        self.system.add_stacks(self.mpc_stack)
        with self.assertRaises(err.SchemeNonExistingReferenceError):
            self.system.add_grid_systems(self.grid)

    def test_remove_grid(self):
        self.system.add_grid_systems(self.empty_grid)
        removed_grid = self.system.remove_grid_system(self.empty_grid.id)
        self.assertTrue(removed_grid == self.empty_grid and len(self.system.grid_systems) == 0)

    def test_remove_non_existing_grid(self):
        with self.assertRaises(err.SchemeElementNotFoundError):
            self.system.remove_grid_system(self.grid.id)

    def test_remove_grid_with_one_existing_grid_node_reference_raises_error(self):
        grid_node = GridNode(
            name='grid_node', placement=PlacementType.LOCAL, energy_type=self.heat, grid_id=self.empty_grid.id)
        self.system.add_grid_systems(self.empty_grid)
        self.system.add_grid_nodes(grid_node)
        with self.assertRaises(err.SchemeExistingReferenceError):
            self.system.remove_grid_node(self.empty_grid.id)
