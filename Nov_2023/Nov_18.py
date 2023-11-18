# Reverse a Doubly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Solution:
    def reverseDLL(self, head):
        curr = head

        while curr:
            head = curr
            prev = curr.prev
            curr.prev = curr.next
            curr.next = prev
            curr = curr.prev

        return head

# Example usage:
# Creating a sample doubly linked list
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2

# Creating an instance of Solution
solution = Solution()

# Reversing the doubly linked list
reversed_head = solution.reverseDLL(node1)

# Printing the reversed doubly linked list
current = reversed_head
while current:
    print(current.data, end=" ")
    current = current.next
