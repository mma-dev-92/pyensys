from test.test_builder.test_scheme import BaseTestEnergySystemScheme


class TestEnergySystemSchemeGridNodes(BaseTestEnergySystemScheme):

    def test_add_grid_node(self):
        pass

    def test_add_two_grid_nodes_to_the_same_grid(self):
        pass

    def test_add_same_grid_node_twice_raise_error(self):
        pass

    def test_add_grid_node_with_non_existing_grid_raise_error(self):
        pass

    def test_remove_grid_node(self):
        pass

    def test_remove_grid_node_connected_to_existing_grid_raise_error(self):
        pass

    def test_remove_grid_node_contained_in_existing_stack_raise_error(self):
        pass

    def test_remove_grid_node_contained_in_non_existing_stack(self):
        pass
