from builder.systemstruct.elements.unit.params import CostParams, TimeParams
from builder.systemstruct.elements.unit.unit import Unit
from builder.systemstruct.types import PlacementType, EnergyType


class GridNode(Unit):

    def __init__(
            self,
            name: str,
            placement: PlacementType,
            energy_type: EnergyType,
            cost_params: CostParams,
            time_params: TimeParams,
            grid_id: int
    ):

        super().__init__(name, placement, energy_type, cost_params, time_params)
        self.__grid_id = grid_id

    @property
    def grid_id(self) -> int:
        return self.__grid_id

