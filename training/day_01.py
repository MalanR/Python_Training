# dictionaries, arrays, schemas
# Schemas are json files that define the structure of a file or a data object


# 1. Create a dictionary with 2 key-value pairs:
my_dict = {"key1": "value1", "key2": "value2"}

# 2. create an array with two values:
my_array = [1, 2]
print(my_array[1])

a = [1, 2, 3, "kiran"]
print(a[1])

a.insert(2, "KK")
print(a)

del a[2]
print(a)
# 3. Create a dictionary with 2 arrays:


# 4. Create an Array with 2 dictionaries:


# print the second key value pair of the first dictionary


# print the first value of the first array



# print the second value of the first array in the second dictionary


# print the value of key 3 in the second array



# Basic schema structure

schema = {
    "id" : "extention_name",
    "description" : "description of the extension",
    "main": {
        "steps" : {
            "start" : "start_step",
            "args" : {

            }
        }
    }
}

# print the values of both args in args
print(schema["main"]["steps"].get("args", []))


Kiran = {"age":30}
Malana ={"age": 25}
Kumar = {"age": 35}

def average_age(person1, person2):
    return (person1.get("age") + person2.get("age")) / 2

result = average_age(Kiran, Kumar)
print(result)

