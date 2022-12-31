from typing import List


class SchemeError(Exception):
    pass


class SchemeDuplicateError(SchemeError):
    def __init__(self, element_id, element_type, aggregate):
        self.message = f"can not add element of type {element_type} and id {element_id} to the {aggregate}, " \
                       f"element {element_id} is already in the {repr(aggregate)}"


class SchemeElementNotFoundError(SchemeError):
    def __init__(self, element_id, element_type, aggregate):
        self.message = f"there is no {element_type} of id {element_id} in the {repr(aggregate)}"


class SchemeExistingReferenceError(SchemeError):
    def __init__(self, element, reference_element, aggregate):
        self.message = f"removing element {repr(element)} from {repr(aggregate)} is not possible, other element " \
                       f"in the system: {repr(reference_element)} contains reference to it"


class SchemeNonExistingReferenceError(SchemeError):
    def __init__(self, element, reference_id, reference_type):
        self.message = f"adding element {repr(element)} is not possible, since it contains a reference to element of " \
                       f"type {reference_type} and id {reference_id} which is not contained in the system"


class SchemeIncompatibleEnergyTypesError(SchemeError):
    def __init__(self, element, reference_element):
        self.message = f"element {element} has different energy type than the element to which it contains a " \
                       f"reference to: {reference_element}"


class SchemeOneToManyViolationError(SchemeError):
    def __init__(self, element, existing_connection, new_connection):
        self.message = f"the element {repr(element)} is already connected to one element: {existing_connection}, it " \
                       f"can be connected to at most one element of that type, so it is not possible to add another: " \
                       f"{new_connection} to which the element is connected to"
