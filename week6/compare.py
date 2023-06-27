from cs50 import get_int

# base example
x = input("x: ")
y = input("y: ")

if x < y:
    print("1. x < y")
elif x > y:
    print("1. x > y")
else:
    print("1. x = y")


#str exmple
s = input("Do you agree? ")
s = s.lower()

if s in ["y", "yes"]:
    print("Agreed")
elif s in ["n", "no"]:
    print("Disagreed")
