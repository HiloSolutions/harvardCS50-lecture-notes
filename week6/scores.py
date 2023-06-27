def main():
   scores = get_scores()
   len_example(scores)
   average_example(scores)


# len: how many elements are in this list?
def get_scores():
      scores = []

      for i in range(3):
          try:
              n = int(input("Score: "))
              if n > 0:
                scores.append(n)
          except ValueError:
            print("Not an integer.")

      return scores




def len_example(l):
   print("Length:", len(l))

def average_example(l):
   s = sum(l)
   c = len(l)
   print("Average:", s / c)


main()