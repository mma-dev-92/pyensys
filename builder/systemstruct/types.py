from enum import Enum

from builder.systemstruct.elements.utils import IdManager


class EmissionType(IdManager):
    pass


class EnergyType(IdManager):
    pass


class CarrierType(Enum):
    PROFILE = 1
    FUEL = 2


class PlacementType(Enum):
    LOCAL = 1
    CENTRAL = 2
