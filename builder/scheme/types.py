from enum import Enum

from builder.scheme.elements.utils import IdElement


class EmissionType(IdElement):

    def __repr__(self):
        return f"EmissionType(id={self.id}, name={self.name})"


class EnergyType(IdElement):

    def __repr__(self):
        return f"EnergyType(id={self.id}, name={self.name})"

    def __hash__(self):
        return hash(self.__repr__())


class CarrierType(str, Enum):
    PROFILE = 'PROFILE'
    FUEL = 'FUEL'


class PlacementType(str, Enum):
    LOCAL = 'LOCAL'
    CENTRAL = 'CENTRAL'
