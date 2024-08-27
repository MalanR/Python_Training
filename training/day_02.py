# The process API

# The goal for today, create a process API class that can register modules and call modules
# Use the process API class to register a module for adding two values, call this modules and return the result
# the process api in this context is a stores and serves modules
# your modules will contain methods
# you will need to call your methods through the process api.


class ProcessAPI:
    def __init__(self):
        self.modules = {}

    def add_module(self, name, module):
        self.modules[name] = module

    def call(self, module, method, params):
        module = self.modules[module]
        method = getattr(module, method)
        return method(**params)


class MathModule:

    @staticmethod
    def add(value1, value2):
        return value1 + value2

    @staticmethod
    def subtract(value1, value2):
        return value1 - value2


api = ProcessAPI()
api.add_module("math", MathModule)
add_result = api.call("math", "add", {"value1": 5, "value2": 6})
subtract_result = api.call("math", "subtract", {"value1": 6, "value2": 5})
print(add_result)
print(subtract_result)

