# Delete Middle of Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def deleteMid(self, head):
        if head.next is None:
            return None
        fast = slow = head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        slow.next = slow.next.next
        return head

# Example usage
# Create a linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Print the original linked list
current = head
while current:
    print(current.data, end=" ")
    current = current.next
print()

# Delete the middle node
sol = Solution()
head = sol.deleteMid(head)

# Print the modified linked list after deleting the middle node
current = head
while current:
    print(current.data, end=" ")
    current = current.next
