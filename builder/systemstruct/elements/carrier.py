from abc import ABC, abstractmethod
from typing import Dict
import numpy as np

from builder.systemstruct.elements.utils import IdManager
from builder.systemstruct.types import CarrierType, EmissionType


class Carrier(ABC, IdManager):

    def __init__(self, name: str):
        IdManager.__init__(self, name)

    @abstractmethod
    @property
    def carrier_type(self) -> CarrierType:
        pass


class Fuel(Carrier):

    def __init__(
            self,
            name: str,
            availability: np.ndarray,
            price: np.ndarray,
            gcv: float,
            ncv: float,
            emission: Dict[EmissionType]
    ):
        """
        :param name: name of given fuel
        :param availability: availability per year, y -> total amount
        :param price: price per year, y -> cost of 1 unit of fuel
        :param gcv: float - gross caloric value
        :param ncv: float - net caloric value
        :param emission: Dict[EmissionType, np.ndarray] - yearly emission per 1 unit of fuel
        """
        super(Fuel, self).__init__(name)
        self.__availability = availability
        self.__price = price
        self.__ncv = ncv
        self.__gcv = gcv
        self.__emission = emission

    @property
    def carrier_type(self) -> CarrierType:
        return CarrierType.FUEL

    @property
    def availability(self) -> np.ndarray:
        return self.__availability

    @property
    def price(self) -> np.ndarray:
        return self.__price

    @property
    def gcv(self) -> float:
        return self.__gcv

    @property
    def ncv(self) -> float:
        return self.__ncv

    @property
    def emission(self) -> Dict[EmissionType, np.ndarray]:
        return self.__emission


class Profile(Carrier):

    def __init__(self, name: str, series: np.ndarray):
        """
        :param name: name of given profile
        :param series: carrier hourly activity, e.g. insolation factor for solar energy, velocity for wind, ...
        """

        super(Profile, self).__init__(name)
        self.__series = series

    @property
    def carrier_type(self) -> CarrierType:
        return CarrierType.PROFILE

    @property
    def series(self) -> np.ndarray:
        return self.__series
