#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum


class SSCExtractor:
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

    def _dfs_second(self, visited, s):
        visited.add(s)

        for v in self._all_v:
            # Traversing through inverse graph!
            if self._ig[s][v] != 0 and v not in visited:
                self._dfs_second(visited, v)

    def _glue_graph(self, sccs):
        n = len(sccs)

        for a, b in zip(range(n), range(n)):
            if a != b:
                assert len(sccs[a].intersection(sccs[b])) == 0

        vertex_component_map = dict()
        for c in range(n):
            for v in sccs[c]:
                vertex_component_map[v] = c

        glued_graph = [[0 for _ in range(n)] for _ in range(n)]

        # Outgoing edges
        for u in range(len(self._g)):
            component_from = vertex_component_map[u]
            for v in range(len(self._g)):
                if self._g[u][v] != 0:
                    component_to = vertex_component_map[v]
                    if component_from != component_to:
                        glued_graph[component_from][component_to] = 1

        return glued_graph

    def extract(self):
        if len(self._g) == 0:
            return []
        if len(self._g) == 1:
            return [[0]]

        colors = [self.Colors.White for _ in range(len(self._g))]
        for v in self._all_v:
            if colors[v] == self.Colors.White:
                self._dfs_first(colors, v)

        sorted_by_f = sorted(enumerate(self._f),
                             key=lambda x: x[1],
                             reverse=True)
        sorted_by_f = [x[0] for x in sorted_by_f]

        sccs = []
        visited = set()
        for v in sorted_by_f:
            if v not in visited:
                old_visited = set(visited)
                self._dfs_second(visited, v)
                new_component = visited - old_visited
                sccs.append(new_component)

        glued_graph = self._glue_graph(sccs)
        return glued_graph


if __name__ == "__main__":
    import unittest

    class SSCExtractorTestCase(unittest.TestCase):
        def test_empty_graph(self):
            graph = []
            self.assertEqual(SSCExtractor(graph).extract(), [])

        def test_one_vertex_graph(self):
            graph = [[]]
            self.assertEqual(SSCExtractor(graph).extract(), [[0]])

        def test_connected_triangle(self):
            graph = [
                [0, 1, 1],
                [1, 0, 1],
                [1, 1, 0],
            ]
            self.assertEqual(SSCExtractor(graph).extract(), [[0]])

        def test_connected_through_one_triangle(self):
            graph = [
                [0, 1, 0],
                [1, 0, 1],
                [0, 1, 0],
            ]
            self.assertEqual(SSCExtractor(graph).extract(), [[0]])

        def test_line(self):
            graph = [
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1],
                [0, 0, 0, 0],
            ]
            self.assertEqual(SSCExtractor(graph).extract(), graph)

        def test_not_connected(self):
            n = 6
            graph = [[0 for _ in range(n)] for _ in range(n)]
            self.assertEqual(SSCExtractor(graph).extract(), graph)

        def test_two_sccs_connected(self):
            graph = [
                [0, 1, 1, 0, 0, 0],
                [1, 0, 1, 0, 0, 0],
                [1, 1, 0, 0, 1, 0],
                [0, 0, 0, 0, 1, 1],
                [0, 0, 0, 1, 0, 1],
                [0, 0, 0, 1, 1, 0],
            ]
            model = [
                [0, 1],
                [0, 0],
            ]
            self.assertEqual(SSCExtractor(graph).extract(), model)

        def test_two_sccs_not_connected(self):
            graph = [
                [0, 1, 1, 0, 0, 0],
                [1, 0, 1, 0, 0, 0],
                [1, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 1],
                [0, 0, 0, 1, 0, 1],
                [0, 0, 0, 1, 1, 0],
            ]
            model = [
                [0, 0],
                [0, 0],
            ]
            self.assertEqual(SSCExtractor(graph).extract(), model)

        def test_scc_and_alone(self):
            graph = [
                [0, 1, 1, 0],
                [1, 0, 1, 0],
                [1, 1, 0, 0],
                [1, 0, 0, 0],
            ]
            model = [
                [0, 1],
                [0, 0],
            ]
            self.assertEqual(SSCExtractor(graph).extract(), model)

    unittest.main()
