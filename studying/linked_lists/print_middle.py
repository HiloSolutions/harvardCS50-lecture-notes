#brute force

class Node:
    def __init__ (self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_node

class Solution:
    def middleNode(self , head: Node) -> Node:
      #get length
      len_list = 0
      start = node = head
      while start: 
          len_list += 1
          start = start.next_node

      middle = len_list / 2

      counter = 0
      while node:
          if counter == middle:
              return node
          else:
              node = node.next

      return None


f = Node(6)
e = Node(5, f)
d = Node(4, e)
c = Node(3, d)
b = Node(2, c)
a = Node(1, b)

print("length", a.get_value(), a.get_next_node())
