#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum


class TopoligicalSorter:
    class Colors(Enum):
        White = 0
        Gray = 1
        Black = 2

    def __init__(self, graph):
        self._g = graph
        self._colors = [self.Colors.White for _ in range(len(self._g))]
        self._f = [-1 for _ in range(len(self._g))]
        self._time = 0
        self._all_v = list(range(len(self._g)))

    def _dfs(self, s):
        self._colors[s] = self.Colors.Gray

        for v in self._all_v:
            if self._g[s][v] != 0 and self._colors[v] == self.Colors.White:
                self._dfs(v)

        self._f[s] = self._time
        self._time += 1
        self._colors[s] = self.Colors.Black

    def sort(self):
        if len(self._g) <= 1:
            return self._all_v

        for v in self._all_v:
            if self._colors[v] == self.Colors.White:
                self._dfs(v)

        pre_result = sorted(enumerate(self._f),
                            key=lambda x: x[1],
                            reverse=True)
        result = [x[0] for x in pre_result]
        return result


if __name__ == "__main__":
    import unittest

    class TopologicalSortTestCase(unittest.TestCase):
        def test_empty_graph(self):
            graph = []
            model = []
            self.assertSequenceEqual(TopoligicalSorter(graph).sort(), model)

        def test_one_vertex_graph(self):
            graph = [[]]
            model = [0]
            self.assertSequenceEqual(TopoligicalSorter(graph).sort(), model)

        def test_line(self):
            graph = [
                [0, 1, 0, 0],
                [1, 0, 1, 0],
                [0, 1, 0, 1],
                [0, 0, 1, 0],
            ]
            model = [0, 1, 2, 3]
            self.assertSequenceEqual(TopoligicalSorter(graph).sort(), model)

        def test_not_connected(self):
            n = 6
            graph = [[0 for i in range(n)] for _ in range(n)]
            model = list(reversed(range(n)))
            self.assertSequenceEqual(TopoligicalSorter(graph).sort(), model)

        def test_mixed(self):
            graph = [
                [0, 1, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 1, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 0],
            ]
            model = [0, 2, 1, 5, 3, 6, 4, 7]
            self.assertSequenceEqual(TopoligicalSorter(graph).sort(), model)

    unittest.main()
