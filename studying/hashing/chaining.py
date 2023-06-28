# make hash table
class HashTable:
    def __init__(self):
        self.size = 100
        self.arr = [[] for i in range(self.size)]  # List comprehension

    # hash function
    def get_hash(self, key):
        hash_value = 0
        for char in key:
            hash_value += ord(char)  # find ascii value for that character
        return hash_value % self.size

    # add item

    def __setitem__(self, key, value):
        hash_value = self.get_hash(key)
        bucket = self.table[hash_value]

        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                # Update existing key's value
                bucket[i] = (key, value)
                return
        # key does not exist, append to the bucket
        bucket.append((key, value))

    # get key

    def __getitem__(self, key):
        hash_value = self.get_hash(key)
        bucket = self.table[hash_value]

        for existing_key, value in bucket:
            if existing_key == key:
                return value

    # delete item

    def __delitem__(self, key):
        hash_value = self.get_hash(key)
        bucket = self.table[hash_value]

        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                del bucket[i]
                return

         # Key does not exist
        raise KeyError(key)
    


# Test cases
ht = HashTable()

# Test case 1: Inserting a key-value pair
ht['key1'] = 'value1'
assert ht['key1'] == 'value1'

# Test case 2: Updating an existing key
ht['key1'] = 'updated_value'
assert ht['key1'] == 'updated_value'

# Test case 3: Inserting multiple key-value pairs with collisions
ht['key2'] = 'value2'
ht['key3'] = 'value3'
ht['key4'] = 'value4'
assert ht['key2'] == 'value2'
assert ht['key3'] == 'value3'
assert ht['key4'] == 'value4'

# Test case 4: Updating a key with collisions
ht['key3'] = 'updated_value3'
assert ht['key3'] == 'updated_value3'

# Test case 5: Accessing a non-existent key
try:
    value = ht['non_existent_key']
except KeyError:
    assert True
else:
    assert False

# Test case 6: Deleting an existing key
del ht['key1']
try:
    value = ht['key1']
except KeyError:
    assert True
else:
    assert False

# Test case 7: Deleting a non-existent key
try:
    del ht['non_existent_key']
except KeyError:
    assert True
else:
    assert False

# Test case 8: Inserting a key-value pair with a large hash value
ht['key5'] = 'value5'
ht['key200'] = 'value200'
assert ht['key5'] == 'value5'
assert ht['key200'] == 'value200'

# Test case 9: Updating a key with a large hash value
ht['key200'] = 'updated_value200'
assert ht['key200'] == 'updated_value200'