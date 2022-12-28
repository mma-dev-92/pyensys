from typing import List

from builder.scheme.elements.stack import Stack
from builder.scheme.elements.unit.unit import CostParams, TimeParams, ElementParameters
from builder.scheme.elements.utils import IdManager
from builder.scheme.types import EnergyType
import builder.scheme.error as err


class Grid(IdManager):

    def __init__(self, name: str, energy_type: EnergyType, stacks: List[int]):
        IdManager.__init__(self, name)
        self.__energy_type = energy_type
        self.__stacks = stacks

    @property
    def energy_type(self) -> EnergyType:
        return self.__energy_type

    @property
    def stacks(self) -> List[int]:
        return self.__stacks

    @stacks.setter
    def stacks(self, stacks_id: List[int]):
        self.__stacks = stacks_id

    def __repr__(self):
        return f"Grid(id={self.id}, name={self.name}, energy_type={self.energy_type}, stacks={self.stacks})"


class GridParameters(ElementParameters):

    def __init__(
            self, grid_id: int, base_capacity: float, loss: float, cost_params: CostParams, time_params: TimeParams):
        super().__init__(grid_id, cost_params, time_params)
        self.__base_capacity = base_capacity
        self.__loss = loss

    @property
    def base_capacity(self) -> float:
        return self.__base_capacity

    @property
    def loss(self) -> float:
        return self.__loss
