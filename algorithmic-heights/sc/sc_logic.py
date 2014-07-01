#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum
from scc_extract_logic import SSCExtractor
from ts_logic import TopoligicalSorter


def check_semi_connectedness(graph):
    # Algorithm:
    # 1. Extract strong connected components (metagraph).
    # 2. Topologically sort the metagraph.
    # 3. Check if there are (meta-)edges between (meta-)vertices
    # in topological order.

    sccExtractor = SSCExtractor(graph)
    metagraph = sccExtractor.extract()

    ts = TopoligicalSorter(metagraph)
    sorted_metagraph = ts.sort()

    for u, v in zip([None] + sorted_metagraph, sorted_metagraph):
        if u is None:
            continue
        if metagraph[u][v] == 0:
            return False
    return True


if __name__ == "__main__":
    import unittest

    class SemiConnectednessTestCase(unittest.TestCase):
        def test_empty_graph(self):
            graph = []
            self.assertEqual(check_semi_connectedness(graph), True)

        def test_one_vertex_graph(self):
            graph = [[]]
            self.assertEqual(check_semi_connectedness(graph), True)

        def test_line(self):
            graph = [
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1],
                [0, 0, 0, 0],
            ]
            self.assertEqual(check_semi_connectedness(graph), True)

        def test_not_connected(self):
            n = 6
            graph = [[0 for _ in range(n)] for _ in range(n)]
            self.assertEqual(check_semi_connectedness(graph), False)

        def test_cork(self):
            graph = [
                [0, 1, 0],
                [0, 0, 0],
                [0, 1, 0],
            ]
            self.assertEqual(check_semi_connectedness(graph), False)

        def test_alone_vertex(self):
            graph = [
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ]
            self.assertEqual(check_semi_connectedness(graph), False)

    unittest.main()
