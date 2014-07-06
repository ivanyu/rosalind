#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def degrees(graph):
    result = [sum(r) for r in graph]
    return result

if __name__ == "__main__":
    import unittest

    class DegreesTestCase(unittest.TestCase):
        def test_empty_graph(self):
            graph = []
            self.assertSequenceEqual(degrees(graph), [])

        def test_one_vertex_graph(self):
            graph = [[0]]
            self.assertSequenceEqual(degrees(graph), [0])

        def test_fully_connected(self):
            n = 6
            graph = [[1 for _ in range(n)] for _ in range(n)]
            model = [n for _ in range(n)]
            self.assertSequenceEqual(degrees(graph), model)

        def test_not_connected(self):
            n = 6
            graph = [[0 for _ in range(n)] for _ in range(n)]
            model = [0 for _ in range(n)]
            self.assertSequenceEqual(degrees(graph), model)

        def test_mixed(self):
            n = 7
            graph = [[0 for _ in range(n)] for _ in range(n)]
            graph[0][1] = 1
            graph[1][0] = 1
            graph[3][4] = 1
            graph[4][3] = 1
            graph[5][1] = 1
            graph[1][5] = 1
            graph[0][6] = 1
            graph[6][0] = 1
            model = [2, 2, 0, 1, 1, 1, 1]
            self.assertSequenceEqual(degrees(graph), model)

    unittest.main()
