

class SchemeError(Exception):
    pass


class SchemeDuplicateError(SchemeError):
    def __init__(self, element_id, element_type, aggregate):
        self.message = f"can not add element of type {element_type} and {element_id} to the {aggregate}, " \
                       f"element {element_id} is already in the {repr(aggregate)}"


class SchemeElementNotFoundError(SchemeError):
    def __init__(self, element_id, element_type, aggregate):
        self.message = f"there is no {element_type} of id {element_id} in the {repr(aggregate)}"


class SchemeExistingReferenceError(SchemeError):
    def __init__(self, element, reference_element, aggregate):
        self.message = f"removing element {repr(element)} from {repr(aggregate)} is not possible, other element " \
                       f"{repr(reference_element)} contains reference to it"
