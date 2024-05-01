# Arrange Consonants and Vowels

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class Solution:
    def arrangeCV(self, head):
        vowels = ["a", "e", "i", "o", "u"]
        dummy = Node(-1)
        dummy.next = head
        vow = dummy
        prev = dummy
        curr = head 

        while curr:
            if curr.data in vowels:
                del_node = curr
                prev.next = curr.next
                curr = prev.next
                nxt = vow.next
                vow.next = del_node
                del_node.next = nxt
                vow = del_node
                if vow.next == curr:
                    prev = vow
            else:
                curr = curr.next
                prev = prev.next 
        return dummy.next

# Example usage:
# Create a linked list: c -> a -> t -> e -> r
head = Node("c")
head.next = Node("a")
head.next.next = Node("t")
head.next.next.next = Node("e")
head.next.next.next.next = Node("r")

sol = Solution()
new_head = sol.arrangeCV(head)

# Print the updated linked list
current = new_head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")  # Indicates the end of the list
