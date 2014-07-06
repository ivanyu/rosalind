#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def _dfs(graph, s_orig, s, len_rest, visited):
    if s == s_orig:
        # Prevent self intersections
        if len_rest == 0:
            return True
        elif len_rest < 4:
            return None  # Cut-off

    if s in visited:
        return None

    visited.add(s)
    for v in range(len(graph)):
        if graph[s][v] != 0:
            r = _dfs(graph, s_orig, v, len_rest - 1, visited)
            if r is None:
                continue
            if r:
                return True
    return False


def detect_sq_cycles(graph):
    if len(graph) < 4:
        return False

    for v in range(len(graph)):
        visited = set()
        r = _dfs(graph, v, v, 4, visited)
        if r:
            return True
    return False


if __name__ == "__main__":
    import unittest

    class SqCyclesDetectionTestCase(unittest.TestCase):
        def test_empty_graph(self):
            graph = []
            self.assertEqual(detect_sq_cycles(graph), False)

        def test_one_vertex_graph(self):
            graph = [[]]
            self.assertEqual(detect_sq_cycles(graph), False)

        def test_line(self):
            graph = [
                [0, 1, 0, 0],
                [1, 0, 1, 0],
                [0, 1, 0, 1],
                [0, 0, 1, 0],
            ]
            self.assertEqual(detect_sq_cycles(graph), False)

        def test_not_connected(self):
            n = 6
            graph = [[0 for i in range(n)] for _ in range(n)]
            self.assertEqual(detect_sq_cycles(graph), False)

        def test_simple_cycle(self):
            graph = [
                [0, 1, 0, 1],
                [1, 0, 1, 0],
                [0, 1, 0, 1],
                [1, 0, 1, 0],
            ]
            self.assertEqual(detect_sq_cycles(graph), True)

        def test_complex_cycle(self):
            graph = [
                [0, 1, 0, 1],
                [1, 0, 1, 1],
                [0, 1, 1, 1],
                [1, 0, 1, 0],
            ]
            self.assertEqual(detect_sq_cycles(graph), True)

        def test_separated_cycle(self):
            graph = [
                [0, 1, 0, 1, 0, 0],
                [1, 0, 1, 0, 0, 0],
                [0, 1, 0, 1, 0, 0],
                [1, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1, 0],
            ]
            self.assertEqual(detect_sq_cycles(graph), True)

        def test_no_square(self):
            graph = [
                [0, 1, 1, 0, 0, 0],
                [1, 0, 1, 0, 0, 0],
                [1, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 1],
                [0, 0, 0, 1, 0, 1],
                [0, 0, 0, 1, 1, 0],
            ]
            self.assertEqual(detect_sq_cycles(graph), False)

    unittest.main()
