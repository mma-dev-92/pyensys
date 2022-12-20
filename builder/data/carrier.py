from abc import ABC, abstractmethod
from enum import Enum

import numpy as np


class CarrierType(Enum):
    RENEWABLE = 1
    FUEL = 2


class Carrier(ABC):

    def __init__(self, name: str):
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name

    @abstractmethod
    @property
    def carrier_type(self) -> CarrierType:
        pass


class Fuel(Carrier):

    def __init__(self, name: str, availability: np.ndarray, price: np.ndarray, gcv: float, ncv: float):
        """
        :param name: name of given fuel
        :param availability: availability per year, y -> total amount
        :param price: price per year, y -> cost per unit
        :param gcv: float - gross caloric value
        :param ncv: float - net caloric value
        """
        super(Fuel, self).__init__(name)
        self.__availability = availability
        self.__price = price
        self.__ncv = ncv
        self.__gcv = gcv

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


class Renewable(Carrier):

    def __init__(self, name: str, profile: np.ndarray):
        """
        :param name: name of given fuel
        :param profile: renewable carrier hourly activity, e.g. insolation factor for solar energy, velocity for wind
        """

        super(Renewable, self).__init__(name)
        self.__profile = profile

    @property
    def carrier_type(self) -> CarrierType:
        return CarrierType.RENEWABLE

    @property
    def profile(self) -> np.ndarray:
        return self.__profile
