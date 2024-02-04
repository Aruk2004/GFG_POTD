# Subtraction in Linked List

class Solution:
    def subLinkedList(self, l1, l2): 
        # Code here
        # return head of difference list
        s=0
        while l1 :
            s=s*10 + l1.data
            l1=l1.next
        s2=0
        while l2 :
            s2=s2*10 + l2.data
            l2=l2.next
        res=Node(abs(s-s2))
        return res

  # Example linked list definition
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# Example usage
if __name__ == "__main__":
    # Creating linked list 1: 123 (1 -> 2 -> 3)
    l1 = Node(1)
    l1.next = Node(2)
    l1.next.next = Node(3)

    # Creating linked list 2: 456 (4 -> 5 -> 6)
    l2 = Node(4)
    l2.next = Node(5)
    l2.next.next = Node(6)

    # Creating an instance of the Solution class
    solution = Solution()

    # Calling the subLinkedList method to get the result
    result_head = solution.subLinkedList(l1, l2)

    # Printing the result linked list
    while result_head:
        print(result_head.data, end=" -> ")
        result_head = result_head.next
    print("None")
