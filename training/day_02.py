# The process API

# The goal for today, create a process API class that can register modules and call modules
# Use the process API class to register a module for adding two values, call this modules and return the result
# the process api in this context is a stores and serves modules
# your modules will contain methods
# you will need to call your methods through the process api.

class ProcessAPI:
    def __init__(self):
        self.modules = {}

    def register(self, name, module):
        self.modules[name] = module

    def call(self, modules_name, method_name, params):
        model = self.modules[modules_name]
        method = getattr(model, method_name)
        return method(**params)


class Math:
    @staticmethod
    def add_speed(a, b):
        return a + b


api = ProcessAPI()
api.register("car", Math)
result = api.call("car", "add_speed", {"a": 14, "b": 2})
print(result)

class processAPI:
    def __init__(self):
        self.book =  {}

    def register(self, book_name, module):
        self.book[book_name] = module

    def call(self,book_name, method_name, params):
        module = self.book[book_name]
        method = getattr(module, method_name)
        return method(**params)

class Book_type:
    @staticmethod
    def add_page_number(page1, page2):
        return page1 + page2


api = processAPI()
api.register("book", Book_type)
result = api.call("book", "add_page_number", {"page1": 100, "page2": 200})
print(result)







