from abc import abstractmethod
from typing import Dict
import numpy as np

from builder.scheme.elements.utils import IdElement
from builder.scheme.types import CarrierType, EmissionType


class Carrier(IdElement):

    def __init__(self, name: str):
        IdElement.__init__(self, name)

    @property
    @abstractmethod
    def carrier_type(self) -> CarrierType:
        pass

    def __repr__(self):
        return f"Carrier(id={self.id}, name={self.name}, carrier_type={self.carrier_type})"


class CarrierParameters:

    def __init__(self, carrier_id: int):
        self.__carrier_id = carrier_id

    @property
    def carrier_id(self) -> int:
        """
        Parameterized element identifier.

        :return: int
        """
        return self.__carrier_id


class Fuel(Carrier):

    @property
    def carrier_type(self) -> CarrierType:
        return CarrierType.FUEL


class FuelParameters(CarrierParameters):

    def __init__(
            self,
            carrier_id: int,
            availability: np.ndarray,
            price: np.ndarray,
            gcv: float,
            ncv: float,
            emission: Dict[EmissionType, float]
    ):
        """
        :param carrier_id:
        :param availability: availability per year, y -> total amount
        :param price: price per year, y -> cost of 1 unit of fuel
        :param gcv: float - gross caloric value
        :param ncv: float - net caloric value
        :param emission: Dict[EmissionType, np.ndarray] - yearly emission per 1 unit of fuel
        """
        super().__init__(carrier_id)
        self.__availability = availability
        self.__price = price
        self.__ncv = ncv
        self.__gcv = gcv
        self.__emission = emission

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

    @property
    def carrier_type(self) -> CarrierType:
        return CarrierType.PROFILE


class ProfileParameters(CarrierParameters):
    def __init__(self, carrier_id: int, series: np.ndarray):
        """
        :param carrier_id:
        :param series: carrier hourly activity, e.g. insolation factor for solar energy, velocity for wind, ...
        """
        super().__init__(carrier_id)
        self.__series = series

    @property
    def series(self) -> np.ndarray:
        return self.__series

