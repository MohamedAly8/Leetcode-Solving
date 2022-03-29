"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        
        marked = {}
        
        if not node:
            return None
        
        def dfs(node):
            if node in marked:
                # Already marked
                return marked[node]
            
            # New node
        
            
            # Create clone
            copy = Node(node.val)
            
            marked[node] = copy
            
            for child in node.neighbors:
                copy.neighbors.append(dfs(child))
                
            return copy
        
        return dfs(node)
            
        
        
        