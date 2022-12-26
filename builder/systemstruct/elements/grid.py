from builder.systemstruct.elements.utils import IdManager
from builder.systemstruct.types import EnergyType


class Grid(IdManager):

    def __init__(self, name: str, energy_type: EnergyType, capacity: float, loss: float):
        IdManager.__init__(self, name)
