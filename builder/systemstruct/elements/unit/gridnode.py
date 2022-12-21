from builder.systemstruct.elements.unit.source import CentralSource, LocalSource


class GridNode:
    pass


class CentralGridNode(CentralSource, GridNode):
    pass


class LocalGridNode(LocalSource, GridNode):
    pass
