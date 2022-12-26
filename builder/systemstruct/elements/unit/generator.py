from typing import Dict
import numpy as np

from builder.systemstruct.elements.unit.unit import Unit, CostParams, TimeParams
from builder.systemstruct.elements.utils import IdManager
from builder.systemstruct.types import EnergyType, PlacementType


class Generator(Unit, IdManager):

    def __init__(
            self,
            name: str,
            placement: PlacementType,
            energy_type: EnergyType,
            cost_params: CostParams,
            time_params: TimeParams,
            carrier_id: int,
            efficiency: float,
            demand_per_unit: Dict[EnergyType, np.ndarray],
    ):

        Unit.__init__(self, placement, energy_type, cost_params, time_params)
        IdManager.__init__(self, name)
        self.__demand_per_unit = demand_per_unit
        self.__carrier_id = carrier_id
        self.__efficiency = efficiency

    @property
    def demand_per_unit(self) -> Dict[EnergyType, np.ndarray]:
        """
        Energy demand per unit of produced energy.

        It is possible, that some generators need additional energy to operate (for example air-heating pumps need
        electricity). This parameter defines demand per 1 unit of output energy. Type of needed energy can
        be different, that the type of energy produced by the source.

        :return: Dict[EnergyType, np.ndarray]
        """
        return self.__demand_per_unit

    @property
    def carrier(self) -> int:
        """
        Energy carrier used by generator.

        :return: int - and id of a carrier
        """
        return self.__carrier_id

    @property
    def efficiency(self) -> float:
        """
        Efficiency of the generator.

        This parameter defines how many units of output energy is produced by the generator from 1 unit of carrier.

        :return: float
        """
        return self.__efficiency
