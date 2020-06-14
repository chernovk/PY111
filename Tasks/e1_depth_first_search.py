from typing import Hashable, List
import networkx as nx
from collections import deque


def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an depth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node of search
    :return: list of nodes in the visited order
    """
    is_visited = {node: False for node in g}
    visited_nodes = []
    d = deque([start_node])
    while True:
        if not d:
            break
        current_node = d.pop()
        is_visited[current_node] = True
        if current_node not in visited_nodes:
            visited_nodes.append(current_node)
        for node in g.neighbors(current_node):
            if not is_visited[node] and node not in d:
                d.append(node)
    return visited_nodes

