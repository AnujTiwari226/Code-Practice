from collections import deque
from typing import List
import Creation_of_graph as cg

class LearningBFS:
    def bfsOfGraph(self, adj: List[List[int]]) -> List[int]:
        queue = deque([0])
        visited = [0] * len(adj)
        bfs_result = []
        visited[0] = 1
        while queue:
            node = queue.popleft()
            bfs_result.append(node)
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor]  = 1
                    queue.append(neighbor)
        return bfs_result



if __name__ == '__main__':
    # Number of nodes
    num_nodes = 4

    # List of edges (undirected graph)
    edges = [(0, 1), (0, 2), (1, 3), (2, 3)]

    graph = cg.generateGraph(num_nodes=num_nodes, edges=edges)
    print('graph is : ', graph)
    lb = LearningBFS()
    print('BFS graph for above is -> ', lb.bfsOfGraph(graph))
