#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter


def find_most_frequent_k_measures(string_to_examine, k):
    cnt = Counter()
    found_max = 0
    for i in range(0, len(string_to_examine) - k + 1):
        s = string_to_examine[i: i + k]
        cnt[s] += 1
        if cnt[s] > found_max:
            found_max = cnt[s]

    result = set()
    for s, c in cnt.items():
        if c == found_max:
            result.add(s)
    return result


if __name__ == "__main__":
    import unittest

    class FindMostFrequentKMeasuresTestCase(unittest.TestCase):
        def test_empty_string(self):
            s = ''
            self.assertSetEqual(find_most_frequent_k_measures(s, 2), set())

        def test_one_symbol(self):
            s = 'A'
            self.assertSetEqual(find_most_frequent_k_measures(s, 1), {'A'})

        def test_k_zero(self):
            s = 'ACGT'
            self.assertSetEqual(find_most_frequent_k_measures(s, 0), {''})

        def test_one_most_frequent(self):
            s = 'AAGACCGTTATGAACAA'
            self.assertSetEqual(
                find_most_frequent_k_measures(s, 2), {'AA'})

        def test_many_most_frequent(self):
            s = 'AAGACCGTTATGAAC'
            self.assertSetEqual(
                find_most_frequent_k_measures(s, 2), {'AA', 'AC', 'GA'})

    unittest.main()
