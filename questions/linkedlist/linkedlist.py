class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

    def __add__(self, other):
        if isinstance(other, Node):
            print("into node concat")
            return str(self.data) + " " + str(other.data)
        else:
            print("into node+str concat")
            return str(self.data) + " " + str(other)


class LinkedList:
    def __init__(self):
        print("Linked list created")
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(data, None)

    def __str__(self):
        node = self.head
        str = ""
        while node is not None:
            str = str + "-->" + node.__str__()
            node = node.next
        return str


if __name__ == "__main__":
    print("inside the name and main check")

    ll = LinkedList()

    ll.insert_at_beginning(7)

    ll.insert_at_beginning(6)

    ll.insert_at_beginning(5)

    print(ll)

    ll.insert_at_end(8)

    ll.insert_at_end(9)

    print(ll)
