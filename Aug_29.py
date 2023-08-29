#Delete nodes having greater value on right

class Solution:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def solve(self, curr):
        if not curr:
            return curr

        last = self.solve(curr.next)

        if last:
            if last.data <= curr.data:
                curr.next = last
            else:
                return last
        else:
            curr.next = last

        return curr

    def compute(self, head):
        return self.solve(head)

# Helper function to print linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Example usage
if __name__ == "__main__":
    s = Solution()

    # Creating a linked list: 3 -> 1 -> 4 -> 2
    head = s.Node(3)
    head.next = s.Node(1)
    head.next.next = s.Node(4)
    head.next.next.next = s.Node(2)

    print("Original linked list:")
    print_linked_list(head)

    # Calling the compute method to rearrange the linked list
    new_head = s.compute(head)

    print("Rearranged linked list:")
    print_linked_list(new_head)
