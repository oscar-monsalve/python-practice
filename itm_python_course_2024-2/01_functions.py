# Functions: generalities

def print_hello() -> None:
    print("Hello, World!")


def pi_value() -> str:
    return "3.14"


def sum_const(a: int) -> int:
    a += 3
    return a


def sum_finger(a: int, b: int) -> int:
    sum = a + b
    subs = a - b
    return sum, subs


# Inputs that may have more that one value. We can use the "*" operator in front of the variable.
def data_base(*arg):
    print(arg)


# data = 1, 2, 3, 4, 5
# data_base(data)

# If I have data like a dictionary with key and value pairs, we use **kwargs. This is called keyword arguments in
# functions
def print_dict(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"Key: {key}")
        print(f"Value: {value}")


# print_dict(A=1, B=2, C=3, D="R")


# The id() function returns a unique id for the specified object.
# The id is the object's memory address, and will be different for each time you run the program. (except for some
# object that has a constant unique id, like integers from -5 to 256)

# a = 1
# print(id(a))


def loc_function(data):
    data += 9
    print(id(data))
    return data


# print(loc_function(a))

array = [1, 2, 3]
# print(f"original data {id(array)}")


def append_array(data):
    array.append(5)
    print(id(data))
    return data


# append_array(array)

# ------------------------------------------------------------------

# Functions: good practices


def return_const():
    """
    Returns a constant.
    """
    return 2.75


# We can print in the terminal the dicumentation of a function using "__doc__"
# print(return_const.__doc__)


# We can specify the type of the function's arguments and the return type of the function. However, these annotations
# do not restrict the function.


def function_a(a: int) -> int:
    return a


# print(function_a.__annotations__)

# ------------------------------------------------------------------

# Lambda functions. The word "lambda" is a reserved word in python.

# sum = lambda a, b: a + b
# print(sum(3, 5))

# ------------------------------------------------------------------

# map function

temp_data = [23, 25, 28, 29]  # °C, I want to convert them to K

conv = lambda a: a + 273.15

# The function map will evluate the definition of "conv" on a set of data like "temp_data"
res = map(conv, temp_data)
print(list(res))
