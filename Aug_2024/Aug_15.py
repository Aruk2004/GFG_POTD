# Add 1 to a Linked List Number

class Solution:
    def addOne(self, head):
        number = 0
        while head:number, head = number * 10 + head.data, head.next
        return Node(number + 1)
