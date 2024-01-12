# Insertion Sort for Singly Linked List

# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None

class Solution:
    def insertionSort(self, head):
        if not head or not head.next:
            return head

        dummy = Node(0)
        dummy.next = head
        current = head.next
        prev_sorted = head

        while current:
            if current.data < prev_sorted.data:
                prev_sorted.next = current.next
                prev = dummy

                while prev.next and prev.next.data < current.data:
                    prev = prev.next

                current.next = prev.next
                prev.next = current

                current = prev_sorted.next
            else:
                prev_sorted = current
                current = current.next

        return dummy.next

# Helper function to print the linked list
def printList(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()

# Example usage:
if __name__ == "__main__":
    # Create a linked list
    head = Node(30)
    head.next = Node(23)
    head.next.next = Node(28)
    head.next.next.next = Node(30)
    head.next.next.next.next = Node(11)
    head.next.next.next.next.next = Node(14)
    head.next.next.next.next.next.next = Node(19)
    head.next.next.next.next.next.next.next = Node(16)
    head.next.next.next.next.next.next.next.next = Node(21)
    head.next.next.next.next.next.next.next.next.next = Node(25)

    # Print the original linked list
    print("Original Linked List:")
    printList(head)

    # Sort the linked list using insertion sort
    sol = Solution()
    sorted_head = sol.insertionSort(head)

    # Print the sorted linked list
    print("\nSorted Linked List:")
    printList(sorted_head)
