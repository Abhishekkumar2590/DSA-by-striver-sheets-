class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        
        # Case 1: Empty list
        if self.head is None:
            self.head = new_node
            return
        
        # Case 2: Traverse to the last node
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
l1 = LinkedList()
ll = LinkedList()
ll.insert_at_end(10)   # list: 10 -> None
ll.insert_at_end(20)   # list: 10 -> 20 -> None
ll.insert_at_end(30) 
l1.insert_at_end(40)
# list: 10 -> 20 -> 30 -> None
ll.display()

