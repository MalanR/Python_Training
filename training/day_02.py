 # functions and loops

def add(a, b):
    return a + b

answer = add(23, 78)
print(answer)


list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for item in list:
#     print(item)

# I want to add each item in the list together and print the result
def add_items():
    total = 0
    for item in list:
        total += item
    print(total)

add_items()

