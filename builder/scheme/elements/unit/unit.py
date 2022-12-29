import dataclasses
import numpy as np

from builder.scheme.types import EnergyType, PlacementType


@dataclasses.dataclass
class CostParams:
    capex: np.ndarray
    opex: np.ndarray


@dataclasses.dataclass
class TimeParams:
    life_time: int
    build_time: int
    amortization_time: int


class ElementParameters:

    def __init__(self, element_id: int, cost_params: CostParams, time_params: TimeParams):

        self.__element_id = element_id
        self.__life_time = time_params.life_time
        self.__build_time = time_params.build_time
        self.__amortization_time = time_params.amortization_time

        self.__capex = cost_params.capex
        self.__opex = cost_params.opex

    @property
    def id(self) -> int:
        """
        Parameterized element identifier.

        :return: int
        """
        return self.__element_id

    @property
    def life_time(self) -> int:
        """
        Time of life of the source.

        If life_time = n, and given amount of power of the source was build in year y, then in the year y + n this power
        is no longer available, since its time of life has passed. It can be replaced by other source or rebuild.

        :return: float - time of life of the source
        """
        return self.__life_time

    @property
    def build_time(self) -> int:
        """
        Time needed to build the source.

        If build_time = m, and building process of given amount of power of the source has been begun in year y, then in
        the year y + m this power will be available, since the build will be over.

        :return: float - time needed to build the source
        """
        return self.__build_time

    @property
    def amortization_time(self) -> int:
        """
        Numbers of years of investment amortization.

        If amortization_time = k, and if the investment (of total cost C) was made in year y, then in each year starting
        from y up to y + k - 1, total charged cost will be equal to C/k.

        :return: int - investment amortization time.
        """
        return self.__amortization_time

    @property
    def capex(self) -> np.ndarray:
        """
        Investment cost.

        Average cost of building one unit of power of the source in each year.

        :return: Y-dimensional vector containing investment cost for each year.
        """
        return self.__capex

    @property
    def opex(self) -> np.ndarray:
        """
        Maintenance cost.

        Average maintenance cost of one unit of power of the source in each year.

        :return: Y-dimensional vector containing investment cost for each year.
        """
        return self.__opex


class Unit:

    def __init__(self, placement: PlacementType, energy_type: EnergyType):
        self.__placement = placement
        self.__energy_type = energy_type

    @property
    def energy_type(self) -> EnergyType:
        """
        Type of the source energy output.

        :return: EnergyType
        """
        return self.__energy_type

    @property
    def placement(self) -> PlacementType:
        """
        LOCAL or CENTRAL.

        Informs if the source is a local or central energy source.

        :return: PlacementType
        """
        return self.__placement
