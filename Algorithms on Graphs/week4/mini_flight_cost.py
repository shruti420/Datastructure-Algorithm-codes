#Uses python3

import sys
import math
import heapq


VERTEX = 0
WEIGHT = 1
INFINITY = float("inf")


def add_edge(graph, vert1, vert2, weight):
    weighted_edge = [vert2, weight]
    if vert1 in graph:
        graph[vert1].append(weighted_edge)
    else:
        graph[vert1] = weighted_edge


def distance(graph, start, destination):
    dist = [[INFINITY, i] for i in range((len(graph)+1))]
    prev = [None for i in range((len(graph)+1))]
    dist[start][0] = 0
    prev[start] = start
    pq = []

    heapq.heappush(pq, dist[start])
    while pq:
        u_dist, u_vert = heapq.heappop(pq)
        if u_dist == dist[u_vert][0]:
            for v in graph[u_vert]:
                v_vert, w_uv = v
                if dist[v_vert][0] > dist[u_vert][0] + w_uv:
                    dist[v_vert][0] = dist[u_vert][0] + w_uv
                    heapq.heappush(pq, dist[v_vert])
                    prev[v_vert] = u_vert
    min_weight = dist[destination][0]

    if min_weight == INFINITY:
        return -1
    else:
        return min_weight


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    graph = {vertex: [] for vertex in range(1, n+1)}
    for _ in range(m):
        vert1, vert2, weight = map(int, sys.stdin.readline().split())
        add_edge(graph, vert1, vert2, weight)

    start, destination = map(int, sys.stdin.readline().split())
    print(distance(graph, start, destination))