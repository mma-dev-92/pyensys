import unittest

from builder.systemstruct.system import EnergySystem


class BaseTestEnergySystem(unittest.TestCase):

    def setUp(self) -> None:
        self.n_hours = 8760
        self.n_years = 5
        self.system = EnergySystem(name='test_energy_system', time_horizon=self.n_years, hours_per_year=self.n_hours)


class TestEnergySystemEnergyTypes(BaseTestEnergySystem):

    def test_add_energy_type(self):
        pass

    def test_add_two_different_energy_types(self):
        pass

    def test_add_existing_energy_type_raises_error(self):
        pass

    def test_remove_energy_type(self):
        pass

    def test_remove_non_existing_energy_type_raises_error(self):
        pass

    def test_remove_energy_type_with_one_carrier_fuel_of_other_energy_type_do_not_raise_error(self):
        pass

    def test_remove_energy_type_of_existing_carrier_fuel_raises_error(self):
        pass

    def test_remove_energy_type_with_one_carrier_profile_of_other_energy_type_do_not_raise_error(self):
        pass

    def test_remove_energy_type_of_existing_carrier_profile_raises_error(self):
        pass

    def test_remove_energy_type_with_one_generator_of_other_energy_type_do_not_raise_error(self):
        pass

    def test_remove_energy_type_of_existing_generator_raises_error(self):
        pass

    def test_remove_energy_type_with_one_grid_node_of_other_energy_type_do_not_raise_error(self):
        pass

    def test_remove_energy_type_of_existing_grid_node_raises_error(self):
        pass

    def test_remove_energy_type_with_one_grid_of_other_energy_type_do_not_raise_error(self):
        pass

    def test_remove_energy_type_of_existing_grid_raises_error(self):
        pass

    def test_remove_energy_type_with_one_stack_of_other_energy_type_do_not_raise_error(self):
        pass

    def test_remove_energy_type_of_existing_stack_raises_error(self):
        pass

    def test_remove_energy_type_with_one_storage_of_other_energy_type_do_not_raise_error(self):
        pass

    def test_remove_energy_type_of_existing_storage_raises_error(self):
        pass


class TestEnergySystemCarriers(BaseTestEnergySystem):

    def test_add_fuel(self):
        pass

    def test_add_profile(self):
        pass

    def test_add_one_fuel_one_profile(self):
        pass

    def test_add_two_fuels(self):
        pass

    def test_remove_fuel(self):
        pass

    def test_remove_non_existing_fuel(self):
        pass

    def test_remove_fuel_of_existing_generator_raises_error(self):
        pass

    def test_remove_fuel_with_one_generator_of_other_fuel_do_not_raise_error(self):
        pass
