# 1-Print each key-value pair using .items() in the format "name: Darshan".
student = {
    "name": "Darshan",
    "cgpa": 7.12,
    "branch": "IT"
}
for key, value in student.items():
    print(f"{key}: {value}")

# 2-add a new item "grapes": 40, then increase "apple" by 10 without retyping the full dictionary.
inventory = {
    "apple": 50,
    "banana": 30,
    "mango": 20
}
inventory["grapes"] = 40
inventory["apple"] = inventory.get("apple") + 10

for key, value in inventory.items():
    print(f"{key}: {value}")

# 3-use a dictionary comprehension to create a new dict passed containing only subjects with marks >= 70.
marks = {
    "Math": 90,
    "Science": 78,
    "English": 65
}

newone = {k: v for k, v in marks.items() if v >= 70}

print(newone)

# 4-merge them using the | operator and print the result. Explain in a comment which value wins for the key that exists in both.
dict_a = {"x": 1, "y": 2}
dict_b = {"y": 5, "z": 3}

merged = dict_a | dict_b
print(merged)

# it accepts dict_b value of "y" because of it accept new value

# 5-count how many times each character appears using a dictionary
word = "programming"
count_char = {}
for char in word:
    count_char[char] = count_char.get(char, 0) + 1

print(count_char)
