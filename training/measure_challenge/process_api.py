

class ProcessAPI:
    def __init__(self):
        self.modules = {}

    def add_module(self, name, module):
        self.modules[name] = module

    def call(self, module, method, params):
        module = self.modules[module]
        method = getattr(module, method)
        return method(**params)