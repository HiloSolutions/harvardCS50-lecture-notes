def meow():
    print("meow ")


def main(i):
    while i < 3:
        meow()
        i += 1

#the range function returns a sequence of numbers, in a given range default starting at 0. 
def for_loop(n):
    x = range(n)
    for i in x:
        print(i)



main(0)
for_loop(3)