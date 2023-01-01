from typing import Dict
import numpy as np

from builder.scheme.elements.carrier import Carrier
from builder.scheme.elements.unit.unit import Unit, CostParams, TimeParams, ElementParameters
from builder.scheme.elements.utils import IdElement
from builder.scheme.types import EnergyType, PlacementType


class GeneratorParameters(ElementParameters):

    def __init__(
            self,
            generator_id: int,
            cost_params: CostParams,
            time_params: TimeParams,
            efficiency: float,
            demand_per_unit: Dict[EnergyType, np.ndarray]
    ):
        super().__init__(generator_id, cost_params, time_params)
        self.__demand_per_unit = demand_per_unit
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
    def efficiency(self) -> float:
        """
        Efficiency of the generator.

        This parameter defines how many units of output energy is produced by the generator from 1 unit of carrier.

        :return: float
        """
        return self.__efficiency


class Generator(Unit, IdElement):

    def __init__(self, name: str, placement: PlacementType, energy_type: EnergyType, carrier_id: int):
        Unit.__init__(self, placement, energy_type)
        IdElement.__init__(self, name)
        self.__carrier_id = carrier_id

    @property
    def carrier_id(self) -> int:
        """
        Energy carrier used by generator.

        :return: int - id of a carrier
        """
        return self.__carrier_id

    @carrier_id.setter
    def carrier_id(self, value: Carrier):
        self.__carrier_id = value.id

    def __repr__(self):
        return f"Generator(id={self.id}, name={self.name}, placement={self.placement}, energy_type={self.energy_type}" \
               f", carrier_id={self.carrier_id})"
