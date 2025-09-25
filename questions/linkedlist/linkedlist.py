
class Node:
    def __init__(self, data=None , next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

    def __add__(self, other):
        if isinstance(other,Node):
            print("into node concat")
            return str(self.data)+" "+str(other.data)
        else:
            print("into node+str concat")
            return str(self.data)+" "+str(other)
    
class LinkedList:
    
    def __init__(self):
        print("Linked list created")
        self.head = None

    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node

    def __str__(self):
        
        node = self.head
        str  = ""
        while node is not None:
            str = str+"-->"+node.__str__()
            node = node.next
        return str
        

if __name__ ==  '__main__':
    print("inside the name and main check")

    ll = LinkedList()

    ll.insert_at_beginning(5)

    ll.insert_at_beginning(6)

    ll.insert_at_beginning(7)

    print(ll)