#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def parse_expr(n, clauses):
    graph = [[0 for _ in range(2 * n)] for _ in range(2 * n)]

    for a, b in clauses:
        at = (a if a > 0 else abs(a) + n) - 1
        nat = (-a if (-a) > 0 else abs(a) + n) - 1
        bt = (b if b > 0 else abs(b) + n) - 1
        nbt = (-b if (-b) > 0 else abs(b) + n) - 1
        graph[nat][bt] = 1
        graph[nbt][at] = 1

    return graph


if __name__ == "__main__":
    import unittest

    class ParseExprTestCase(unittest.TestCase):
        def test_parse_empty(self):
            g = parse_expr(0, [])
            self.assertEqual(g, [])

        def test_one_clause1(self):
            g = parse_expr(2, [(1, 2)])
            m = [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 1, 0, 0],
                [1, 0, 0, 0],
            ]
            self.assertEqual(g, m)

        def test_one_clause2(self):
            g = parse_expr(2, [(-1, 2)])
            m = [
                [0, 1, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 1, 0],
            ]
            self.assertEqual(g, m)

        def test_one_clause3(self):
            g = parse_expr(2, [(1, -2)])
            m = [
                [0, 0, 0, 0],
                [1, 0, 0, 0],
                [0, 0, 0, 1],
                [0, 0, 0, 0],
            ]
            self.assertEqual(g, m)

        def test_one_clause4(self):
            g = parse_expr(2, [(-1, -2)])
            m = [
                [0, 0, 0, 1],
                [0, 0, 1, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ]
            self.assertEqual(g, m)

        def test_two_clauses_not_mixed(self):
            g = parse_expr(4, [(1, 2), (3, 4)])
            m = [
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0],
            ]
            self.assertEqual(g, m)

        def test_two_clauses_mixed(self):
            g = parse_expr(3, [(1, 2), (-2, 3)])
            m = [
                [0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0],
            ]
            self.assertEqual(g, m)

        def test_complex_1(self):
            g = parse_expr(2, [(1, 2), (-1, 2), (1, -2), (-1, -2)])
            m = [
                [0, 1, 0, 1],
                [1, 0, 1, 0],
                [0, 1, 0, 1],
                [1, 0, 1, 0],
            ]
            self.assertEqual(g, m)

        def test_complex_2(self):
            g = parse_expr(3, [(1, 2), (2, 3), (-1, -2), (-2, -3)])
            m = [
                [0, 0, 0, 0, 1, 0],
                [0, 0, 0, 1, 0, 1],
                [0, 0, 0, 0, 1, 0],
                [0, 1, 0, 0, 0, 0],
                [1, 0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0, 0],
            ]
            self.assertEqual(g, m)

    unittest.main()
