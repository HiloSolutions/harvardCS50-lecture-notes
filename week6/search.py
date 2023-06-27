from sys import exit

names = ["Bill", "Charlie", "Fred", "George", "Ginny", "Percy", "Ron"]

name = input("Name: ")

# LINEAR SEARCH
if name in names:
    print("Found")
    exit(0)

print("Not found")
exit(1)
