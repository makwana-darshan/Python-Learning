# 1 - Write a function safe_divide(a, b) that divides a by b and returns the result, but catches ZeroDivisionError and returns None with a printed message instead of crashing.~
from oddoreven import result


def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print(e)
        return None


safe_divide(3, 3)
safe_divide(3, 0)


# 2 - Write a function get_value(dictionary, key) that returns dictionary[key], catching KeyError and returning "Key not found" instead of crashing.

def get_value(dictionary, key):
    try:
        return dictionary[key]
    except KeyError:
        return "Key not found"


person = {
    "name": "darshan",
    "age": 22
}
get_value(person, "collage")


# 3 - Write a function convert_to_int(value) that tries to convert value to an int, catching ValueError, and returns -1 on failure. Test with "42" and "abc"

def convert_to_int(value):
    try:
        return int(value)
    except ValueError as e:
        return -1


convert_to_int("abc")
convert_to_int("42")


# 4 - Create a custom exception class NegativeNumberError(Exception). Write a function check_positive(n) that raises this custom exception if n is negative, with a message like "Number cannot be negative". Call it inside a try/except and print the caught message for n = -5

class NegativeNumberError(Exception):
    pass


def check_positive(n):
    if n < 0:
        raise NegativeNumberError("Number cannot be negative")
    print("safe")


try:
    check_positive(5)
    check_positive(-5)
except NegativeNumberError as e:
    print(e)


# 5 - Write a function process_list(items) that loops through a list, tries to convert each item to an int, and uses try/except inside the loop to skip invalid items instead of crashing — collecting only the successfully converted integers into a new list, and returning it. Test with ["10", "abc", "20", "xyz", "30"]


def process_list(items):
    result = []
    for item in items:
        try:
            result.append(int(item))
        except ValueError as e:
            continue
    return result


print(process_list(["10", "abc", "20", "xyz", "30"]))
