class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
       
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:   # empty list
            self.head = new_node
            return
        temp = self.head
        while temp.next:        # traverse till last node
            temp = temp.next
        temp.next = new_node
    
    def count(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

# Example usage
l1 = LinkedList()
l1.insert_at_end(10)
l1.insert_at_end(20)
l1.insert_at_end(30)

print("Count of nodes:", l1.count())


