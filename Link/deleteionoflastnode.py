class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def delete_node_from_last(self,data):
        new_node = Node(data)
        if  not self.head:
            self.head  = new_node
            return
        temp  = self.head
        while  temp.next:
            temp = temp.next
        temp.next = 
        
        # Case 1: Empty list
        
        
             
