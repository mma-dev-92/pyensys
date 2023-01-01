from typing import Dict, List
import numpy as np

from builder.scheme.elements.stack import Stack
from builder.scheme.elements.utils import IdElement
from builder.scheme.types import EnergyType, PlacementType
import builder.scheme.error as err


class Zone(IdElement):

    def __init__(self, name: str, available_stacks: List[Stack]):
        super().__init__(name)
        self.__available_stacks = np.nan
        self.__validate_stacks(self)
        self.__available_stacks = [x.id for x in available_stacks]

    @property
    def available_stacks(self) -> List[int]:
        return self.__available_stacks

    @available_stacks.setter
    def available_stacks(self, stacks: List[Stack]):
        self.__available_stacks = [x.id for x in stacks]

    def __validate_stacks(self, stacks: List[Stack]):
        for stack in stacks:
            if not stack.placement == PlacementType.LOCAL:
                raise err.SchemeIncompatiblePlacementTypeError(element=stack, aggregate=self)

    def __repr__(self):
        return f"Zone(id={self.id}, name={self.name}, available_stacks={self.available_stacks})"


class ZoneParameters:

    def __init__(self, zone_id, demand: Dict[EnergyType, np.ndarray], base_fractions: Dict[int, float]):
        self.__zone_id = zone_id
        self.__demand = demand
        self.__base_fractions = base_fractions

    @property
    def zone_id(self) -> int:
        return self.__zone_id

    @property
    def demand(self) -> Dict[EnergyType, np.ndarray]:
        return self.__demand

    @property
    def base_fractions(self) -> Dict[int, int]:
        return self.__base_fractions
