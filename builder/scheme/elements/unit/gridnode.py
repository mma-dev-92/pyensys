from builder.scheme.elements.unit.unit import Unit, CostParams, TimeParams, ElementParameters
from builder.scheme.elements.utils import IdElement
from builder.scheme.types import PlacementType, EnergyType


class GriNodeParameters(ElementParameters):

    def __init__(self, grid_node_id: int, cost_params: CostParams, time_params: TimeParams):
        super().__init__(grid_node_id, cost_params, time_params)


class GridNode(Unit, IdElement):

    def __init__(self, name: str, placement: PlacementType, energy_type: EnergyType, grid_id: int):
        Unit.__init__(self, placement, energy_type)
        IdElement.__init__(self, name)
        self.__grid_id = grid_id

    @property
    def grid_id(self) -> int:
        return self.__grid_id

    def __repr__(self):
        return f"GridNode(id={self.id}, name={self.name}, placement={self.placement}, energy_type={self.energy_type}" \
               f"grid_id={self.grid_id})"

