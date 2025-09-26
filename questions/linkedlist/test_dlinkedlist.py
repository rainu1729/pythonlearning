import pytest

from questions.linkedlist.dlinkedlist import Node,DlinkedList

@pytest.fixture
def node():
    return Node(10,None,None)

def test_node_str(node):
    assert str(node) == "10"


@pytest.fixture
def empty_dlist():
    return DlinkedList()

def test_dlinkedlist_insert_at_beginning(empty_dlist):
    empty_dlist.insert_at_beginning(3)
    empty_dlist.insert_at_beginning(2)
    empty_dlist.insert_at_beginning(1)

    assert str(empty_dlist) == "-->1-->2-->3"

def test_dlinkedlist_insert_at_end(empty_dlist):
    empty_dlist.insert_at_end(1)
    empty_dlist.insert_at_end(2)
    empty_dlist.insert_at_end(3)

    assert str(empty_dlist) == "-->1-->2-->3"