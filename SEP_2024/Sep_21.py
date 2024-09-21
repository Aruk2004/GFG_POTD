#Clone a linked list with next and random pointer

class Solution:
    def copyList(self, head):
        
        if not head:
            return None
        d = {}
        curr = head
        
        while curr:
            d[curr] = Node(curr.data)
            curr = curr.next
        curr = head
        while curr:
            d[curr].next = d.get(curr.next)
            d[curr].random = d.get(curr.random)
            curr = curr.next
            
        return d[head]
