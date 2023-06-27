# dictionary
people = {
    "Lauren": "902-907-8507",
    "Garrett": "902-686-7329",
    "Yennefer": "902-633-2575",
}

name = input("Name: ")

if name in people:
    number = people[name]
    print(f"Number: {number}")
