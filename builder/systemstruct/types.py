from enum import Enum

from builder.systemstruct.elements.utils import IdManager


class DynamicEnum(IdManager):

    def __init__(self, name: str):
        super().__init__()
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name


class EmissionType(DynamicEnum):
    pass


class EnergyType(DynamicEnum):
    pass


class CarrierType(Enum):
    PROFILE = 1
    FUEL = 2


class PlacementType(Enum):
    LOCAL = 1
    CENTRAL = 2
