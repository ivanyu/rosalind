#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import heapq


def dijkstra(graph, s):
    if len(graph) == 0:
        return []

    INF = -1

    all_v = [i for i in range(len(graph))]

    dist = [INF for _ in graph]
    dist[s] = 0
    visited = [False for _ in graph]

    while not all(visited):
        not_visited = [e[0] for e in enumerate(visited) if not e[1]]
        minimum = not_visited[0]
        for v in not_visited:
            if (dist[minimum] == INF and dist[v] != INF or
                    dist[minimum] != INF and dist[v] != INF
                    and dist[v] < dist[minimum]):
                minimum = v
        curr_n = minimum
        if dist[curr_n] != INF:
            for u in all_v:
                if graph[curr_n][u] > 0 and not visited[u]:
                    new_dist = dist[curr_n] + graph[curr_n][u]
                    if dist[u] == INF or dist[u] > new_dist:
                        dist[u] = new_dist
        visited[curr_n] = True
    return dist

if __name__ == "__main__":
    import unittest

    class DijkstraTestCase(unittest.TestCase):
        def test_empty_graph(self):
            graph = []
            self.assertSequenceEqual(dijkstra(graph, 0), [])

        def test_one_vertex_graph(self):
            graph = [[0]]
            self.assertSequenceEqual(dijkstra(graph, 0), [0])

        def test_line(self):
            graph=[
                [0, 1, 0, 0],
                [0, 0, 2, 0],
                [0, 0, 0, 3],
                [0, 0, 0, 0],
            ]
            self.assertSequenceEqual(dijkstra(graph, 0), [0, 1, 3, 6])

        def test_not_connected(self):
            n = 6
            graph = [[0 for _ in range(n)] for _ in range(n)]
            model = [-1 for _ in range(n)]
            model[0] = 0
            self.assertSequenceEqual(dijkstra(graph, 0), model)

        def test_first_isolated(self):
            graph=[
                [0, 0, 0, 0],
                [1, 0, 0, 0],
                [1, 0, 0, 0],
                [1, 0, 0, 0],
            ]
            self.assertSequenceEqual(dijkstra(graph, 0), [0, -1, -1, -1])

        def test_mixed1(self):
            graph = [
                [0, 3, 0, 0, 10, 0, 0],
                [0, 0, 5, 1,  0, 0, 0],
                [0, 0, 0, 0,  1, 1, 0],
                [0, 0, 0, 0,  4, 0, 0],
                [0, 0, 0, 0,  0, 2, 0],
                [0, 0, 0, 0,  0, 0, 0],
                [1, 0, 0, 0,  0, 0, 0],
            ]
            model = [0, 3, 8, 4, 8, 9, -1]
            self.assertSequenceEqual(dijkstra(graph, 0), model)

        def test_mixed2(self):
            graph = [
                [ 0,  7,  9,  0, 0, 14],
                [ 7,  0, 10, 15, 0,  0],
                [ 9, 10,  0, 11, 0,  2],
                [ 0, 15, 11,  0, 6,  0],
                [ 0,  0,  0,  6, 0,  9],
                [14,  0,  2,  0, 9,  0],
            ]
            model = [0, 7, 9, 20, 20, 11]
            self.assertSequenceEqual(dijkstra(graph, 0), model)

        def test_isolated_pair(self):
            graph = [
                [0, 2, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 3, 0],
                [0, 0, 0, 0],
            ]
            model = [0, 2, -1, -1]
            self.assertSequenceEqual(dijkstra(graph, 0), model)

    unittest.main()
