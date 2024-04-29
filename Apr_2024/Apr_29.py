# Remove every kth node

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class Solution:
    def deleteK(self, head, k):
        if not head or k <= 0:
            return head
        
        if k == 1:  # Remove every node
            return None
        
        # Use two pointers to traverse the linked list
        prev = None
        current = head
        count = 0

        while current:
            count += 1
            if count % k == 0:  # This node needs to be removed
                if prev:
                    prev.next = current.next
                else:
                    head = current.next  # If the first node is removed, update the head
                current = current.next  # Move to the next node after deletion
            else:
                prev = current
                current = current.next
        
        return head

# Example usage:
# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)

k = 2  # Remove every 2nd node
sol = Solution()
new_head = sol.deleteK(head, k)

# Print the updated linked list
current = new_head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")  # Indicates the end of the list
