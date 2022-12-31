from test.test_builder.test_scheme import BaseTestEnergySystemScheme


class TestEnergySystemSchemeStacks(BaseTestEnergySystemScheme):

    def test_add_stack(self):
        pass

    def test_add_stack_with_non_existing_energy_type_raises_error(self):
        pass

    def test_add_stack_with_non_existing_base_generator_raises_error(self):
        pass

    def test_add_local_stack_with_central_base_generator_raises_error(self):
        pass

    def test_add_central_stack_with_local_base_generator_raises_error(self):
        pass

    def test_add_stack_with_non_existing_peak_generator_raises_error(self):
        pass

    def test_add_local_stack_with_central_peak_generator_raises_error(self):
        pass

    def test_add_central_stack_with_local_peak_generator_raises_error(self):
        pass

    def test_add_stack_with_non_existing_storage_raises_error(self):
        pass

    def test_add_local_stack_with_central_storage_raises_error(self):
        pass

    def test_add_central_stack_with_local_storage_raises_error(self):
        pass

    def test_remove_stack(self):
        pass

    def test_remove_non_existing_stack_raises_error(self):
        pass

    def test_remove_stack_with_base_generator_contained_in_other_existing_stack_raises_error(self):
        pass

    def test_remove_stack_with_peak_generator_contained_in_other_existing_stack_raises_error(self):
        pass

    def test_remove_stack_with_storage_contained_in_other_existing_stack_raises_error(self):
        pass
