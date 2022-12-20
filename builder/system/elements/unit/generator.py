from builder.system.elements.unit.source import LocalSource, CentralSource


class Generator:
    pass


class LocalGenerator(LocalSource, Generator):
    pass


class CentralGenerator(CentralSource, Generator):
    pass
