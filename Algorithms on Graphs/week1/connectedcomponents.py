#Uses python3

import sys

def add_edge(graph, vertex1, vertex2):
    edges = (vertex1, vertex2)
    (v1, v2) = (edges)
    if v1 in graph:
        if v2 not in graph[v1]:
            graph[v1].append(v2)
            graph[v2].append(v1)
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)

def explore(graph, vert, cc_val=None, visited=None):
    if visited is None:
        visited = []
    if cc_val is None:
        cc_val = 0
    cc_num = cc_val
    visited.append(vert)
    for neighbour in graph[vert]:
        if neighbour not in visited:
            explore(graph, neighbour, cc_num, visited)
    return visited

def number_of_components(graph, visit=None):
    if visit is None:
        visit = []
    cc = 0
    for vertex in graph.keys():
        if vertex not in visit:
            explore(graph, vertex, cc, visit)
            cc += 1
    return cc

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    graph = {vertex: [] for vertex in range(1, n+1)}

    for _ in range(m):
        vert1, vert2 = map(int, sys.stdin.readline().split())
        add_edge(graph, vert1, vert2)
    
    print(number_of_components(graph))