from typing import List

def generateGraph(num_nodes: int, edges: List[tuple], directed: bool = False) -> List[List[int]]:
    """
    Generate a graph as an adjacency list.
    
    :param num_nodes: Number of nodes in the graph (0 to num_nodes-1).
    :param edges: List of edges where each edge is a tuple (u, v).
    :param directed: If True, creates a directed graph; otherwise, undirected.
    :return: Adjacency list representing the graph.
    """
    # Initialize the adjacency list
    graph = [[] for _ in range(num_nodes)]
    
    # Add edges to the graph
    for u, v in edges:
        graph[u].append(v)  # Add the edge u -> v
        if not directed:
            graph[v].append(u)  # Add the edge v -> u (if undirected)
    
    return graph