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


class DlinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        node = Node(data,None,self.head)
        if self.head is not None:
            self.head.prev = node
        self.head = node

    def insert_at_end(self,data):
        if self.head == None:
            self.head = Node(data)
            return
        
        current = self.head

        while current.next is not None:
            current = current.next

        current.next = Node(data,current)
    

    def __str__(self):
        node = self.head
        str = ""
        while node is not None:
            str = str + "-->" + node.__str__()
            node = node.next
        return str

    def __len__(self):
        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.next
        return count
    