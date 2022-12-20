import numpy as np

from builder.system.types import EnergyType


class EnergyDemand:

    def __init__(self, data: np.ndarray, et: EnergyType):
        self.__data = data
        self.__et = et

    @property
    def data(self) -> np.ndarray:
        return self.__data

    @property
    def et(self) -> EnergyType:
        return self.__et
