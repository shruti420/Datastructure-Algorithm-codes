#Uses python3

import sys


DISTANCE = 0
VERTEX = 1
INFINITY = 10**5


def add_edge(graph, vert1, vert2, weight):
    """Build directed graph with edge weights.
    This directed graph may also contain negative weights.
    """

    weighted_edge = [vert2, weight]
    if vert1 in graph:
        graph[vert1].append(weighted_edge)
    else:
        graph[vert1] = weighted_edge

def negative_cycle(graph, start):
    """Implement Belman-Ford algorithm
    Will also detect negative cycles.
    Parameters
    ----------
    graph: dictionary
        directed graph with edge weights which may be negative
    Returns
    -------
    1: int
        Return 1 if graph contains a negative cycle
    0: int
        Return 0 if graph does not contain a negative cycle
    """

    # initialise storages
    dist = [INFINITY for i in range((len(graph)+1))]
    prev = [None for i in range((len(graph)+1))]

    dist[start] = 0
    prev[start] = start
    graph_length = len(graph)

    # relax edges
    for i in range(graph_length):
        for key_node in graph:
            for neighbour_node in graph[key_node]:
                if neighbour_node:
                    nb_vert, nb_weight = neighbour_node
                    if dist[nb_vert] > dist[key_node] + nb_weight:
                        dist[nb_vert] = dist[key_node] + nb_weight
                        prev[nb_vert] = key_node

    # check for negative cycles
    for key_node in graph:
        for neighbour_node in graph[key_node]:
            if neighbour_node:
                nb_vert, nb_weight = neighbour_node
                if dist[nb_vert] > dist[key_node] + nb_weight:
                    return 1
    return 0


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    graph = {vertex: [] for vertex in range(1, n+1)}
    for _ in range(m):
        vert1, vert2, weight = map(int, sys.stdin.readline().split())
        add_edge(graph, vert1, vert2, weight)
    print(negative_cycle(graph, 1))