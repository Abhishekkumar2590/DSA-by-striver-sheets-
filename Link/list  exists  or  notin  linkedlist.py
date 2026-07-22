class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def searchKey(self, head, key):
        curr = head
        while curr:   # traverse until end
            if curr.data == key:
                return True
            curr = curr.next
        return False

# Example usage
# Create linked list: 10 -> 20 -> 30
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n1.next = n2
n2.next = n3

sol = Solution()
print(sol.searchKey(n1, 20))  # True
print(sol.searchKey(n1, 40)) 
# False
