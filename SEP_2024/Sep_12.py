# Middle of a Linked List

class Solution:
    def getMiddle(self, head):
        l1 = []
        while head:
            l1.append(head.data)
            head = head.next
        return l1[len(l1) // 2]
