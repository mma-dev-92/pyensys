import itertools


class IdManager:

    obj_id = itertools.count()

    def __init__(self, name: str):
        self.__id = next(IdManager.obj_id)
        self.__name = name

    @property
    def id(self) -> int:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    def __eq__(self, other):
        return isinstance(other, IdManager) and other.id == self.id and other.name == self.name
