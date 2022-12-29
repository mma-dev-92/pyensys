from enum import Enum

from builder.scheme.elements.utils import IdElement


class EmissionType(IdElement):

    def __repr__(self):
        return f"EmissionType(id={self.id}, name={self.name})"


class EnergyType(IdElement):

    def __repr__(self):
        return f"EnergyType(id={self.id}, name={self.name})"


class CarrierType(Enum):
    PROFILE = 1
    FUEL = 2


class PlacementType(Enum):
    LOCAL = 1
    CENTRAL = 2
