# Bottom View of Binary Tree

class Solution:
    def bottomView(self, root):
        if not root:
            return []
        
        # Dictionary to store the bottom view of the binary tree
        hd_node_map = {}
        
        # Queue to perform level-order traversal
        # Each element in the queue is a tuple (node, horizontal_distance)
        queue = deque([(root, 0)])
        
        while queue:
            node, hd = queue.popleft()
            
            # Update the dictionary with the current node at the horizontal distance
            hd_node_map[hd] = node.data
            
            # If there's a left child, add it to the queue with horizontal distance hd-1
            if node.left:
                queue.append((node.left, hd - 1))
            
            # If there's a right child, add it to the queue with horizontal distance hd+1
            if node.right:
                queue.append((node.right, hd + 1))
        
        # Extract the values from the dictionary, sorted by their keys (horizontal distances)
        bottom_view = [hd_node_map[hd] for hd in sorted(hd_node_map)]
        
        return bottom_view
