#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def cc(graph):
    def _dfs_traversal(graph, t, visited):
        for v in graph[t]:
            if v not in visited:
                visited.add(v)
                _dfs_traversal(graph, v, visited)

    visited = set()
    cnt = 0
    for v in range(len(graph)):
        if v in visited:
            continue
        _dfs_traversal(graph, v, visited)
        cnt += 1
    return cnt


if __name__ == "__main__":
    import unittest

    class ConnectedComponentsTestCase(unittest.TestCase):
        def test_empty_graph(self):
            graph = []
            self.assertEqual(cc(graph), 0)

        def test_one_vertex_graph(self):
            graph = [[]]
            self.assertEqual(cc(graph), 1)

        def test_line(self):
            graph = [
                [1],
                [0, 2],
                [2, 3],
                [],
            ]
            self.assertEqual(cc(graph), 1)

        def test_not_connected(self):
            n = 6
            graph = [[] for _ in range(n)]
            self.assertEqual(cc(graph), 6)

        def test_big_and_one_vertex(self):
            graph = [
                [1, 2],
                [0, 2],
                [0, 1],
                []
            ]
            self.assertEqual(cc(graph), 2)

    unittest.main()
