import json


# 1 - Write a function write_lines(filename, lines) that writes a list of strings to a file, one per line (handle the \n yourself). Call it with ["Darshan", "Priya", "Ravi"] and a filename of your choice.

def write_lines(filename, lines):
    with open(filename, "w") as f:
        for line in lines:
            f.write(f"{line}\n")


write_lines("info.txt", ["Darshan", "Priya", "Ravi"])


# 2. Write a function read_lines(filename) that reads that file back and returns a list of the lines without trailing newlines (use .strip()). Print the result.

def read_lines(filename):
    with open(filename, "r") as f:
        for line in f:
            print(line.strip())


read_lines("info.txt")


# 3. Write a function append_log(filename, message) that appends a single line to a log file using "a" mode. Call it three times with different messages, then open the file and confirm all three lines are present.


def append_log(filename, message):
    with open(filename, "a") as f:
        f.write(f"{message}\n")


append_log("info.txt", "first log")


# 4. Write a function safe_read(filename) that tries to read a file and returns its content, but catches FileNotFoundError and returns None instead of crashing. Test it with a file that exists and one that doesn't.

def safe_read(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        return None


safe_read("info.txt")
safe_read("missing.txt")

# 5. Create a Python dictionary representing your own resume data (name, skills as a list, years of experience), convert it to a JSON string with json.dumps(..., indent=2) and print it. Then write it to a file profile.json using json.dump().

resume = {
    "Name": "Darshan Makwana",
    "skills": ["java", "python", "sql"],
    "Yoe": 0.3
}
with open("profile.json", "w") as f:
    json.dump(resume, f, indent=2)

# 6. Read profile.json back using json.load(), print the "skills" list, and print how many skills are listed using len()
with open("profile.json", "r") as f:
    data = json.load(f)

skill_list = data['skills']

print(skill_list)
print(len(skill_list))
