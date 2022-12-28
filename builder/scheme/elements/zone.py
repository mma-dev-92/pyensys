from typing import Dict, List
import numpy as np

from builder.scheme.elements.utils import IdManager
from builder.scheme.types import EnergyType


class Zone(IdManager):

    def __init__(self, name: str, available_stacks: List[int]):
        super().__init__(name)
        self.__available_stacks = available_stacks

    @property
    def available_stacks(self) -> List[int]:
        return self.__available_stacks

    @available_stacks.setter
    def available_stacks(self, stack_ids: List[int]):
        self.__available_stacks = stack_ids

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
