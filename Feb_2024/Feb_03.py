# Decimal Equivalent of Binary Linked List

class node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Solution:
    def decimalValue(self, head):
        MOD = 10**9 + 7
        decimal_value = 0

        # Traverse the linked list
        while head:
            # Update the decimal value by left-shifting and adding the current bit
            decimal_value = (decimal_value << 1) | head.data
            # Take modulo to avoid overflow
            decimal_value %= MOD
            # Move to the next node
            head = head.next

        return decimal_value

# Example usage:
solution = Solution()

# Example Linked List: 1 -> 0 -> 1
head = node(1)
head.next = node(0)
head.next.next = node(1)

output = solution.decimalValue(head)
print(output)  # Output: 5
