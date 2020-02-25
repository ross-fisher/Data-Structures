"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
            
    def __gt__(self, other_node):
        return self.value > other_node.value


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""



from functools import reduce

# ctor -> constructor 
def monoid(fn, ctor):
    def _monoid(a=None, b=None):
        if a is None: 
            return ctor()
        else:
            return fn(a, b)
    
    return _monoid


def max_monoid(coll):
    maxer = lambda a, b: a if a > b else b
    ctor = lambda: float('-inf')
    return reduce(monoid(maxer, ctor), coll)


class DoublyLinkedListIterator:
    def __init__(self, doubly_linked_list):
        self.doubly_linked_list = doubly_linked_list 
        self.node = self.doubly_linked_list.head 
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.node is None:
            raise StopIteration # python uses this exception to stop iterating
        else:
            old_node = self.node 
            self.node = self.node.next
            return old_node       


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
        
    def __iter__(self):
        return DoublyLinkedListIterator(self)

    def set_head_tail(self, value):
        self.head = ListNode(value)
        self.tail = self.head 

    def add_to_head(self, value):
        if self.head is None: 
            self.set_head_tail(value)
        else: 
            self.head.insert_before(value)
            self.head = self.head.prev 

        self.length += 1

    def remove_from_head(self):
        if self.head:
            value = self.head.value
            self.delete(self.head)
            return value


    def add_to_tail(self, value):
        if self.tail is None: 
            self.set_head_tail(value)
        else: 
            self.tail.insert_after(value)
            self.tail = self.tail.next 

        self.length += 1

    def remove_from_tail(self):
        if self.tail:
            value = self.tail.value
            self.delete(self.tail)
            return value

    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node.value)

    def move_to_end(self, node_or_val):
        self.delete(node)
        self.add_to_tail(node.value)
        
    def __repr__(self):
        result = '['+', '.join(str(node.value) for node in self.__iter__()) + ']'
        return result

    def delete(self, node):
        if self.head is None: 
            return 
        else:
            iter_node = self.head
            self.length -= 1
            while(iter_node is not None):
                # found the node, delete
                if node == iter_node:
                    if node == self.tail:
                        self.tail = node.prev
                    if node == self.head:
                        self.head = node.next 
                
                    node.delete()

                iter_node = iter_node.next
    

    def get_max(self):
        return max_monoid(self.__iter__()).value
        


