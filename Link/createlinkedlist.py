class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)       # create new node
        new_node.next = self.head   # link new node to current head
        self.head = new_node        # update head to new node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
        
ll = LinkedList()
ll.insert_at_beginning(30)   # list: 30 -> None
ll.insert_at_beginning(20)   # list: 20 -> 30 -> None
ll.insert_at_beginning(10)
# list: 10 -> 20 -> 30 -> None

ll.display()
        