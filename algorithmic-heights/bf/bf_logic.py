#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def _collect_edges(graph):
    from itertools import product

    result = []
    for (u, v) in product(range(len(graph)), range(len(graph))):
        if graph[u][v] != 0:
            result.append((u, v))
    return result


def bf(graph, s):
    if len(graph) == 0:
        return []

    INF = None

    dist = [INF for _ in graph]
    dist[s] = 0

    edges = _collect_edges(graph)

    for _ in range(len(graph) - 1):
        for u, v in edges:
            if (dist[u] is not INF and
                    (dist[v] is INF or dist[v] > dist[u] + graph[u][v])):
                dist[v] = dist[u] + graph[u][v]
    return dist


if __name__ == "__main__":
    import unittest

    class BellmanFormTestCase(unittest.TestCase):
        def test_empty_graph(self):
            graph = []
            self.assertSequenceEqual(bf(graph, 0), [])

        def test_one_vertex_graph(self):
            graph = [[0]]
            self.assertSequenceEqual(bf(graph, 0), [0])

        def test_line(self):
            graph = [
                [0, 1, 0, 0],
                [0, 0, 2, 0],
                [0, 0, 0, 3],
                [0, 0, 0, 0],
            ]
            self.assertSequenceEqual(bf(graph, 0), [0, 1, 3, 6])

        def test_not_connected(self):
            n = 6
            graph = [[0 for _ in range(n)] for _ in range(n)]
            model = [None for _ in range(n)]
            model[0] = 0
            self.assertSequenceEqual(bf(graph, 0), model)

        def test_first_isolated(self):
            graph = [
                [0, 0, 0, 0],
                [1, 0, 0, 0],
                [1, 0, 0, 0],
                [1, 0, 0, 0],
            ]
            self.assertSequenceEqual(bf(graph, 0), [0, None, None, None])

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
            model = [0, 3, 8, 4, 8, 9, None]
            self.assertSequenceEqual(bf(graph, 0), model)

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
            self.assertSequenceEqual(bf(graph, 0), model)

        def test_isolated_pair(self):
            graph = [
                [0, 2, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 3, 0],
                [0, 0, 0, 0],
            ]
            model = [0, 2, None, None]
            self.assertSequenceEqual(bf(graph, 0), model)

        def test_shortest_path_with_negative_edge(self):
            graph = [
                [0, 1,  0, 2],
                [0, 0,  5, 0],
                [0, 0,  0, 0],
                [0, 0, -1, 0],
            ]
            model = [0, 1, 1, 2]
            self.assertSequenceEqual(bf(graph, 0), model)

    unittest.main()
