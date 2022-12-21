from abc import abstractmethod
import numpy as np

from builder.systemstruct.parameters.demand import Demand
from builder.systemstruct.types import EnergyType, PlacementType


class Unit:

    def __init__(
            self,
            energy_type: EnergyType,
            life_time: int,
            build_time: int,
            amortization_time: int,
            capex: np.ndarray,
            opex: np.ndarray,
            demand_per_unit: Demand
    ):
        self.__life_time = life_time
        self.__build_time = build_time
        self.__amortization_time = amortization_time
        self.__energy_type = energy_type
        self.__capex = capex
        self.__opex = opex

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
    def energy_type(self) -> EnergyType:
        """
        Type of the source energy output.

        :return: EnergyType
        """
        return self.__energy_type

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

    @abstractmethod
    @property
    def placement(self) -> PlacementType:
        """
        LOCAL or CENTRAL.

        Informs if the source is a local or central energy source.

        :return: PlacementType
        """
        pass
