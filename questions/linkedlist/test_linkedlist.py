import pytest
from questions.linkedlist.linkedlist import Node, LinkedList

def test_node_str():
    node = Node(10)
    assert str(node) == "10"

def test_node_add_node():
    node1 = Node(1)
    node2 = Node(2)
    assert node1 + node2 == "1 2"

def test_node_add_str():
    node = Node(5)
    assert node + "test" == "5 test"

def test_linkedlist_insert_at_beginning():
    ll = LinkedList()
    ll.insert_at_beginning(1)
    ll.insert_at_beginning(2)
    assert str(ll) == "-->2-->1"

def test_linkedlist_insert_at_end():
    ll = LinkedList()
    ll.insert_at_end(1)
    ll.insert_at_end(2)
    assert str(ll) == "-->1-->2"

def test_linkedlist_create_ll_from_list():
    ll = LinkedList()
    ll.create_ll_from_list([1, 2, 3])
    assert str(ll) == "-->1-->2-->3"

def test_linkedlist_remove_at():
    ll = LinkedList()
    ll.create_ll_from_list([1, 2, 3])
    ll.remove_at(1)
    assert str(ll) == "-->1-->3"

def test_linkedlist_insert_at_index():
    ll = LinkedList()
    ll.create_ll_from_list([1, 2, 3])
    ll.insert_at_index(1, 99)
    assert str(ll) == "-->1-->99-->2-->3"

def test_linkedlist_node_at_index():
    ll = LinkedList()
    ll.create_ll_from_list([1, 2, 3])
    node = ll.node_at_index(1)
    assert node.data == 2

def test_linkedlist_len():
    ll = LinkedList()
    ll.create_ll_from_list([1, 2, 3, 4])
    assert len(ll) == 4

def test_linkedlist_iter():
    ll = LinkedList()
    ll.create_ll_from_list([1, 2, 3])
    items = [item for item in ll]
    assert items == [1, 2, 3]

def test_linkedlist_str_empty():
    ll = LinkedList()
    assert str(ll) == ""

def test_linkedlist_str_nonempty():
    ll = LinkedList()
    ll.create_ll_from_list([1, 2])
    assert str(ll) == "-->1-->2"
