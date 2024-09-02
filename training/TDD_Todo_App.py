# Python  TodoApp
## To do app logic

# For this we are not interested in any UI, only the engine code that drives the todo app.
# Instead of UI the logic will be driven using unit tests, use Pytest for the unit tests.
# We will be testing if the application works by running the unit tests.
# The application should be comprehensively tested and all tests must pass.
#
# The project folder should contain two folders:
#
# 1. src - where all the application logic files are stored.
# 2. tests - where all the test files are located.
#
# Create a class named "TodoApp".
# This must have public methods for all the actions required.
# All methods should be async
#
# 1. create
# this will create a todo item on a datastructure of your choice in the TodoApp instance.
#
# 1. update
# make changes to a todo item so you will need a way to identify the todo item from the others and a way to define what changes to make.
# 2. delete
# remove a todo item from
# 3. complete
# set the todo item as being complete.
# 4. filter
# there are different filter criteria that should be supported
#     1. partial text search - find all the todo items where the description partially matches the text being passed.
#     2. completed - show me all the completed items
#     3. todo - show me all the items that have not yet been completed
#
# The TodoApp class should have one static factory function called "new" that will create a instance of TodoApp and return that instance.
# For example "app = TodoApp.new()"
#
# Each todo item stored should contain at least the following information.
#
# 1. id - unique idenfitifier for the item
# 2. description - what must be done.
# 3. created_on - when was the item create
# 4. completed_on - when was the item completed