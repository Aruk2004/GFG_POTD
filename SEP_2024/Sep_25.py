# Palindrome Linked List

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Function to check whether the list is palindrome.
class Solution:
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        
        # Step 1: Find the middle of the linked list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the list
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        
        # Step 3: Compare the first and the second half
        left = head
        right = prev
        while right:  # Only need to compare until the end of the second half
            if left.data != right.data:
                return False
            left = left.next
            right = right.next
        
        return True

# Example Usage
# Create a linked list: 1 -> 2 -> 1
head = Node(1)
head.next = Node(2)
head.next.next = Node(1)

sol = Solution()
print(sol.isPalindrome(head))  # Output: True

# Create a linked list: 1 -> 2 -> 3 -> 4
head2 = Node(1)
head2.next = Node(2)
head2.next.next = Node(3)
head2.next.next.next = Node(4)

print(sol.isPalindrome(head2))  # Output: False
