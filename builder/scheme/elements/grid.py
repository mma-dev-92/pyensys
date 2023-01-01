from typing import List, Dict
import numpy as np

from builder.scheme.elements import GridNode
from builder.scheme.elements.stack import Stack
from builder.scheme.elements.unit.unit import CostParams, TimeParams, ElementParameters
from builder.scheme.elements.utils import IdElement
from builder.scheme.types import EnergyType, PlacementType
import builder.scheme.error as err


class Grid(IdElement):

    def __init__(self, name: str, energy_type: EnergyType, stacks: List[Stack], grid_nodes: List[GridNode]):
        super().__init__(name)
        self.__energy_type = energy_type
        self.__stacks = np.nan
        self.__validate_stacks(stacks)
        self.__stacks = self.__store_in_dict(stacks)
        self.__grid_nodes = self.__store_in_dict(grid_nodes)

    @property
    def energy_type(self) -> EnergyType:
        return self.__energy_type

    @property
    def stacks(self) -> Dict[int, Stack]:
        return self.__stacks

    @property
    def grid_nodes(self) -> Dict[int, GridNode]:
        return self.__grid_nodes

    def add_grid_node(self, grid_node: GridNode):
        pass

    def add_stack(self):
        pass

    def remove_grid_node(self, grid_node_id: int):
        pass

    def remove_stack(self, stack_id: int):
        pass

    def __validate_stacks(self, stacks: List[Stack]):
        for stack in stacks:
            if not stack.placement == PlacementType.CENTRAL:
                raise err.SchemeIncompatiblePlacementTypeError(element=stack, aggregate=self)
            if self.energy_type not in stack.members:
                raise err.IncompatibleEnergyTypesError(element=stack, reference_element=self)
            if stacks.count(stack) > 1:
                raise err.DuplicateError(element=stack, aggregate=self)

    @staticmethod
    def __store_in_dict(ll: list):
        return {x.id: x for x in ll}

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
