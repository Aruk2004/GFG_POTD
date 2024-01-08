# Merge 2 sorted linked list in reverse order

class Solution:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def reverseList(self, curr):
        if not curr or not curr.next:
            return curr
        res = self.reverseList(curr.next)
        curr.next.next = curr
        curr.next = None
        return res

    def mergeResult(self, node1, node2):
        if not node1:
            return self.reverseList(node2)
        if not node2:
            return self.reverseList(node1)

        curr = self.Node(0)
        head = curr

        while node1 and node2:
            if node1.data < node2.data:
                curr.next = node1
                node1 = node1.next
            else:
                curr.next = node2
                node2 = node2.next
            curr = curr.next

        while node1:
            curr.next = node1
            node1 = node1.next
            curr = curr.next

        while node2:
            curr.next = node2
            node2 = node2.next
            curr = curr.next

        head = head.next
        return self.reverseList(head)

# Example usage:
# Create an instance of the Solution class
sol = Solution()

# Create linked list nodes (replace with your actual node creation logic)
node1 = sol.Node(1)
node1.next = sol.Node(3)
node1.next.next = sol.Node(5)

node2 = sol.Node(2)
node2.next = sol.Node(4)
node2.next.next = sol.Node(6)

# Call the mergeResult function with specific linked list nodes
result_head = sol.mergeResult(node1, node2)

# Print the result (replace with your actual result processing logic)
while result_head:
    print(result_head.data, end=" ")
    result_head = result_head.next
