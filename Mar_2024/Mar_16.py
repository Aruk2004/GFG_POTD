# Delete without head pointer

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def deleteNode(self, del_node):
        if not del_node or not del_node.next:
            return

        next_node = del_node.next
        del_node.data = next_node.data
        del_node.next = next_node.next
        del next_node
