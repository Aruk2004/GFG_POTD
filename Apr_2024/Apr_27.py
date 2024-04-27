# Merge Sort on Doubly Linked List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Solution():
    def sortDoubly(self, head):
        lis = []
        while head:
            lis.append(head.data)
            head = head.next
        lis.sort()
        root = Node(lis[0])
        cur = root
        for i in lis[1:]:
            cur.next = Node(i)
            cur.next.prev = cur
            cur = cur.next
        return root

# Example usage
# Create a doubly linked list
head = Node(3)
head.next = Node(1)
head.next.prev = head
head.next.next = Node(2)
head.next.next.prev = head.next

# Sort the doubly linked list
sol = Solution()
sorted_head = sol.sortDoubly(head)

# Print the sorted linked list
current = sorted_head
while current:
    print(current.data, end=" ")
    current = current.next
