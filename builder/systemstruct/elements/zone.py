from typing import Dict
import numpy as np
from pandas import Series

from builder.systemstruct.elements.utils import IdManager
from builder.systemstruct.types import EnergyType


class Zone(IdManager):

    def __init__(self, demand: Dict[EnergyType, np.ndarray], stacks: np.ndarray, base_fractions: Series):
        super().__init__()
        self.__demand = demand
        self.__stacks = stacks
        self.__base_fractions = base_fractions
