from builder.scheme.elements import StackTuple
from builder.scheme.elements import Generator
from builder.scheme.types import PlacementType
from test.test_builder.test_scheme import BaseTestEnergySystemScheme
import builder.scheme.error as err


class TestStackTuple(BaseTestEnergySystemScheme):

    def setUp(self) -> None:
        super(TestStackTuple, self).setUp()

    def test_only_base_generator(self):
        stack_tuple = StackTuple(base=self.node_local)
        self.assertTrue(stack_tuple.gen == self.node_local)

    def test_incorrect_base_type_raises_error(self):
        with self.assertRaises(err.InvalidAttributeTypeError):
            StackTuple(base=self.storage_central)

    def test_incorrect_peak_type_raises_error(self):
        with self.assertRaises(err.InvalidAttributeTypeError):
            StackTuple(base=self.node_local, peak=self.storage_local)

    def test_incorrect_storage_type_raises_error(self):
        gen = Generator(name='aux_gen', placement=PlacementType.LOCAL, energy_type=self.heat, carrier_id=self.coal)
        with self.assertRaises(err.InvalidAttributeTypeError):
            StackTuple(base=self.node_local, peak=self.peak_local, storage=gen)

    def test_full_stack_tuple(self):
        st = StackTuple(base=self.node_local, peak=self.peak_local, storage=self.storage_local)
        self.assertTrue(st.gen == self.node_local and st.peak == self.peak_local and st.storage == self.storage_local)

    def test_no_base_generator_raises_error(self):
        with self.assertRaises(err.AttributeNotFoundError):
            StackTuple(base=None, peak=None, storage=None)

    def test_same_base_and_peak_generator_raises_error(self):
        with self.assertRaises(err.DuplicateError):
            StackTuple(base=self.node_local, peak=self.node_local)

    def test_central_base_local_peak_raises_error(self):
        with self.assertRaises(err.SchemeIncompatiblePlacementTypeError):
            StackTuple(base=self.node_local, peak=self.peak_central)

    def test_local_base_central_storage_raises_error(self):
        with self.assertRaises(err.SchemeIncompatiblePlacementTypeError):
            StackTuple(base=self.node_local, storage=self.storage_central)

    def test_local_base_local_peak_central_storage_raises_error(self):
        with self.assertRaises(err.SchemeIncompatiblePlacementTypeError):
            StackTuple(base=self.node_local, peak=self.peak_local, storage=self.storage_central)

    def test_base_and_peak_different_energy_type_raises_error(self):
        with self.assertRaises(err.IncompatibleEnergyTypesError):
            StackTuple(base=self.node_local, peak=self.ee_peak_local)

    def test_base_and_storage_different_energy_type_raises_error(self):
        with self.assertRaises(err.IncompatibleEnergyTypesError):
            StackTuple(base=self.node_local, storage=self.ee_storage_local)

    def test_peak_and_storage_different_energy_type_raises_error(self):
        with self.assertRaises(err.IncompatibleEnergyTypesError):
            StackTuple(base=self.node_local, peak=self.peak_local, storage=self.ee_storage_local)


class TestStackScheme(BaseTestEnergySystemScheme):

    def test_setitem(self):
        pass

    def test_setitem_invalid_energy_type_raises_error(self):
        pass

    def test_getitem(self):
        pass

    def test_getitem_invalid_energy_type_raises_error(self):
        pass

    def test_set_members(self):
        pass
