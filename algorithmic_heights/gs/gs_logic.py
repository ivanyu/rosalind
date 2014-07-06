#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum


class GeneralSinkFinder:
    class Colors(Enum):
        White = 0
        Gray = 1
        Black = 2

    def __init__(self, graph):
        self._g = graph
        self._f = [-1 for _ in range(len(self._g))]
        self._time = 0
        self._all_v = list(range(len(self._g)))

    def _dfs(self, colors, s):
        colors[s] = self.Colors.Gray

        for v in self._all_v:
            if self._g[s][v] != 0 and colors[v] == self.Colors.White:
                self._dfs(colors, v)

        self._f[s] = self._time
        self._time += 1
        colors[s] = self.Colors.Black

    def find(self):
        if len(self._g) == 0:
            return None
        if len(self._g) == 1:
            return 0

        colors = [self.Colors.White for _ in range(len(self._g))]
        for v in self._all_v:
            if colors[v] == self.Colors.White:
                self._dfs(colors, v)

        sorted_by_f = sorted(enumerate(self._f),
                             key=lambda x: x[1],
                             reverse=True)
        sorted_by_f = [x[0] for x in sorted_by_f]

        potential_s = sorted_by_f[0]
        colors = [self.Colors.White for _ in range(len(self._g))]
        self._dfs(colors, potential_s)
        if any([x == self.Colors.White for x in colors]):
            return None
        else:
            return potential_s


if __name__ == "__main__":
    import unittest

    class GeneralSinkFinderTestCase(unittest.TestCase):
        def test_empty_graph(self):
            graph = []
            self.assertEqual(GeneralSinkFinder(graph).find(), None)

        def test_one_vertex_graph(self):
            graph = [[]]
            self.assertEqual(GeneralSinkFinder(graph).find(), 0)

        def test_line(self):
            graph = [
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1],
                [0, 0, 0, 0],
            ]
            self.assertEqual(GeneralSinkFinder(graph).find(), 0)

        def test_not_connected(self):
            n = 6
            graph = [[0 for _ in range(n)] for _ in range(n)]
            self.assertEqual(GeneralSinkFinder(graph).find(), None)

        def test_one_src(self):
            graph = [
                [0, 1, 0, 0],
                [0, 0, 1, 1],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ]
            self.assertEqual(GeneralSinkFinder(graph).find(), 0)

        def test_no_src(self):
            graph = [
                [0, 1, 0],
                [0, 0, 0],
                [0, 1, 0],
            ]
            self.assertEqual(GeneralSinkFinder(graph).find(), None)

    unittest.main()
