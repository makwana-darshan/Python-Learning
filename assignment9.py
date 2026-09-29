# 1-Write a function min_max(numbers) that returns a tuple (minimum, maximum) using the built-ins min() and max().
from assignment8 import count


def min_max(numbers):
    return min(numbers), max(numbers)


low, high = min_max([4, 2, 9, 1, 7])
print(f"min:{low} & high:{high}")


# 2-Write a function is_even(n) that returns True if n is even, otherwise False. Test it with 10 and 7

def iseven(num):
    if num % 2 == 0:
        return True
    return False


print(iseven(6))


# 3-Write a function power(base, exponent=2) that returns base ** exponent. Call it once with only base and once with both values.

def power(base, exponent=2):
    return base ** exponent


print(power(5, 3))


# 4 -Write a function average(*numbers) that accepts any number of values and returns their average. Test it with 3 numbers and with 6 numbers.

def average(*number):
    return sum(number) / len(number)


print(average(1, 2, 5, 8, 6))


# 5-Write a function find_duplicates(items) that takes a list and returns a set of the items that appear more than once.

def find_duplicates(items):
    count = {}
    for item in items:
        count[item] = count.get(item, 0) + 1
    duplicates = {key for key, c in count.items() if c > 1}
    return duplicates


its = ["darsh", "jil", "darshan", "jil", "darsh"]
print(find_duplicates(its))


# 6-Write a recursive function sum_to(n) that returns 1 + 2 + ... + n (for example, sum_to(5) is 15). Remember the base case.

def sum_to(n):
    if n <= 0:
        return 0
    return n + sum_to(n - 1)


print(sum_to(5))
