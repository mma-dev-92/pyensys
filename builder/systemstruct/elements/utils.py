import itertools


class IdManager:

    obj_id = itertools.count()

    def __init__(self):
        self.__id = next(IdManager.obj_id)

    @property
    def id(self) -> int:
        return self.__id
