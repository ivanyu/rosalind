#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from parse_expr_logic import parse_expr
from scc_extract_logic import SSCExtractor


def try_satisfy(n, exp):
    graph = parse_expr(n, exp)
    sccExtractor = SSCExtractor(graph)

    result = [None for _ in range(2 * n)]
    for scc in reversed(sccExtractor.extract()):
        for v in scc:
            nv = v + n if v < n else v - n
            if nv in scc:
                return 0

            if result[v] is None:
                result[v] = True
                result[nv] = False

    return result[:n]


if __name__ == "__main__":
    import unittest

    # class ParseExprTestCase(unittest.TestCase):

    unittest.main()
