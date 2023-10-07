# Reverse alternate nodes in Link List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def rearrange(self, odd):
        even = odd
        rev_odd = None
        itr = odd

        while itr:
            next_itr = itr.next

            if next_itr:
                even.next = itr.next.next
                if even.next:
                    even = even.next
                next_itr.next = rev_odd
                rev_odd = next_itr
            else:
                break

            itr = even

        even.next = rev_odd

    # Utility function to print the linked list
    def printLinkedList(self, head):
        current = head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
odd = Node(1)
odd.next = Node(2)
odd.next.next = Node(3)
odd.next.next.next = Node(4)
odd.next.next.next.next = Node(5)

sol = Solution()
print("Original Linked List:")
sol.printLinkedList(odd)

sol.rearrange(odd)

print("\nRearranged Linked List:")
sol.printLinkedList(odd)
