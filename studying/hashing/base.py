# make hash table
class HashTable:
    def __init__(self):
        self.size = 100
        self.table = [None] * self.size

    #hash function
    def get_hash(self, key):
        hash_value = 0
        for char in key:
            h += ord(char) #find ascii value for that character
        return h % self.size

    #add item
    def __setitem__(self, key, value):
        hash_value = self.get_hash(key)
        self.table[hash_value] = value

    #get key
    def __getitem__(self, key):
        hash_value = self.get_hash(key)
        return self.table[hash_value]
    
    #delete item
    def __delitem__(self, key):
        hash_value = self.get_hash(key)
        self.arr[hash_value] = None
    

t = HashTable()

#__setitem__
t['lj'] = 26
#__getitem__
print(t['lj'])
# __delitem__
del t['lj']

print(t.arr)


