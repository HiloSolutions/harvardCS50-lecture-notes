def if_statement(x, y):
  if x < y:
      print("1. x is less than y")


def if_else_statement(x, y):
   if x < y:
      print("2. x is less than y")
   else:
      print("2. y is less than x")


def elif_statement(x, y):
   if x < y:
      print("3. x is less than y")
   elif x > y:
      print("3. y is less than x")
   else:
      print("3. y is equal to x")

        
if_statement(5, 10)
if_else_statement(10, 5)
elif_statement(10, 10)