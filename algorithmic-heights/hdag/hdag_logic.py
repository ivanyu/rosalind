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


def find_hamiltonian_path(graph):
    if len(graph) <= 1:
        return list(range(len(graph)))

    ts = TopoligicalSorter(graph)
    path = ts.sort()
    for u, v in zip([None] + path, path):
        if u is None:
            continue
        if graph[u][v] == 0:
            return None
    return path


if __name__ == "__main__":
    import unittest

    # There can't be any cycles in test cases (because of DAG).
    class HamiltonianPathFinderTestCase(unittest.TestCase):
        def check_path(self, graph, path):
            self.assertNotEqual(path, None)

            self.assertEqual(len(set(path)), len(graph))
            self.assertEqual(max(path), len(graph) - 1)
            self.assertEqual(min(path), 0)

            for u, v in zip([None] + path, path):
                if u is None:
                    continue
                self.assertNotEqual(graph[u][v], 0)

        def test_empty_graph(self):
            graph = []
            model = []
            self.assertSequenceEqual(find_hamiltonian_path(graph), [])

        def test_one_vertex_graph(self):
            graph = [[]]
            model = [0]
            self.assertSequenceEqual(find_hamiltonian_path(graph), [0])

        def test_line(self):
            graph = [
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1],
                [0, 0, 0, 0],
            ]
            self.check_path(graph, find_hamiltonian_path(graph))

        def test_not_connected(self):
            n = 6
            graph = [[0 for _ in range(n)] for _ in range(n)]
            self.assertEqual(find_hamiltonian_path(graph), None)

        def test_mixed_non_hamilton(self):
            graph = [
                [0, 1, 1, 0],
                [0, 0, 0, 1],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ]
            self.assertEqual(find_hamiltonian_path(graph), None)

        def test_square_hamilton_from_one(self):
            graph = [
                [0, 1, 1, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 1],
                [0, 1, 0, 0],
            ]
            self.check_path(graph, find_hamiltonian_path(graph))

        def test_square_non_hamilton(self):
            graph = [
                [0, 1, 1, 1],
                [0, 0, 0, 1],
                [0, 0, 0, 1],
                [0, 0, 0, 0],
            ]
            self.assertEqual(find_hamiltonian_path(graph), None)

    unittest.main()
