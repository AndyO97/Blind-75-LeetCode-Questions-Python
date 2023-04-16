# Clone Graph

# Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.
# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

# class Node {
#     public int val;
#     public List<Node> neighbors;
# }


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # Check that node is not None
        if node is None:
            return None
        
        # Breadth-first search (Beter results for Leetcode)

        # Dequeing the node for Popping Items Efficiently (popleft())
        # deque provides an O(1) time complexity for append and pop operations as compared to a list that provides O(n) time complexity.
        q = collections.deque([node])
        
        map = {node: Node(node.val)}

        while q:
            u = q.popleft()
            for v in u.neighbors:
                if v not in map:
                    map[v] = Node(v.val)
                    q.append(v)
                map[u].neighbors.append(map[v])

        return map[node]

    # Depth-first search

    #     if node in self.map:
    #         return self.map[node]

    #     newNode = Node(node.val, [])
    #     self.map[node] = newNode

    #     for neighbor in node.neighbors:
    #         self.map[node].neighbors.append(self.cloneGraph(neighbor))

    #     return newNode

    # map = {}