# 1-use a list comprehension to create a new list passed containing only scores >= 50
scores = [55, 89, 32, 76, 91, 40, 67]
score = [s for s in scores if s >= 50]
print(score)

# 2-use a list comprehension to create grades where each score becomes "Pass" if >=50 else "Fail"

grades = ["Pass" if s >= 50 else "Fail" for s in scores]
print(grades)

# 3-write a loop that prints the sum of each row.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

sum = 0
for raw in matrix:
    for num in raw:
        sum += num
    print(sum)
    sum = 0

# 4-sort the list in descending order without using .sort(reverse=True) — instead use .sort() then .reverse() as two separate steps, and print the result.
numbers = [4, 2, 9, 1, 7, 5]
numbers.sort()
numbers.reverse()
print(numbers)

# 5-Append 99 to list_a. Print all three lists and explain in a comment which ones changed and why.
list_a = [1, 2, 3]
list_b = list_a
list_c = list_a.copy()
list_a.append(99)
print(list_a)
print(list_b)
print(list_c)

# here asign list_a to list_b ,it actually assinging a reference og object but list_c is a copy of a list_a it diffent object
