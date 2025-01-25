import pprint
import inspect



def introspection_info(obj):
    type_of_object = (type(obj))
    attribute_list = dir(obj)
    attributes_of_object = [attr for attr in attribute_list if not attr.startswith('_')]
    methods_of_object = [attr for attr in attribute_list if attr.startswith('_')]
    #methods_of_object = inspect.getmembers(obj, predicate=inspect.ismethod)
    module_of_object = inspect.getmodule(obj)
    callable_or_not = callable(obj)
    dict_info = {
        'type': type_of_object,
        'attributes': attributes_of_object,
        'methods': methods_of_object,
        'module':module_of_object,
        'callable': callable_or_not}
    return dict_info

print(introspection_info(50))


class Vegetables:
    def __init__(self, color:str, mass:int, solid:bool):
        self.color = color
        self.mass = mass
        self.solid = solid
        self.alive = True
    def destruction (self):
        self.alive = False

    def colorization (self):
        self.color = 'blue'



cucumber = Vegetables('green',50,False)

print(introspection_info(cucumber))