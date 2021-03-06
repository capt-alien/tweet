#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]
        self.number_of_entries = 0

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # ^^runtime: O(n^2) --> has a nested loop that makes it quadradic time
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # ^^runtime: O(n^2) --> has a nested loop that makes it quadradic time
        #Declare a list to return
        values = []
        # TODO: Loop through all buckets
        for bucket in self.buckets:
            # Collect all values in each bucket
            for key, value in bucket.items():
                values.append(value)
            return values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Runtime O(n) --> it loops through inputs
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        # O(1) --> this data is stored in a variable so it is readly accessable
        return self.number_of_entries
        # Loop through all buckets

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(???) Why and under what conditions?"""
        # O(1)  --> Key should be already indexed
        # Find bucket where given key belongs
        index = self._bucket_index(key)
        finder = False
        key_value = self.buckets[index].find(lambda item: item[0] == key)
        # find(lambda item: item[0] == key) --> ret.data[0] = key
        if key_value is not None:
            finder = True
        return finder

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Runtime: O(1) --> uses contains to loacate key
        if self.contains(key):
            bucket = self.buckets[self._bucket_index(key)]
            return bucket.find(key)
        else:
            raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        # Runtime: O(1)
        index = self._bucket_index(key)
        key_value = (key, value)
        print(key_value)
        try:
            self.buckets[index].replace(lambda item: item[0] == key, key_value)
        except ValueError:
            self.buckets[index].append(key_value)
        self.number_of_entries += 1

    def delete(self, key):
        index = self._bucket_index(key)
        key_value = self.buckets[index].find(lambda item: item[0] == key)
        if key_value is None:
            raise KeyError('Key not found: {}'.format(key))
        else:
            self.buckets[index].delete(key_value)
            self.number_of_entries -=1


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
