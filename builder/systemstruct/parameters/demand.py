import numpy as np

from builder.systemstruct.types import EnergyType


class Demand:

    def __init__(self, arr: np.ndarray, et: EnergyType):
        self.__arr = arr
        self.__et = et

    @property
    def arr(self) -> np.ndarray:
        return self.arr

    @property
    def et(self) -> EnergyType:
        return self.__et
