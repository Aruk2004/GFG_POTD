# Intersection of two sorted Linked lists

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def findIntersection(self, head1, head2):
        dummy = Node(0)
        tail = dummy

        while head1 and head2:
            if head1.data == head2.data:
                tail.next = head1
                tail = head1
                head1, head2 = head1.next, head2.next
            elif head1.data < head2.data:
                head1 = head1.next
            else:
                head2 = head2.next

        tail.next = None

        return dummy.next

# Example usage:
# Creating linked list 1: 1 -> 2 -> 3 -> 4
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.next = node2
node2.next = node3
node3.next = node4

head1 = node1

# Creating linked list 2: 2 -> 4 -> 6 -> 8
node2 = Node(2)
node4 = Node(4)
node6 = Node(6)
node8 = Node(8)

node2.next = node4
node4.next = node6
node6.next = node8

head2 = node2

# Creating an instance of Solution
solution = Solution()

# Finding the intersection of the two linked lists
intersection_head = solution.findIntersection(head1, head2)

# Printing the intersection linked list
current = intersection_head
while current:
    print(current.data, end=" ")
    current = current.next
