from builder.systemstruct.elements.unit.unit import Unit, CostParams, TimeParams
from builder.systemstruct.elements.utils import IdManager
from builder.systemstruct.types import PlacementType, EnergyType


class GridNode(Unit, IdManager):

    def __init__(
            self,
            name: str,
            placement: PlacementType,
            energy_type: EnergyType,
            cost_params: CostParams,
            time_params: TimeParams,
            grid_id: int
    ):

        Unit.__init__(self, placement, energy_type, cost_params, time_params)
        IdManager.__init__(self, name)
        self.__grid_id = grid_id

    @property
    def grid_id(self) -> int:
        return self.__grid_id

