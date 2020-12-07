import sys

def add_edge(graph, vertex1, vertex2):
    if vertex1 in graph:
        graph[vertex1].append(vertex2)
    else:
        graph[vertex1] = vertex2

def dfs(i, vertex, visited, ordering, graph):
    visited[vertex-1] = True
    for neighbour in graph[vertex]:
        if visited[neighbour-1] is False:
            dfs(i, neighbour, visited, ordering, graph)
    ordering.insert(0, vertex)
    return i - 1
    
def topsort(adj):
    num_of_nodes = len(graph)
    visited = [False] * num_of_nodes
    ordering = []
    i = num_of_nodes - 1

    for vertex in graph:
        if visited[vertex-1] is False:
            i = dfs(i, vertex, visited, ordering, graph)
    return ordering

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    graph = {vertex: [] for vertex in range(1, n+1)}
    
    for _ in range(m):
        vert1, vert2 = map(int, sys.stdin.readline().split())
        add_edge(graph, vert1, vert2)
    in_order = (topsort(graph))

    for x in in_order:
        print(x, end=' ')