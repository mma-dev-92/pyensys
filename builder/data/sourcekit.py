from abc import abstractmethod
from typing import Dict, List

from builder.data.utils import Placement, EnergyType


class SourceKit:

    def __int__(self, base_iis: Dict[EnergyType, int], peak_iis: Dict[EnergyType, int]):
        self.__base_iis = base_iis
        self.__peak_iis = peak_iis

    @abstractmethod
    @property
    def placement(self) -> Placement:
        pass

    @property
    def base_iis(self) -> Dict[EnergyType, int]:
        return self.__base_iis

    @property
    def peak_iis(self) -> Dict[EnergyType, int]:
        return self.__peak_iis


class LocalSourceKit(SourceKit):

    @property
    def placement(self) -> Placement:
        return Placement.LOCAL


class GlobalSourceKit(SourceKit):

    @property
    def placement(self) -> Placement:
        return Placement.GLOBAL


class SourceKitContainer:

    def __init__(self, source_kits: List[SourceKit]):
        local_ = [sk for sk in source_kits if sk.placement == Placement.LOCAL]
        global_ = [sk for sk in source_kits if sk.placement == Placement.GLOBAL]

        self.__data = {
            Placement.LOCAL: dict((idx, sk) for idx, sk in enumerate(local_)),
            Placement.GLOBAL: dict((idx, sk) for idx, sk in enumerate(global_))
        }

    def __getitem__(self, placement: Placement) -> Dict[int, SourceKit]:
        return self.__data[placement]
