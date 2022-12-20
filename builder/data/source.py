from abc import abstractmethod
from typing import List, Dict
import numpy as np

from builder.data.carrier import Carrier, CarrierType
from builder.data.demand import EnergyDemand
from builder.data.utils import EnergyType, Placement, Generation


# eff should have shape (n_years, life_time)
# all parameters p_min, p_max, max_p_incr, max_p_decr are global
class Source:

    def __init__(
            self,
            carrier: Carrier,
            generation: Generation,
            eff: np.ndarray,
            life_time: np.ndarray,
            build_time: np.ndarray,
            p_min: np.ndarray,
            p_max: np.ndarray,
            max_p_incr: np.ndarray,
            max_p_decr: np.ndarray,
            energy_type: EnergyType,
            capex: np.ndarray,
            opex: np.ndarray,
            demand_per_unit: EnergyDemand
    ):
        """
        General class for any type of source in the energy system.

        :param carrier: Carrier - type of energy carrier used by the source
        :param generation: Generation - how generation of source is defined (CONTROLLABLE, PROFILED, FIXED)
        :param eff: np.ndarray - how many units of energy of type self.ext_en_type will be produced from one unit of
        carrier of ncv = 1 TODO: ask someone who knows the stuff how it is usually parametrized
        :param life_time: np.ndarray - life time of source
        :param build_time: np.ndarray - how long it takes to build the source
        :param p_min: np.ndarray - minimal power installed per year
        :param p_max: np.ndarray - maximal power installed per year
        :param max_p_incr - maximal power increase in years
        :param max_p_decr - maximal power decrease in years
        :param energy_type: EnergyType - type of energy source can produce (e.g. heat, electricity)
        :param capex: np.ndarray - investment cost for each year [PLN / 1 unit of power]
        :param opex: np.ndarray - maintenance cost for each year [PLN / 1 unit of power]
        :param demand_per_unit: EnergyDemand - amount of energy consumed by the source per unit of produced energy
        """
        self.__carrier = carrier
        self.__generation = generation
        self.__eff = eff
        self.__life_time = life_time
        self.__build_time = build_time
        self.__p_min = p_min
        self.__p_max = p_max
        self.__max_p_incr = max_p_incr
        self.__max_p_decr = max_p_decr
        self.__energy_type = energy_type
        self.__capex = capex
        self.__opex = opex
        self.__dem_per_unit = demand_per_unit

    @property
    def energy_type(self) -> EnergyType:
        """
        :return: type of energy source can produce (e.g. heat, electricity)
        """
        return self.__energy_type

    @property
    def life_time(self) -> np.ndarray:
        """
        :return: life time of source
        """
        return self.__life_time

    @property
    def build_time(self) -> np.ndarray:
        """
        :return: how long it takes to build the source
        """
        return self.__build_time

    @property
    def generation(self) -> Generation:
        """
        :return: how generation of source is defined (CONTROLLABLE, PROFILED, FIXED)
        """
        return self.__generation

    @property
    def dem_per_unit(self) -> EnergyDemand:
        """
        :return: amount of energy consumed by the source per unit of extracted energy from carrier
        """
        return self.__dem_per_unit

    @property
    def carrier(self) -> Carrier:
        """
        :return: type of energy carrier used by the source
        """
        return self.__carrier

    @property
    def eff(self) -> np.ndarray:
        """
        :return: how many units of energy of type self.ext_en_type will be produced from one unit of carrier of ncv = 1
        """
        return self.__eff

    @property
    def p_max(self) -> np.ndarray:
        """
        :return: maximal power installed per year
        """
        return self.__p_max

    @property
    def p_min(self) -> np.ndarray:
        """
        :return: minimal power installed per year
        """
        return self.__p_min

    @property
    def max_p_incr(self) -> np.ndarray:
        """
        :return: maximal power increase in years
        """
        return self.__max_p_incr

    @property
    def max_p_decr(self) -> np.ndarray:
        """
        :return: maximal power decrease in years
        """
        return self.__max_p_decr

    @abstractmethod
    @property
    def placement(self) -> Placement:
        """
        :return: LOCAL or GLOBAL
        """
        pass


class LocalSource(Source):

    def __init__(
            self,
            p_min_z: np.ndarray,
            p_max_z: np.ndarray,
            max_p_incr_z: np.ndarray,
            max_p_decr_z: np.ndarray,
            *args,
            **kwargs
    ):
        """
        Local energy source general type.

        :param p_min_z: np.ndarray - minimal power per year and zone
        :param p_max_z: np.ndarray - maximal power per year and zone
        :param max_p_incr_z: np.ndarray - maximal power increase per year and zone
        :param max_p_decr_z: np.ndarray - minimal power increase per year and zone
        """
        super(LocalSource, self).__init__(*args, **kwargs)
        self.__p_min_z = p_min_z
        self.__p_max_z = p_max_z
        self.__max_p_incr_z = max_p_incr_z
        self.__max_p_decr_z = max_p_decr_z

    @property
    def placement(self) -> Placement:
        return Placement.LOCAL

    @property
    def p_min_z(self) -> np.ndarray:
        """
        :return: minimal power per year and zone
        """
        return self.__p_min_z

    @property
    def p_max_z(self) -> np.ndarray:
        """
        :return: maximal power per year and zone
        """
        return self.__p_max_z

    @property
    def max_p_incr_z(self) -> np.ndarray:
        """
        :return: maximal power increase per year and zone
        """
        return self.__max_p_incr_z

    @property
    def max_p_decr_z(self) -> np.ndarray:
        """
        :return: maximal power decrease per year and zone
        """
        return self.__max_p_decr_z


class GlobalSource(Source):

    @property
    def placement(self) -> Placement:
        return Placement.GLOBAL


class SourceContainer:

    def __init__(self, sources: List[Source]):

        self.__data = {
            (pl, ct): dict(
                (idx, s) for idx, s in enumerate(sources) if s.carrier.carrier_type == ct and s.placement == pl
            ) for pl in Placement for ct in CarrierType
        }

    def __getitem__(self, placement: Placement, carrier_type: CarrierType) -> Dict[int, Source]:
        return self.__data[placement, carrier_type]
