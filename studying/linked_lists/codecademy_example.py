class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node

    #get_value
  def get_value(self):
    return self.value

    #get_next_node
  def get_next_node(self):
    return self.next_node

    #set_next_node
  def set_next_node(self, next_node):
    self.next_node = next_node


class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)

    #get_head_node
  def get_head_node (self):
    return self.head_node

    #insert_beginning
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node

    #stringify_list

    #remove_node



#TESTING
a = Node(44)
b = Node(43)
c = Node(41)
d = Node(40)

a_value = a.get_value()
print(a_value) #44
a_next_node = a.get_next_node()
print(a_next_node) #None
a_new_pointer = a.set_next_node(b)
a_next_node = a.get_next_node()
print(a_next_node) #b node

list = LinkedList(1)
list_head = list.get_head_node()
print(list_head.get_value()) #1
list_new_head = list.insert_beginning(2)
print(list_head.get_value()) #2



  