#Remove duplicates from a link list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def removeDuplicates(self, head):
        curr = head
        while curr:
            next_node = curr.next
            while next_node and next_node.data == curr.data:
                next_node = next_node.next
            curr.next = next_node
            curr = curr.next
        return head

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    curr = head
    for val in values[1:]:
        curr.next = Node(val)
        curr = curr.next
    return head

# Helper function to print linked list
def print_linked_list(head):
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")

# Example usage
values = [1, 2, 2, 3, 3, 3, 4, 5, 5]
head = create_linked_list(values)

print("Original Linked List:")
print_linked_list(head)

solution = Solution()
new_head = solution.removeDuplicates(head)

print("\nLinked List after Removing Duplicates:")
print_linked_list(new_head)
