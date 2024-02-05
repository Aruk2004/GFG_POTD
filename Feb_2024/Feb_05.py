# Sorted insert for circular linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def sortedInsert(self, head, data):
        new_node = Node(data)

        if not head:
            new_node.next = new_node
            return new_node

        if data < head.data:
            temp = head
            while temp.next != head:
                temp = temp.next
            temp.next = new_node
            new_node.next = head
            return new_node

        current = head
        while current.next != head and current.next.data < data:
            current = current.next

        new_node.next = current.next
        current.next = new_node

        return head


# Example usage
if __name__ == "__main__":
    # Creating a circular linked list: 1 -> 2 -> 4 -> 1 (last node connects to the first)
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(4)

    n1.next = n2
    n2.next = n3
    n3.next = n1

    # Creating an instance of the Solution class
    solution = Solution()

    # Calling the sortedInsert method to insert a new node with data 3
    head = solution.sortedInsert(n1, 3)

    # Printing the modified circular linked list
    temp = head
    while True:
        print(temp.data, end=" ")
        temp = temp.next
        if temp == head:
            break
