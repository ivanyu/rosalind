#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def _collect_edges(graph):
    from itertools import product

    result = []
    for (u, v) in product(range(len(graph)), range(len(graph))):
        if graph[u][v] != 0:
            result.append((u, v))
    return result


def _detect_nwc_for_src(graph):
    if len(graph) == 0:
        return False

    edges = _collect_edges(graph)

    INF = None

    all_v = list(range(len(graph)))

    touched_v = set()  # To not follow already followed paths.

    for s in all_v:
        if s in touched_v:
            continue
        dist = [INF for _ in range(len(graph))]
        dist[s] = 0
        changes = True  # To stop when distances are already found.
        for i in range(len(graph)):
            if not changes:
                break
            extra = (i == len(graph) - 1)
            changes = False
            for u, v in edges:
                if (dist[u] is not INF and
                        (dist[v] is INF or dist[v] > dist[u] + graph[u][v])):
                    dist[v] = dist[u] + graph[u][v]
                    changes = True
                    if extra:  # If it's the extra pass and there is decrement.
                        return True
        for i, d in enumerate(dist):
            if d is not None:
                touched_v.add(i)
    return False


def detect_nwc(graph):
    return _detect_nwc_for_src(graph)


if __name__ == "__main__":
    import unittest

    class BellmanFormCycleDetectionTestCase(unittest.TestCase):
        def test_empty_graph(self):
            graph = []
            self.assertEqual(detect_nwc(graph), False)

        def test_one_vertex_graph(self):
            graph = [[0]]
            self.assertEqual(detect_nwc(graph), False)

        def test_line(self):
            graph = [
                [0, 1, 0, 0],
                [0, 0, 2, 0],
                [0, 0, 0, 3],
                [0, 0, 0, 0],
            ]
            self.assertEqual(detect_nwc(graph), False)

        def test_not_connected(self):
            n = 6
            graph = [[0 for _ in range(n)] for _ in range(n)]
            self.assertEqual(detect_nwc(graph), False)

        def test_first_isolated(self):
            graph = [
                [0, 0, 0, 0],
                [1, 0, 0, 0],
                [1, 0, 0, 0],
                [1, 0, 0, 0],
            ]
            self.assertEqual(detect_nwc(graph), False)

        def test_mixed1(self):
            graph = [
                [0, 3, 0, 0, 10, 0, 0],
                [0, 0, 5, 1,  0, 0, 0],
                [0, 0, 0, 0,  1, 1, 0],
                [0, 0, 0, 0,  4, 0, 0],
                [0, 0, 0, 0,  0, 2, 0],
                [0, 0, 0, 0,  0, 0, 0],
                [1, 0, 0, 0,  0, 0, 0],
            ]
            self.assertEqual(detect_nwc(graph), False)

        def test_mixed2(self):
            graph = [
                [ 0,  7,  9,  0, 0, 14],
                [ 7,  0, 10, 15, 0,  0],
                [ 9, 10,  0, 11, 0,  2],
                [ 0, 15, 11,  0, 6,  0],
                [ 0,  0,  0,  6, 0,  9],
                [14,  0,  2,  0, 9,  0],
            ]
            self.assertEqual(detect_nwc(graph), False)

        def test_isolated_pair(self):
            graph = [
                [0, 2, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 3, 0],
                [0, 0, 0, 0],
            ]
            self.assertEqual(detect_nwc(graph), False)

        def test_shortest_path_with_negative_edge(self):
            graph = [
                [0, 1,  0, 2],
                [0, 0,  5, 0],
                [0, 0,  0, 0],
                [0, 0, -1, 0],
            ]
            self.assertEqual(detect_nwc(graph), False)

        def test_connected_with_nwc(self):
            graph = [
                [0,   2,  0, 0],
                [0,   0, 20, 0],
                [2, -30,  0, 2],
                [5,   0, -1, 0],
            ]
            self.assertEqual(detect_nwc(graph), True)

        def test_separated_nwc(self):
            graph = [
                [0, 2,  0, 0, 0],
                [0, 0,  0, 0, 0],
                [0, 0,  0, 1, 0],
                [0, 0,  0, 0, 2],
                [0, 0, -4, 0, 0],
            ]
            self.assertEqual(detect_nwc(graph), True)

    unittest.main()
