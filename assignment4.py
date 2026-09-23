#1
for num in range(1,21):
    if num % 2 != 0:
        continue
    print(num)

#2
marks = [45, 67, 89, 32, 95, 50]
for i,mark in enumerate(marks):
    print(i+1,mark)

#3
i=1
while i<=10:
    print(7*i)
    i +=1

#4
for num in range(1,51):
    if num %3==0 and num %7==0:
        print(num)
        break

#5
names = ["Ravi", "Priya", "Aman", "Sneha"]
for name in names:
    print(name.upper())