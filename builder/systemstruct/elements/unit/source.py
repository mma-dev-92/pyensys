from abc import ABC
from numpy import ndarray

from builder.systemstruct.elements.unit import Unit
from builder.systemstruct.types import PlacementType


class Source(Unit, ABC):

    def __init__(self, p_max: ndarray, p_min: ndarray, p_max_incr: ndarray, p_max_decr: ndarray, *args, **kwargs):
        super(Source, self).__init__(*args, **kwargs)
        self.__p_max = p_max
        self.__p_min = p_min
        self.__p_max_incr = p_max_incr
        self.__p_max_decr = p_max_decr

    @property
    def p_max(self) -> ndarray:
        """
        Maximal power for every year y.

        For given year y, p_max[y] is an upper bound for P_y.

        :return: Y-dimensional vector containing maximal powers per each year.
        """
        return self.__p_max

    @property
    def p_min(self) -> ndarray:
        """
        Minimal power for every year y.

        For given year y, p_min[y] is a lower bound for P_y.

        :return: Y-dimensional vector containing minimal powers per each year.
        """
        return self.__p_min

    @property
    def p_max_incr(self) -> ndarray:
        """
        Maximal power increase.

        For given year y < y_{max}, p_max_incr[y] is an upper bound for P_{y+1} - P_y.

        :return: (Y-1)-dimensional vector containing maximal power increase in each year
        """
        return self.__p_max_incr

    @property
    def p_max_decr(self) -> ndarray:
        """
        Maximal power decrease.

        For given year y < y_{max}, p_max_decr[y] is an upper bound for P_y - P_{y+1}.

        :return: (Y-1)-dimensional vector containing maximal power decrease in each year
        """
        return self.__p_max_decr


class CentralSource(Source):

    @property
    def placement(self) -> PlacementType:
        return PlacementType.CENTRAL


class LocalSource(Source):

    @property
    def placement(self) -> PlacementType:
        return PlacementType.LOCAL
