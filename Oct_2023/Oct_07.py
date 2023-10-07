# Pairwise swap elements of a linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def pairWiseSwap(self, head):
        if not head or not head.next:
            return head

        itr = head
        head = head.next
        itr.next = head.next
        head.next = itr

        while itr:
            curr = itr.next
            if curr and curr.next:
                itr.next = curr.next
                curr.next = itr.next.next
                itr.next.next = curr
            else:
                break
            itr = itr.next.next

        return head

    # Utility function to print the linked list
    def printLinkedList(self, head):
        current = head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

sol = Solution()
print("Original Linked List:")
sol.printLinkedList(head)

head = sol.pairWiseSwap(head)

print("\nPairwise Swapped Linked List:")
sol.printLinkedList(head)
