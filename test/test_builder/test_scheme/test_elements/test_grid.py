from builder.scheme.elements.grid import Grid
from test.test_builder.test_scheme import BaseTestEnergySystemScheme
import builder.scheme.error as err


class TestGridScheme(BaseTestEnergySystemScheme):

    def test_simple_creation(self):
        grid = Grid(name='test_grid', energy_type=self.heat, stacks=[self.centr_stack, ], grid_nodes=[])
        self.assertTrue(grid.name == 'test_grid')
        self.assertTrue(grid.energy_type == self.heat and not grid.energy_type == self.ee)
        self.assertTrue(grid.stacks == [self.centr_stack.id, ])

    def test_duplicate_grid_stacks_raises_error(self):
        with self.assertRaises(err.DuplicateError):
            Grid(name='test_grid', energy_type=self.heat, stacks=[self.centr_stack, self.centr_stack], grid_nodes=[])

    def test_grid_with_local_stack_raises_error(self):
        with self.assertRaises(err.SchemeIncompatiblePlacementTypeError):
            Grid(name='test_grid', energy_type=self.heat, stacks=[self.loc_stack], grid_nodes=[])

    def test_stack_incompatible_energy_type_error_with_grid(self):
        with self.assertRaises(err.IncompatibleEnergyTypesError):
            Grid(name='test_grid', energy_type=self.ee, stacks=[self.centr_stack], grid_nodes=[])

    def test_grid_node_incompatible_energy_type_error_with_grid(self):
        pass

    def test_stacks_setter_clear(self):
        grid = Grid(name='test_grid', energy_type=self.heat, stacks=[self.centr_stack, ], grid_nodes=[])
        grid.stacks = {}
        self.assertTrue(grid.stacks == {})

    def test_stacks_setter(self):
        grid = Grid(name='test_grid', energy_type=self.heat, stacks=[], grid_nodes=[])
        grid.stacks = [self.centr_stack, ]
        self.assertTrue(grid.stacks == [self.centr_stack.id, ])

    def test_grid_nodes_setter(self):
        pass

    def test_stacks_setter_duplicate_raises_error(self):
        grid = Grid(name='test_grid', energy_type=self.heat, stacks=[self.centr_stack, ], grid_nodes=[])
        with self.assertRaises(err.DuplicateError):
            grid.stacks = [self.centr_stack, self.centr_stack]

    def test_stacks_setter_with_local_stack_raises_error(self):
        grid = Grid(name='test_grid', energy_type=self.heat, stacks=[], grid_nodes=[])
        with self.assertRaises(err.SchemeIncompatiblePlacementTypeError):
            grid.stacks = [self.centr_stack, self.loc_stack]

    def test_stacks_setter_incompatible_energy_type_error_with_grid(self):
        grid = Grid(name='test_grid', energy_type=self.ee, stacks=[], grid_nodes=[])
        with self.assertRaises(err.IncompatibleEnergyTypesError):
            grid.stacks = [self.centr_stack, ]
