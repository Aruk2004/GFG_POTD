# Count Pairs whose sum is equal to X

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def countPair(self, head1, head2, n1, n2, x):
        values_set = set()
        count = 0

        # Store values from linked list 1 in the set
        while head1:
            values_set.add(head1.data)
            head1 = head1.next

        # Check for pairs in linked list 2 that sum up to x
        while head2:
            if x - head2.data in values_set:
                count += 1
            head2 = head2.next

        return count

# Create linked list 1: 1 -> 2 -> 3
head1 = Node(1)
head1.next = Node(2)
head1.next.next = Node(3)

# Create linked list 2: 4 -> 5 -> 6
head2 = Node(4)
head2.next = Node(5)
head2.next.next = Node(6)

n1 = 3  # Length of linked list 1
n2 = 3  # Length of linked list 2
x = 7   # Target sum

solution = Solution()
result = solution.countPair(head1, head2, n1, n2, x)
print("Number of pairs with sum", x, ":", result)
