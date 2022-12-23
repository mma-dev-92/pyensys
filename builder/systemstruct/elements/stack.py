import dataclasses
from abc import abstractmethod
from typing import Dict

from builder.systemstruct.types import PlacementType, EnergyType


@dataclasses.dataclass
class StackTuple:
    base: int
    peak: int = None
    storage: int = None


class Stack:

    __counter = 0

    def __init__(
            self,
            members: Dict[EnergyType, StackTuple],
            max_peak2base: Dict[EnergyType, float],
            max_stor2base: Dict[EnergyType, float],
    ):

        self.__id = self.__next_id()

        self.__members = members
        self.__max_p2b = max_peak2base
        self.__max_s2b = max_stor2base

    def __getitem__(self, et: EnergyType) -> StackTuple:
        return self.__members[et]

    @classmethod
    def __next_id(cls) -> int:
        result = cls.__counter
        cls.__counter += 1
        return result

    @property
    def id(self) -> int:
        return self.__id

    @abstractmethod
    @property
    def placement(self) -> PlacementType:
        pass

    @property
    def members(self) -> Dict[EnergyType, StackTuple]:
        return self.__members

    @property
    def max_p2b(self) -> Dict[EnergyType, float]:
        return self.__max_p2b

    @property
    def max_s2b(self) -> Dict[EnergyType, float]:
        return self.__max_s2b
