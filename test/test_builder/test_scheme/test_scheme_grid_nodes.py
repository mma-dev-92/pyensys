from builder.scheme.elements.grid import Grid
from builder.scheme.elements.stack import Stack, StackTuple
from builder.scheme.elements.unit.gridnode import GridNode
from builder.scheme.types import PlacementType
from test.test_builder.test_scheme import BaseTestEnergySystemScheme
import builder.scheme.error as err


class TestEnergySystemSchemeGridNodes(BaseTestEnergySystemScheme):

    def setUp(self) -> None:
        super(TestEnergySystemSchemeGridNodes, self).setUp()
        self.grid = Grid(name='empty_grid', energy_type=self.heat, stacks=[])
        self.grid_node_1 = GridNode(
            name='grid_node_1', energy_type=self.heat, grid_id=self.grid.id, placement=PlacementType.LOCAL)
        self.grid_node_2 = GridNode(
            name='grid_node_2', energy_type=self.heat, grid_id=self.grid.id, placement=PlacementType.LOCAL)
        self.stack = Stack(
            name='stack', members={self.heat: StackTuple(base=self.grid_node_1.id)}, placement=PlacementType.LOCAL)

        self.system.add_energy_types(self.heat)

    def test_add_grid_node(self):
        self.system.add_grid_systems(self.grid)
        self.system.add_grid_nodes(self.grid_node_1)
        self.assertTrue(self.system.grid_nodes[self.grid_node_1.id] == self.grid_node_1)

    def test_add_grid_node_with_non_existing_energy_type(self):
        with self.assertRaises(err.ElementNotFoundError):
            self.system.add_grid_nodes(
                GridNode(name='tmp', energy_type=self.ee, grid_id=self.grid.id, placement=PlacementType.LOCAL)
            )

    def test_add_two_grid_nodes_to_the_same_grid(self):
        self.system.add_grid_systems(self.grid)
        self.system.add_grid_nodes(self.grid_node_1, self.grid_node_2)
        self.assertTrue(self.system.grid_nodes[self.grid_node_1.id] == self.grid_node_1)
        self.assertTrue(self.system.grid_nodes[self.grid_node_2.id] == self.grid_node_2)

    def test_add_same_grid_node_twice_raises_error(self):
        self.system.add_grid_systems(self.grid)
        self.system.add_grid_nodes(self.grid_node_1)
        with self.assertRaises(err.DuplicateError):
            self.system.add_grid_nodes(self.grid_node_1)

    def test_add_grid_node_with_non_existing_grid_raises_error(self):
        with self.assertRaises(err.SchemeNonExistingReferenceError):
            self.system.add_grid_nodes(self.grid_node_1)

    def test_remove_grid_node(self):
        self.system.add_grid_systems(self.grid)
        self.system.add_grid_nodes(self.grid_node_1)
        removed_node = self.system.remove_grid_node(self.grid_node_1.id)
        self.assertTrue(removed_node == self.grid_node_1 and len(self.system.grid_nodes) == 0)

    def test_remove_grid_node_contained_in_non_existing_stack(self):
        self.system.add_grid_nodes(self.grid_node_1)
        self.system.add_stacks(self.stack)
        self.system.remove_stack(self.stack.id)
        try:
            self.system.remove_grid_node(self.grid_node_1.id)
        except err.ExistingReferenceSchemeError:
            self.fail()

    def test_remove_non_existing_grid_node_raises_error(self):
        with self.assertRaises(err.ElementNotFoundError):
            self.system.remove_grid_node(self.grid_node_1.id)

    def test_remove_grid_node_contained_in_existing_stack_raises_error(self):
        self.system.add_grid_nodes(self.grid_node_1)
        self.system.add_stacks(self.stack)
        with self.assertRaises(err.ExistingReferenceSchemeError):
            self.system.remove_grid_node(self.grid_node_1.id)
