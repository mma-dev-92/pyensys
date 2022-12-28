from test.test_builder.test_scheme import BaseTestEnergySystemScheme


class TestEnergySystemSchemeCarriers(BaseTestEnergySystemScheme):

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
