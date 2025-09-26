class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __str__(self):
        return str(self.data)

    def __add__(self, other):
        if isinstance(other, Node):
            return str(self.data) + " " + str(other.data)
        return str(self.data) + " " + str(other)

