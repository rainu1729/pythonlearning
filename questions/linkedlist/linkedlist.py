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


class LinkedListiterator:
    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data


class LinkedList:
    def __init__(self):
        self.head = None

    def __invalidindex(self, index):
        if index < 0 or index >= len(self):
            raise Exception("Invalid Index")

    def node_at_index(self, index):
        self.__invalidindex(index)

        current_index = 0
        current_node = self.head
        while current_node is not None:
            if current_index == index:
                return current_node
            current_node = current_node.next
            current_index += 1

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

    def create_ll_from_list(self, list):
        self.head = None
        for data in list:
            self.insert_at_end(data)

    def remove_at(self, index):
        self.__invalidindex(index)

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        node = self.head
        while node is not None:
            if count == index - 1:
                node.next = node.next.next
                break
            node = node.next
            count += 1
        return

    def insert_at(self, index, data):
        self.__invalidindex(index)

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

    def __iter__(self):
        return LinkedListiterator(self.head)


if __name__ == "__main__":
    ll = LinkedList()

    ll.insert_at_beginning(7)

    ll.insert_at_beginning(6)

    ll.insert_at_beginning(5)

    print(ll)

    print(f"Node at a specific index 2:: {ll.node_at_index(2)}")

    print("----------------------------------")

    # print("element at position 2 :"+ll.node_at_index(2))

    # ll.insert_at_end(8)

    # ll.insert_at_end(9)

    # print(ll)

    # lls = LinkedList()

    # lls.insert_at_beginning("A")

    # lls.insert_at_beginning("B")

    # lls.insert_at_beginning("C")

    # lls.insert_at_end("D")

    # lls.insert_at_end("E")

    # print(lls)

    llv = LinkedList()

    llv.create_ll_from_list(["orange", "apple", "banana", "grape", "kiwi"])

    print(llv)

    # print(f"Length of llv is {len(llv)}")
    # try:
    #     llv.remove_at(1)
    # except Exception as e:
    #     print(e)

    # print(llv)

    # print(f"Length of llv is {len(llv)}")

    # for node in llv:
    #     print(type(node))
