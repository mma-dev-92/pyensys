from builder.scheme.elements.zone import Zone
from test.test_builder.test_scheme import BaseTestEnergySystemScheme
import builder.scheme.error as err


class TestZoneScheme(BaseTestEnergySystemScheme):

    def test_available_stacks_with_duplicates_raises_error(self):
        with self.assertRaises(err.DuplicateError):
            Zone(name='zone', available_stacks=[self.loc_stack, self.loc_stack])

    def test_zone_with_central_stack_raises_error(self):
        with self.assertRaises(err.SchemeIncompatiblePlacementTypeError):
            Zone(name='zone', available_stacks=[self.loc_stack, self.centr_stack])
