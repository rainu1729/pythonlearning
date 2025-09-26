import pytest

from questions.linkedlist.dlinkedlist import Node

@pytest.fixture
def node():
    return Node(10,None,None)

def test_node_str(node):
    assert str(node) == "10"