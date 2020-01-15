# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        index = self._hash_mod(key)
        current_node = self.storage[index]
        last_node = None

        while (current_node is not None) and (current_node.key != key): # Collision
            last_node = current_node
            current_node = last_node.next
        if current_node is not None:
            current_node.value = value
        else: # create and add new node
            new_node = LinkedPair(key, value) 
            new_node.next = self.storage[index]
            self.storage[index] = new_node


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        current_node  = self.storage[index]
        last_node = None

         #if requested node not found and key doesn't match, iterate through nodes changing the pointers.
        while(current_node is not None) and (current_node.key != key):
            last_node = current_node
            current_node = last_node.next
        if current_node is None:
            print('key not removed')
        if last_node is None: # if linked pair is at the start of the list
            self.storage[index] = current_node.next
        else:
            last_node.next = current_node.next


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key) # compute the index of the key
        current_node = self.storage[index] # go to first node
        while current_node is not None: # traverse linked list at this node
            if current_node.key == key: 
                return current_node.value # return value if key is the target
            current_node = current_node.next # if not go on and try the next node

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2 # doubling the capacity
        prev = self.storage
        self.storage = [None] * self.capacity # creating new array with an increased capacity

        for each_node in prev:
            current_node = each_node #interate each node
            while current_node is not None: #  ... while we still have elements in nodes
                self.insert(current_node.key, current_node.value)
                current_node = current_node.next
        



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
