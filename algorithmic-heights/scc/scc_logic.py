#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum


class SCCCounter:
    class Colors(Enum):
        White = 0
        Gray = 1
        Black = 2

    def __init__(self, graph):
        self._g = graph
        self._f = [-1 for _ in range(len(self._g))]
        self._time = 0
        self._all_v = list(range(len(self._g)))

        self._ig = [[0 for _ in self._g] for _ in self._g]
        for r in range(len(self._g)):
            for c in range(r + 1, len(self._g)):
                self._ig[c][r] = self._g[r][c]
                self._ig[r][c] = self._g[c][r]

    def _dfs_first(self, colors, s):
        colors[s] = self.Colors.Gray

        for v in self._all_v:
            if self._g[s][v] != 0 and colors[v] == self.Colors.White:
                self._dfs_first(colors, v)

        self._f[s] = self._time
        self._time += 1
        colors[s] = self.Colors.Black

    def _dfs_second(self, colors, s):
        colors[s] = self.Colors.Gray

        for v in self._all_v:
            # Traversing through inverse graph!
            if self._ig[s][v] != 0 and colors[v] == self.Colors.White:
                self._dfs_second(colors, v)

        colors[s] = self.Colors.Black

    def count(self):
        if len(self._g) <= 1:
            return len(self._g)

        colors = [self.Colors.White for _ in range(len(self._g))]
        for v in self._all_v:
            if colors[v] == self.Colors.White:
                self._dfs_first(colors, v)

        sorted_by_f = sorted(enumerate(self._f),
                             key=lambda x: x[1],
                             reverse=True)
        sorted_by_f = [x[0] for x in sorted_by_f]

        cc_count = 0
        colors = [self.Colors.White for _ in range(len(self._g))]
        for v in sorted_by_f:
            if colors[v] == self.Colors.White:
                self._dfs_second(colors, v)
                cc_count += 1
        return cc_count


if __name__ == "__main__":
    import unittest

    class SCCCounterTestCase(unittest.TestCase):
        def test_empty_graph(self):
            graph = []
            self.assertEqual(SCCCounter(graph).count(), 0)

        def test_one_vertex_graph(self):
            graph = [[]]
            self.assertEqual(SCCCounter(graph).count(), 1)

        def test_line(self):
            graph = [
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1],
                [0, 0, 0, 0],
            ]
            self.assertEqual(SCCCounter(graph).count(), 4)

        def test_not_connected(self):
            n = 6
            graph = [[0 for _ in range(n)] for _ in range(n)]
            self.assertEqual(SCCCounter(graph).count(), n)

        def test_one_scc(self):
            graph = [
                [0, 1, 0],
                [0, 0, 1],
                [1, 0, 0],
            ]
            self.assertEqual(SCCCounter(graph).count(), 1)

        def test_separated_scc(self):
            graph = [
                [0, 0, 1, 0],
                [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 0, 0],
            ]
            self.assertEqual(SCCCounter(graph).count(), 2)

        def test_mixed(self):
            graph = [
                [0, 0, 1, 0, 0],
                [1, 0, 0, 0, 0],
                [0, 1, 0, 0, 1],
                [1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ]
            self.assertEqual(SCCCounter(graph).count(), 3)

    unittest.main()
