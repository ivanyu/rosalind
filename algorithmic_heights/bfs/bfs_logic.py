#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def bfs(graph, s):
    if len(graph) == 0:
        return []

    UNREACHEABLE = -1
    dist = [UNREACHEABLE for _ in graph]
    dist[s] = 0
    queue = [s]
    while queue:
        ui = queue.pop()
        for vi, v in enumerate(graph[ui]):
            if v <= 0 or dist[vi] != UNREACHEABLE:
                continue
            queue.insert(0, vi)
            dist[vi] = dist[ui] + 1
    return dist

if __name__ == "__main__":
    import unittest

    class BFSTestCase(unittest.TestCase):
        def test_empty_graph(self):
            graph = []
            self.assertSequenceEqual(bfs(graph, 0), [])

        def test_one_vertex_graph(self):
            graph = [[0]]
            self.assertSequenceEqual(bfs(graph, 0), [0])

        def test_fully_connected(self):
            n = 6
            graph = [[1 for _ in range(n)] for _ in range(n)]
            model = [1 for _ in range(n)]
            model[0] = 0
            self.assertSequenceEqual(bfs(graph, 0), model)

        def test_not_connected(self):
            n = 6
            graph = [[0 for _ in range(n)] for _ in range(n)]
            model = [-1 for _ in range(n)]
            model[0] = 0
            self.assertSequenceEqual(bfs(graph, 0), model)

        def test_source_isolated_by_direction(self):
            n = 6
            graph = [[1 for _ in range(n)] for _ in range(n)]
            for i in range(1, n):
                graph[0][i] = -1
            model = [-1 for _ in range(n)]
            model[0] = 0
            self.assertSequenceEqual(bfs(graph, 0), model)

        def test_mixed(self):
            n = 7
            graph = [
                [0, 1, 0, 0, 1, 0, 0],
                [-1, 1, 1, 1, 0, 0, 0],
                [0, -1, 0, 1, 0, 0, 0],
                [0, -1, -1, 0, 1, 0, 0],
                [-1, -1, 0, -1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, -1, 0],
            ]
            model = [0, 1, 2, 2, 1, -1, -1]
            self.assertSequenceEqual(bfs(graph, 0), model)

    unittest.main()
