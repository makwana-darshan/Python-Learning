from pathlib import Path
# import os

#  with open("data.txt","r") as f:
#      content=f.read()
#     print(content)
#
# with open("data.txt","r") as f:
#     lines=f.readline()
#      print(lines)
#
#
# with open("data.txt","r") as f:
#    for line in f:
#        print(line.strip())
#
#
# with open("data.txt","w") as f:
#     f.write("Hello, Coder\n")
#     f.write("second line\n")
#
#
# lines = ["First", "Second", "Third"]
# with open("data.txt", "w") as f:
#     f.writelines(line + "\n" for line in lines)

# with open("data.txt","a") as f:
#     f.write("Four\n")

# try:
#     with open("missing.txt", "r") as f:
#         content = f.read()
# except FileNotFoundError:
#     print("File does not exist")

# print(os.getcwd())
# print(os.path.exists("data.txt"))
# print(os.path.join("folder",file.txt))

p=Path("data.txt")
print(p.exists())
print(p.name)
print(p.suffix)