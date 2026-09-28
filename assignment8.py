# 1 - unpack it into four separate variables in one line, then print each.
student = ("Darshan", 24, "IT", 7.12)
a, b, c, d = student
print(a, b, c, d)

# 2 -

# 3 - print the union, intersection, difference (set_a - set_b), and symmetric difference.
set_a = {10, 20, 30, 40}
set_b = {30, 40, 50, 60}
print(set_a | set_b)
print(set_a - set_b)
print(set_a ^ set_b)
print(set_a & set_b)  #

# 4 -, use a set to find and print only the duplicate emails (emails that appear more than once)
emails = ["a@x.com", "b@x.com", "a@x.com", "c@x.com", "b@x.com"]
count = {}
for email in emails:
    count[email] = count.get(email, 0) + 1

duplicates = {email for email, c in count.items() if c > 1}
print(duplicates)

# 5 -use set operations to find which skills Darshan already has that match the job  and which required skills he's missing.
skills_darshan = ["Java", "Spring Boot", "MySQL", "Git"]
skills_job = ["Java", "Python", "MySQL", "Docker"]
s_darshan = set(skills_darshan)
j_darshan = set(skills_job)

print(s_darshan & j_darshan)
print(j_darshan - s_darshan)
