import dataclasses
from typing import Dict

from builder.scheme.elements import GridNode, Storage, Generator
from builder.scheme.elements.utils import IdElement
from builder.scheme.types import PlacementType, EnergyType
import builder.scheme.error as err


@dataclasses.dataclass
class StackTuple:
    gen: Generator = None
    grid_node: GridNode = None
    peak: Generator = None
    storage: Storage = None

    def __repr__(self):
        return f"StackTuple(gen={self.gen}, grid_node={self.grid_node}, peak={self.peak}, storage={self.storage})"

    def __post_init__(self):
        if self.gen is None:
            raise ValueError(f"base generator must be always set, None value is not allowed")
        self.__validate_base_energy_source()
        self.__validate_member_types()
        self.__validate_energy_types()
        self.__validate_duplicates()

    def __validate_base_energy_source(self):
        if self.gen is None and self.grid_node is None:
            raise err.AttributeNotFoundError(
                attr_name='gen or grid_node', attr_type=f'{Generator} or {GridNode}', element_type=self.__class__)

    def __validate_energy_types(self):
        if self.peak is not None and self.peak.energy_type == self.gen.energy_type:
            raise err.IncompatibleEnergyTypesError(element=self.peak, reference_element=self)
        if self.storage is not None and not self.storage.energy_type == self.gen.energy_type:
            raise err.IncompatibleEnergyTypesError(element=self.storage, reference_element=self)

    def __validate_duplicates(self):
        if self.peak is not None and (self.peak == self.gen or self.peak == self.grid_node):
            raise err.DuplicateError(element=self.peak, aggregate=self)

    def __validate_member_types(self):
        if self.gen is not None and not isinstance(self.gen, Generator):
            raise err.InvalidAttributeTypeError(element_type=self.__class__, attr_name='gen', attr_type=Generator)

        if self.grid_node is not None and not isinstance(self.grid_node, GridNode):
            raise err.InvalidAttributeTypeError(element_type=self.__class__, attr_name='grid_node', attr_type=GridNode)

        if self.peak is not None and not isinstance(self.peak, Generator):
            raise err.InvalidAttributeTypeError(element_type=self.__class__, attr_name='peak', attr_type=Generator)

        if self.storage is not None and not isinstance(self.storage, Storage):
            raise err.InvalidAttributeTypeError(element_type=self.__class__, attr_name='storage', attr_type=Storage)


class Stack(IdElement):

    def __init__(self, name: str, members: Dict[EnergyType, StackTuple], placement: PlacementType):

        super().__init__(name)
        self.__members = members
        self.__placement = placement

    def __getitem__(self, energy_type: EnergyType) -> StackTuple:
        self.__check_energy_type(energy_type)
        return self.__members[energy_type]

    def __setitem__(self, energy_type: int, stack_tuple: StackTuple):
        self.__check_energy_type(energy_type)
        self.__members[energy_type] = stack_tuple

    @property
    def placement(self) -> PlacementType:
        return self.__placement

    def __repr__(self):
        members_str = {repr(energy_type): repr(stack_tuple) for energy_type, stack_tuple in self.__members.items()}
        return f"Stack(id={self.id}, name={self.name}, placement={self.placement}, members={members_str}"

    def __check_energy_type(self, energy_type: EnergyType):
        if energy_type not in self.__members:
            raise err.ElementNotFoundError(element_id=energy_type.id, element_type=EnergyType, aggregate=self)
