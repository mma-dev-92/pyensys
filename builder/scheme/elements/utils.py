import itertools


class ClassCounter:
    counters = {}
    names = {}

    @classmethod
    def get_counter(cls, class_to_count):
        cls.counters.setdefault(class_to_count, itertools.count())
        return next(cls.counters[class_to_count])

    @classmethod
    def check_name_uniqueness(cls, class_to_check, name_to_check):
        if class_to_check not in cls.names:
            cls.names[class_to_check] = set()

        if name_to_check in cls.names[class_to_check]:
            raise NameError(f"you are trying to create an instance of a class {class_to_check} with name "
                            f"{name_to_check}, however an instance of a class {class_to_check} with this name "
                            f"already exist.")


class IdElement:

    def __init__(self, name: str):
        self.__id = ClassCounter.get_counter(self.__class__)
        ClassCounter.check_name_uniqueness(self.__class__, name)
        self.__name = name

    @property
    def id(self) -> int:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    def __eq__(self, other):
        return isinstance(other, IdElement) and other.id == self.id and other.name == self.name
