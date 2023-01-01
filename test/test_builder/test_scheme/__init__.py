import unittest

from builder.scheme.elements.carrier import Fuel, Profile
from builder.scheme.elements.grid import Grid
from builder.scheme.elements.stack import Stack, StackTuple
from builder.scheme.elements.unit.generator import Generator
from builder.scheme.elements.unit.gridnode import GridNode
from builder.scheme.elements.unit.storage import Storage
from builder.scheme.scheme import EnergySystemScheme
from builder.scheme.types import EnergyType, PlacementType


class BaseTestEnergySystemScheme(unittest.TestCase):

    def setUp(self) -> None:
        self.system = EnergySystemScheme(name='test_energy_system')
        self.coal, self.gas = Fuel('coal'), Fuel('gas')
        self.heat, self.ee, self.solar = EnergyType('heat'), EnergyType('electricity'), Profile('solar_energy')

        self.gen_central = Generator(
            name='gen_central', placement=PlacementType.CENTRAL, energy_type=self.heat, carrier_id=self.coal)
        self.node_central = GridNode(name='node_central', placement=PlacementType.CENTRAL, energy_type=self.heat)
        self.gen_local = Generator(
            name='gen_local', placement=PlacementType.CENTRAL, energy_type=self.heat, carrier_id=self.coal)
        self.node_local = GridNode(name='node_local', placement=PlacementType.LOCAL, energy_type=self.heat)
        self.peak_central = Generator(
            name='central_peak', placement=PlacementType.CENTRAL, energy_type=self.heat, carrier_id=self.solar)
        self.peak_local = Generator(
            name='local_peak', placement=PlacementType.LOCAL, energy_type=self.heat, carrier_id=self.gas)
        self.storage_central = Storage(name='storage_central', placement=PlacementType.CENTRAL, energy_type=self.heat)
        self.storage_local = Storage(name='storage_local', placement=PlacementType.LOCAL, energy_type=self.heat)

        self.empty_grid = Grid(
            name='empty_grid', energy_type=self.heat, stacks=[], grid_nodes=[])

        self.ee_base_local = Generator(
            name='ee_local_base', placement=PlacementType.LOCAL, energy_type=self.ee, carrier_id=self.gas)
        self.ee_peak_local = Generator(
            name='ee_local_peak', placement=PlacementType.LOCAL, energy_type=self.ee, carrier_id=self.gas)
        self.ee_storage_local = Storage(name='ee_storage_local', placement=PlacementType.LOCAL, energy_type=self.ee)

        self.loc_stack = Stack(
            name='local_stack',
            members={self.heat: StackTuple(grid_node=self.node_local, peak=self.peak_local, storage=self.storage_local)},
            placement=PlacementType.LOCAL
        )

        self.centr_stack = Stack(
            name='local_stack',
            members={self.heat: StackTuple(gen=self.gen_central, peak=self.peak_central, storage=self.storage_central)},
            placement=PlacementType.CENTRAL
        )
