# Insert in a Sorted List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def sortedInsert(self, head, data):
        new_node = Node(data)
        
        if not head or head.data >= data:
            new_node.next = head
            return new_node

        itr = head
        while itr.next and itr.next.data < data:
            itr = itr.next

        new_node.next = itr.next
        itr.next = new_node
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
head.next = Node(3)
head.next.next = Node(5)
head.next.next.next = Node(7)

sol = Solution()
print("Original Linked List:")
sol.printLinkedList(head)

data_to_insert = 4
head = sol.sortedInsert(head, data_to_insert)

print(f"\nInserted {data_to_insert} into Sorted Linked List:")
sol.printLinkedList(head)
