from typing import Dict

from builder.scheme.elements import Carrier
from builder.scheme.elements import Stack
from builder.scheme.elements import Grid
from builder.scheme.elements import Generator
from builder.scheme.elements import GridNode
from builder.scheme.elements import Storage
from builder.scheme.elements import Zone
from builder.scheme.types import EnergyType, CarrierType


# TODO: implement this class + validation for adding and removing elements
class EnergySystemScheme:

    def __init__(self, name: str):
        self.__name = name

        self.__energy_types = dict()
        self.__carriers = dict()

        self.__generators = dict()
        self.__storages = dict()
        self.__grid_nodes = dict()

        self.__grids = dict()
        self.__stacks = dict()

        self.__zones = dict()

    def add_energy_types(self, *energy_types: EnergyType) -> None:
        pass

    def remove_energy_type(self, energy_type_id: int) -> EnergyType:
        pass

    def add_carriers(self, *carriers: Carrier) -> None:
        pass

    def remove_carrier(self, carrier_id: int) -> Carrier:
        pass

    def add_generators(self, *generators: Generator) -> None:
        pass

    def remove_generator(self, generator_id: int) -> Generator:
        pass

    def add_storages(self, *storages: Storage) -> None:
        pass

    def remove_storage(self, storage_id: int) -> Storage:
        pass

    def add_grid_nodes(self, *grid_nodes: GridNode) -> None:
        pass

    def remove_grid_node(self, grid_node_id: int) -> GridNode:
        pass

    def add_stacks(self, *stacks: Stack) -> None:
        pass

    def remove_stack(self, stack_id: int) -> Stack:
        pass

    def add_grid_systems(self, *grid_systems: Grid) -> None:
        pass

    def remove_grid_system(self, grid_system_id: int) -> Grid:
        pass

    def add_zones(self, *zones: Zone):
        pass

    def remove_zone(self, zone_id: int) -> Zone:
        pass

    @property
    def name(self) -> str:
        return self.__name

    @property
    def zones(self) -> Dict[int, Zone]:
        return self.__zones

    @property
    def carriers(self) -> Dict[CarrierType, Dict[int, Carrier]]:
        return self.__carriers

    @property
    def energy_types(self) -> Dict[int, EnergyType]:
        return self.__energy_types

    @property
    def grid_systems(self) -> Dict[int, Grid]:
        return self.__grids

    @property
    def stacks(self) -> Dict[int, Stack]:
        return self.__stacks

    @property
    def generators(self) -> Dict[int, Generator]:
        return self.__generators

    @property
    def storages(self) -> Dict[int, Storage]:
        return self.__storages

    @property
    def grid_nodes(self) -> Dict[int, GridNode]:
        return self.__grid_nodes
