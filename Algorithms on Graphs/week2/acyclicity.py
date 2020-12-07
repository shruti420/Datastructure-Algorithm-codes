#Uses python3

import sys


def add_edge(graph, vertex1, vertex2):
    if vertex1 in graph:
        graph[vertex1].append(vertex2)
    else:
        graph[vertex1] = [vertex2]

def pre_visit(vertex, previsit):
    previsit.append(vertex)


def post_visit(vertex, postvisit):
    postvisit.append(vertex)


def explore(graph, vertex, previsit=None, postvisit=None, visited=None):
    if visited is None:
        visited = []

    if previsit is None:
        previsit = []

    if postvisit is None:
        postvisit = []

    visited.append(vertex)
    pre_visit(vertex, previsit)
    for neighbour in graph[vertex]:
        if neighbour in previsit and neighbour not in postvisit:
            return 1
        if neighbour not in visited:
            cycle_found = explore(graph, neighbour, previsit, postvisit, visited)
            if cycle_found:
                return 1
    post_visit(vertex, postvisit)
    return 0

def acyclic(graph):
    visited = []
    previsit = []
    postvisit = []

    for vertex in graph.keys():
        if vertex not in visited:
            cycle_exists = explore(graph, vertex, previsit, postvisit, visited)
            if cycle_exists:
                return 1
    return 0

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    graph = {vertex: [] for vertex in range(1, n+1)}

    for _ in range(m):
        vert1, vert2 = map(int, sys.stdin.readline().split())
        add_edge(graph, vert1, vert2)
    
    print(acyclic(graph))