from test.test_builder.test_scheme import BaseTestEnergySystemScheme


class TestEnergySystemSchemeZones(BaseTestEnergySystemScheme):

    def setUp(self) -> None:
        super(TestEnergySystemSchemeZones, self).setUp()

    def test_add_zone(self):
        pass

    def test_add_duplicate_raises_error(self):
        pass

    def test_add_zone_with_non_existing_stack_raises_error(self):
        pass

    def test_remove_zone(self):
        pass

    def test_remove_non_existing_zone_raises_error(self):
        pass
