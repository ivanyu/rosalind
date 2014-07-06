#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def double_degrees(graph):
    result = []
    for v in graph:
        result.append(sum(len(graph[nbr]) for nbr in v))
    return result

if __name__ == "__main__":
    import unittest

    class DegreesTestCase(unittest.TestCase):
        def test_empty_graph(self):
            graph = []
            self.assertSequenceEqual(double_degrees(graph), [])

        def test_one_vertex_graph(self):
            graph = [[]]
            self.assertSequenceEqual(double_degrees(graph), [0])

        def test_fully_connected(self):
            n = 6
            graph = [[j for j in range(n) if j != i] for i in range(n)]
            model = [(n - 1) * (n - 1) for i in range(n)]
            self.assertSequenceEqual(double_degrees(graph), model)

        def test_not_connected(self):
            n = 6
            graph = [[] for _ in range(n)]
            model = [0 for _ in range(n)]
            self.assertSequenceEqual(double_degrees(graph), model)

        def test_mixed(self):
            n = 7
            graph = [
                [5],
                [2, 3, 4],
                [1, 4],
                [1],
                [1, 2],
                [0],
                [],
            ]
            model = [1, 5, 5, 3, 5, 1, 0]
            self.assertSequenceEqual(double_degrees(graph), model)

    unittest.main()
