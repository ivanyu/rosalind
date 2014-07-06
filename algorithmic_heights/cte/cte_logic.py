#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Taken from dij problem.
def _dijkstra(graph, s):
    if len(graph) == 0:
        return []

    INF = -1

    all_v = [i for i in range(len(graph))]

    dist = [INF for _ in graph]
    dist[s] = 0
    visited = [False for _ in graph]

    while not all(visited):
        not_visited = [e[0] for e in enumerate(visited) if not e[1]]
        minimum = not_visited[0]
        for v in not_visited:
            if (dist[minimum] == INF and dist[v] != INF or
                    dist[minimum] != INF and dist[v] != INF
                    and dist[v] < dist[minimum]):
                minimum = v
        curr_n = minimum
        if dist[curr_n] != INF:
            for u in all_v:
                if graph[curr_n][u] > 0 and not visited[u]:
                    new_dist = dist[curr_n] + graph[curr_n][u]
                    if dist[u] == INF or dist[u] > new_dist:
                        dist[u] = new_dist
        visited[curr_n] = True
    return dist


def cte(graph, a, b):
    r = _dijkstra(graph, b)[a]
    if r == -1:
        return r
    return r + graph[a][b]


if __name__ == "__main__":
    import unittest

    class CTETestCase(unittest.TestCase):
        def test_line(self):
            graph = [
                [0, 1, 0, 0],
                [0, 0, 2, 0],
                [0, 0, 0, 3],
                [0, 0, 0, 0],
            ]
            self.assertEqual(cte(graph, 0, 1), -1)

        def test_not_connected(self):
            n = 6
            graph = [[0 for _ in range(n)] for _ in range(n)]
            model = [-1 for _ in range(n)]
            model[0] = 0
            self.assertEqual(cte(graph, 0, 1), -1)

        def test_one_circle(self):
            graph = [
                [0, 1, 0, 0],
                [0, 0, 2, 2],
                [4, 0, 0, 0],
                [0, 0, 0, 0],
            ]
            self.assertEqual(cte(graph, 0, 1), 7)

        def test_two_compete_circles(self):
            graph = [
                [0, 1, 0, 0],
                [0, 0, 2, 2],
                [4, 0, 0, 0],
                [3, 0, 0, 0],
            ]
            self.assertEqual(cte(graph, 0, 1), 6)

        def test_no_circles(self):
            graph = [
                [0, 1, 0, 0],
                [0, 0, 2, 0],
                [0, 0, 0, 0],
                [3, 0, 0, 0],
            ]
            self.assertEqual(cte(graph, 0, 1), -1)

    unittest.main()
