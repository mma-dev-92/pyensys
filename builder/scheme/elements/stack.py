import dataclasses
from typing import Dict

from builder.scheme.elements.utils import IdElement
from builder.scheme.types import PlacementType, EnergyType
import builder.scheme.error as err


@dataclasses.dataclass
class StackTuple:
    base: int
    peak: int = None
    storage: int = None

    def __repr__(self):
        return f"StackTuple(base={self.base}, peak={self.peak}, storage={self.storage})"

    def __post_init__(self):
        if self.base is None:
            raise ValueError(f"base_id must be always set, None value is not allowed")


class Stack(IdElement):

    def __init__(self, name: str, members: Dict[EnergyType, StackTuple], placement: PlacementType):

        super().__init__(name)
        self.__members = members
        self.__placement = placement

    def __getitem__(self, energy_type: EnergyType) -> StackTuple:
        return self.__members[energy_type]

    def __setitem__(self, energy_type: int, stack_tuple: StackTuple):
        self.__check_energy_type(energy_type)
        self.__members[energy_type] = stack_tuple

    @property
    def placement(self) -> PlacementType:
        return self.__placement

    @property
    def members(self) -> Dict[EnergyType, StackTuple]:
        return self.__members

    def __repr__(self):
        members_str = {repr(et): repr(members) for et, members in self.members.items()}
        return f"Stack(id={self.id}, name={self.name}, placement={self.placement}, members={members_str}"

    def __check_energy_type(self, energy_type: EnergyType):
        if energy_type not in self.__members:
            raise err.SchemeElementNotFoundError(element_id=energy_type.id, element_type=EnergyType, aggregate=self)
