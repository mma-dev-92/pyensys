from enum import Enum


class DynamicEnum:

    __counter = 0

    def __init__(self, name: str):
        self.__name = name
        self.__id = DynamicEnum.__counter
        DynamicEnum.__counter += 1

    @property
    def name(self) -> str:
        return self.__name

    @property
    def identifier(self) -> int:
        return self.__id

    def __eq__(self, other):
        return type(self) == type(other) and self.__id == other.__idx


class EnergyType(DynamicEnum):
    pass


class EmissionType(DynamicEnum):
    pass


class Placement(Enum):
    GLOBAL = 1
    LOCAL = 2


class Generation(Enum):
    CONTROLLABLE = 1
    PROFILED = 2
    FIXED = 3
