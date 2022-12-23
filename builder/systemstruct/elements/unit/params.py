import dataclasses
import numpy as np


@dataclasses.dataclass
class CostParams:
    capex: np.ndarray
    opex: np.ndarray


@dataclasses.dataclass
class TimeParams:
    life_time: int
    build_time: int
    amortization_time: int
