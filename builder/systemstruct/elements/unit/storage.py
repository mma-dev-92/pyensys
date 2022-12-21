from abc import ABC

from builder.systemstruct.elements.unit import Unit
from builder.systemstruct.types import PlacementType


class Storage(Unit, ABC):
    pass


class LocalStorage(Storage):

    @property
    def placement(self) -> PlacementType:
        return PlacementType.LOCAL


class CentralStorage(Storage):

    @property
    def placement(self) -> PlacementType:
        return PlacementType.CENTRAL
