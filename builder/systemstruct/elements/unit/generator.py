from builder.systemstruct.elements.carrier import Carrier
from builder.systemstruct.elements.unit.source import LocalSource, CentralSource
from builder.systemstruct.parameters.demand import Demand


class Generator:
    def __init__(self, demand_per_unit: Demand, carrier: Carrier, efficiency: float):
        self.__demand_per_unit = demand_per_unit
        self.__carrier = carrier
        self.__efficiency = efficiency

    @property
    def demand_per_unit(self) -> Demand:
        """
        Energy demand per unit of produced energy.

        It is possible, that some generators need additional energy to operate (for example air-heating pumps need
        electricity). This parameter defines demand per 1 unit of output energy. Type of needed energy can
        be different, that the type of energy produced by the source.

        :return: Demand
        """
        return self.__demand_per_unit

    @property
    def carrier(self) -> Carrier:
        """
        Energy carrier used by generator.

        :return: Carrier
        """
        return self.__carrier

    @property
    def efficiency(self) -> float:
        """
        Efficiency of the generator.

        This parameter defines how many units of output energy is produced by the generator from 1 unit of carrier.

        :return: float
        """
        return self.__efficiency


class LocalGenerator(LocalSource, Generator):
    pass


class CentralGenerator(CentralSource, Generator):
    pass
