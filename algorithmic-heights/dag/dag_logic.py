#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from enum import Enum

class AcyclicityTester:
    class Colors(Enum):
        White = 1
        Gray = 2
        Black = 3

    def __init__(self, graph):
        self._graph = graph
        self._all_v = list(range(len(graph)))
        self._time = 0
        self._colors = [self.Colors.White for _ in self._all_v]
        self._d = [-1 for _ in self._all_v]
        self._f = [-1 for _ in self._all_v]

    def _dfs(self, u):
        self._colors[u] = self.Colors.Gray
        self._time += 1
        self._d[u] = self._time

        for v in self._all_v:
            if self._graph[u][v] == 0:
                continue

            if self._colors[v] == self.Colors.Gray:
                return False

            if self._colors[v] == self.Colors.White:
                r = self._dfs(v)
                if not r:
                    return False

        self._colors[u] = self.Colors.Black
        self._time += 1
        self._f[u] = self._time

        return True

    def test(self):
        if len(self._graph) <= 1:
            return True

        for v in self._all_v:
            if self._colors[v] != self.Colors.White:
                continue
            r = self._dfs(v)
            if not r:
                return False
        return True


if __name__ == "__main__":
    import unittest

    class AcyclicityTestCase(unittest.TestCase):
        def test_empty_graph(self):
            graph = []
            self.assertEqual(AcyclicityTester(graph).test(), True)

        def test_one_vertex_graph(self):
            graph = [[]]
            self.assertEqual(AcyclicityTester(graph).test(), True)

        def test_line(self):
            graph = [
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1],
                [0, 0, 0, 0],
            ]
            self.assertEqual(AcyclicityTester(graph).test(), True)

        def test_not_connected(self):
            n = 6
            graph = [[0 for i in range(n)] for _ in range(n)]
            self.assertEqual(AcyclicityTester(graph).test(), True)

        def test_simple_cycle(self):
            graph = [
                [0, 1, 0, 1],
                [0, 0, 1, 0],
                [0, 0, 0, 1],
                [1, 0, 0, 0],
            ]
            self.assertEqual(AcyclicityTester(graph).test(), False)

        def test_complex_cycle(self):
            graph = [
                [0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 1],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 1, 0],
            ]
            self.assertEqual(AcyclicityTester(graph).test(), False)

        def test_separated_cycle(self):
            graph = [
                [0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 1, 0],
            ]
            self.assertEqual(AcyclicityTester(graph).test(), False)

        def test_acyclic_reversed_order(self):
            graph = [
                [0, 0, 0, 0],
                [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
            ]
            self.assertEqual(AcyclicityTester(graph).test(), True)

        def test_acyclic_diamond(self):
            graph = [
                [0, 1, 1, 0],
                [0, 0, 0, 1],
                [0, 0, 0, 1],
                [0, 0, 0, 0],
            ]
            self.assertEqual(AcyclicityTester(graph).test(), True)

    unittest.main()
