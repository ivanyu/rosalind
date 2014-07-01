#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum


class Colors(Enum):
    White = 1
    Red = 2
    Green = 3


def _dfs(graph, s, colors, current_color):
    colors[s] = current_color

    old_color = current_color
    if current_color == Colors.Red:
        new_color = Colors.Green
    else:
        new_color = Colors.Red

    for v in range(len(graph)):
        if graph[s][v] != 0:
            if colors[v] == old_color:
                return False
            if colors[v] == new_color:
                continue
            r = _dfs(graph, v, colors, new_color)
            if not r:
                return False
    return True


def test_bip(graph):
    if len(graph) <= 2:
        return False

    colors = [Colors.White for _ in range(len(graph))]

    for v in range(len(graph)):
        if colors[v] == Colors.White:
            r = _dfs(graph, v, colors, Colors.Red)
            if not r:
                return False
    return True



if __name__ == "__main__":
    import unittest

    class BipartitenessTestTestCase(unittest.TestCase):
        def test_empty_graph(self):
            graph = []
            self.assertEqual(test_bip(graph), False)

        def test_one_vertex_graph(self):
            graph = [[]]
            self.assertEqual(test_bip(graph), False)

        def test_line(self):
            graph = [
                [0, 1, 0, 0],
                [1, 0, 1, 0],
                [0, 1, 0, 1],
                [0, 0, 1, 0],
            ]
            self.assertEqual(test_bip(graph), True)

        def test_not_connected(self):
            n = 6
            graph = [[0 for i in range(n)] for _ in range(n)]
            self.assertEqual(test_bip(graph), True)

        def test_cycle_of_4(self):
            graph = [
                [0, 1, 0, 1],
                [1, 0, 1, 0],
                [0, 1, 0, 1],
                [1, 0, 1, 0],
            ]
            self.assertEqual(test_bip(graph), True)

        def test_cycle_of_4_with_triangle(self):
            graph = [
                [0, 1, 1, 1],
                [1, 0, 1, 0],
                [1, 1, 0, 1],
                [1, 0, 1, 0],
            ]
            self.assertEqual(test_bip(graph), False)

        def test_fork(self):
            graph = [
                [0, 1, 1],
                [1, 0, 0],
                [1, 0, 0],
            ]
            self.assertEqual(test_bip(graph), True)

    unittest.main()
