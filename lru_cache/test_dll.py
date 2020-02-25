from doubly_linked_list import DoublyLinkedList, ListNode, max_monoid


def test_it():
    node = ListNode(1)
    dll = DoublyLinkedList(node)

    dll.remove_from_tail()
    assert dll.head is None
    assert dll.tail is None

    dll.add_to_tail(33)
    assert dll.head.value == 33
    assert dll.tail.value == 33
    
    assert dll.remove_from_tail() == 33
    
def test_max_monoid():
    node = ListNode(1)
    dll = DoublyLinkedList(node)
    dll.add_to_tail(33)
    dll.add_to_tail(30)
    dll.add_to_tail(21)
    dll.add_to_tail(99)
    dll.add_to_tail(-10)
    assert dll.get_max() == 99
    assert max_monoid([1,2,3,5,-2,9,1]) == 9
    assert max_monoid([1]) == 1
