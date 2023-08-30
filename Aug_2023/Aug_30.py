#Delete a node in a single link list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def deleteNode(self, head, x):
        to_delete = None
        
        if x == 1:
            to_delete = head
            head = head.next
        else:
            itr = head
            x -= 1  # Decrement x to account for 0-based indexing
            while x > 1:
                itr = itr.next
                x -= 1
                
            to_delete = itr.next
            itr.next = itr.next.next
        
        del to_delete  # Use 'del' to delete the reference
        return head

# Create a sample linked list: 1 -> 2 -> 3 -> 4 -> 5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

solution = Solution()
x = 3  # Position of the node to delete
new_head = solution.deleteNode(head, x)

# Print the linked list to verify the result
current = new_head
while current:
    print(current.value, end=" -> ")
    current = current.next
print("None")
