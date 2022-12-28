from typing import Dict
import numpy as np

from builder.scheme.elements.unit.unit import Unit, CostParams, TimeParams, ElementParameters
from builder.scheme.elements.utils import IdManager
from builder.scheme.types import PlacementType, EnergyType


# TODO: energy losses
class StorageParameters(ElementParameters):

    def __init__(
            self,
            storage_id: int,
            cost_params: CostParams,
            time_params: TimeParams,
            demand_per_unit_load: Dict[EnergyType, np.ndarray],
            demand_per_unit_gen: Dict[EnergyType, np.ndarray]
    ):
        super().__init__(storage_id, cost_params, time_params)
        self.__demand_per_unit_load = demand_per_unit_load
        self.__demand_per_unit_gen = demand_per_unit_gen

    @property
    def demand_per_unit_load(self) -> Dict[EnergyType, np.ndarray]:
        """
        Energy demand per unit of load energy.

        It is possible, that some storages need additional energy to load energy. This parameter defines demand per 1
        unit of loaded energy. Type of needed energy can be different, that the type of energy produced by the source.

        :return: Dict[EnergyType, np.ndarray]
        """
        return self.__demand_per_unit_load

    @property
    def demand_per_unit_gen(self) -> Dict[EnergyType, np.ndarray]:
        """
        Energy demand per unit of generated (retrieved) energy.

        It is possible, that some storages need additional energy to retrieve stored energy. This parameter defines
        demand per 1 unit of (retrieved) energy. Type of needed energy can be different, that the type of energy
        produced by the source.

        :return: Dict[EnergyType, np.ndarray]
        """
        return self.__demand_per_unit_gen


class Storage(Unit, IdManager):

    def __init__(self, name: str, placement: PlacementType, energy_type: EnergyType):
        Unit.__init__(self, placement, energy_type)
        IdManager.__init__(self, name)

    def __repr__(self):
        return f"Storage(id={self.id}, name={self.name}, placement={self.placement}, energy_type={self.energy_type})"
