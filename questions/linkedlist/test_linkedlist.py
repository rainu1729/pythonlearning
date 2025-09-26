import pytest
from questions.linkedlist.linkedlist import Node, LinkedList

@pytest.fixture
def node():
    return Node(10)

@pytest.fixture
def node_one():
    return Node(1)

@pytest.fixture
def node_two():
    return Node(2)

@pytest.fixture
def empty_list():
    return LinkedList()

@pytest.fixture
def populated_list():
    ll = LinkedList()
    ll.create_ll_from_list([1, 2, 3])
    return ll

def test_node_str(node):
    assert str(node) == "10"

def test_node_add_node(node_one, node_two):
    assert node_one + node_two == "1 2"

def test_node_add_str(node):
    assert node + "test" == "10 test"

def test_linkedlist_insert_at_beginning(empty_list):
    empty_list.insert_at_beginning(1)
    empty_list.insert_at_beginning(2)
    assert str(empty_list) == "-->2-->1"

def test_linkedlist_insert_at_end(empty_list):
    empty_list.insert_at_end(1)
    empty_list.insert_at_end(2)
    assert str(empty_list) == "-->1-->2"

def test_linkedlist_create_ll_from_list(empty_list):
    empty_list.create_ll_from_list([1, 2, 3])
    assert str(empty_list) == "-->1-->2-->3"

def test_linkedlist_remove_at(populated_list):
    populated_list.remove_at(1)
    assert str(populated_list) == "-->1-->3"

def test_linkedlist_insert_at_index(populated_list):
    populated_list.insert_at_index(1, 99)
    assert str(populated_list) == "-->1-->99-->2-->3"

def test_linkedlist_node_at_index(populated_list):
    node = populated_list.node_at_index(1)
    assert node.data == 2

def test_linkedlist_len(populated_list):
    assert len(populated_list) == 3

def test_linkedlist_iter(populated_list):
    items = [item for item in populated_list]
    assert items == [1, 2, 3]

def test_linkedlist_str_empty(empty_list):
    assert str(empty_list) == ""

def test_linkedlist_str_nonempty(empty_list):
    empty_list.create_ll_from_list([1, 2])
    assert str(empty_list) == "-->1-->2"
