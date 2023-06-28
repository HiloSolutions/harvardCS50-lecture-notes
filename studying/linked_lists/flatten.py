#brute force

class Node:
    def __init__ (self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_node



f = Node(6)
e = Node(5, f)
d = Node(4, e)
c = Node(3, d)
b = Node(2, c)
a = Node(1, b)

print("a", a.get_value(), a.get_next_node())
print("b", b.get_value(), b.get_next_node())
print("c", c.get_value(), c.get_next_node())
print("d", d.get_value(), d.get_next_node())
print("e", e.get_value(), e.get_next_node())
print("f", f.get_value(), f.get_next_node())