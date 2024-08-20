# dictionaries, arrays, schemas
# Schemas are json files that define the structure of a file or a data object


# 1. Create a dictionary with 2 key-value pairs:


# 2. create an array with two values:


# 3. Create a dictionary with 2 arrays:


# 4. Create an Array with 2 dictionaries:


# print the second key value pair of the first dictionary


# print the first value of the first array



# print the second value of the first array in the second dictionary


# print the value of key 3 in the second array



# Basic schema structure

schema = {
    "id" : "extention_name",
    "main": {
        "steps" : {
            "start" : "start_step",
            "args" : {
                "arg1" : "value1",
                "arg2" : "value2"
            }
        }
    }
}

# print the value of both args
