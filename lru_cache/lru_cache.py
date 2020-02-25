from doubly_linked_list import DoublyLinkedList


# - Lookup by key (hashtable)
# - Queue (doubly linked list)
# - Need the cache enties in a doubly linked list, in order to be able to store
#   if something was recently used or not
class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.data = {}
        self.orderlist = DoublyLinkedList()
        self.limit = limit

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # cache hit
        if key in self.data:
            self.add_to_lru(key)
            return self.data[key]
        # cache miss
        else: 
            return None 
        
    
    def add_to_lru(self, key):
        """Add an entry to the lru queue, poping the oldest thing and removing from 
           the cache if the limit is hit"""
        if len(self.orderlist) >= self.limit+1:
            lru_item = self.orderlist.remove_from_tail()
            self.data.pop(lru_item)

        if key in self.data:
            # find the node and move it to the front in the list, making it the most
            # recently used thing 
            for node in self.orderlist:
                if node.value == key: 
                    self.orderlist.move_to_front(node)
                    break
        else:   
            # else add to the order list
            self.orderlist.add_to_head(key)
    

    def __repr__(self):
        return '\n'.join([str(self.data), str(self.orderlist)])
        
        
    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        self.add_to_lru(key)
        self.data[key] = value

