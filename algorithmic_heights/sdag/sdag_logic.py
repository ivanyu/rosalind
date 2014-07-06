#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Linearizer:
    def __init__(self, graph, s):
        self._cur_post_mark = 0
        self._graph = graph
        self._s = s
        self._post_marks = [-1] * len(graph)
        self._visited = [False] * len(graph)

    def _linearize(self, t):
        for v, w in self._graph[t]:
            if not self._visited[v]:
                self._visited[v] = True
                self._linearize(v)
        self._post_marks[t] = self._cur_post_mark
        self._cur_post_mark += 1

    def linearize(self):
        self._linearize(self._s)
        return list(sorted(
            enumerate(self._post_marks), key=lambda x: x[1], reverse=True))


def shortest_paths(graph, s):
    if len(graph) == 0:
        return []

    lin = Linearizer(graph, 0)
    visit_order = lin.linearize()

    dist = [None] * len(graph)
    dist[s] = 0

    for u, mark in visit_order:
        if mark == -1:
            continue
        for v, w in graph[u]:
            new_dist = dist[u] + w
            if dist[v] is None or dist[v] > new_dist:
                dist[v] = new_dist
    return dist

if __name__ == "__main__":
    import unittest

    class ShortestPathsInDAGTestCase(unittest.TestCase):
        def test_empty_graph(self):
            graph = []
            self.assertEqual(shortest_paths(graph, 0), [])

        def test_one_vertex_graph(self):
            graph = [[]]
            self.assertEqual(shortest_paths(graph, 0), [0])

        def test_line(self):
            graph = [
                [(1, 1)],
                [(2, 2)],
                [(3, 3)],
                [],
            ]
            self.assertEqual(shortest_paths(graph, 0), [0, 1, 3, 6])

        def test_not_connected(self):
            n = 6
            graph = [[] for _ in range(n)]
            model = [0] + [None] * (n - 1)
            self.assertEqual(shortest_paths(graph, 0), model)

        def test_first_isolated(self):
            graph = [
                [],
                [(0, 1)],
                [(0, 1)],
                [(0, 1)],
            ]
            model = [0, None, None, None]
            self.assertEqual(shortest_paths(graph, 0), model)

        def test_mixed(self):
            graph = [
                [(1, 1), (2, 2)],
                [(3, 4), (5, 5)],
                [(5, 6)],
                [(4, -4), (6, -1)],
                [(7, -5)],
                [(6, 2)],
                [(7, -7)],
                [],
                [(9, 2)],
                [],
            ]
            model = [0, 1, 2, 5, 1, 6, 4, -4, None, None]
            self.assertEqual(shortest_paths(graph, 0), model)

    unittest.main()
