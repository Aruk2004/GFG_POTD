# Linked List that is Sorted Alternatingly

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def sort(self, head):
        if not head or not head.next:
            return head

        # Split the list into two halves
        mid = self.get_mid(head)
        left = head
        right = mid.next
        mid.next = None

        # Recursively sort the two halves
        left = self.sort(left)
        right = self.sort(right)

        # Merge the sorted halves
        return self.merge(left, right)

    def get_mid(self, head):
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, left, right):
        dummy = Node(0)
        curr = dummy

        while left and right:
            if left.data < right.data:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next

        if left:
            curr.next = left
        elif right:
            curr.next = right

        return dummy.next

# Example usage
if __name__ == "__main__":
    # Create a linked list: 5 -> 2 -> 9 -> 1 -> 3
    head = Node(5)
    head.next = Node(2)
    head.next.next = Node(9)
    head.next.next.next = Node(1)
    head.next.next.next.next = Node(3)

    solution = Solution()
    sorted_head = solution.sort(head)

    # Print the sorted linked list
    while sorted_head:
        print(sorted_head.data, end=" -> ")
        sorted_head = sorted_head.next
    print("None")
