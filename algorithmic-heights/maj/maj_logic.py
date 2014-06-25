#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collections import Counter


def find_majority(arr):
    cnt = Counter()
    threshold = (len(arr) - len(arr) % 2) // 2
    for el in arr:
        cnt[el] += 1
        if cnt[el] > threshold:
            return el
    return -1


if __name__ == "__main__":
    import unittest

    class MajorityFindingTestCase(unittest.TestCase):
        def test_empty_element(self):
            arr = []
            self.assertEqual(find_majority(arr), -1)

        def test_one_element(self):
            arr = [5]
            self.assertEqual(find_majority(arr), 5)

        def test_all_element(self):
            arr = [5, 5, 5, 5, 5, 5, 5, 5]
            self.assertEqual(find_majority(arr), 5)

        def test_strictly_half(self):
            arr = [5, 1, 5, 1, 5, 1, 5, 1]
            self.assertEqual(find_majority(arr), -1)
            arr = [5, 5, 5, 5, 1, 2, 3, 4]
            self.assertEqual(find_majority(arr), -1)

        def test_one_before_half(self):
            arr = [1, 5, 2, 5, 3, 5, 4, 0]
            self.assertEqual(find_majority(arr), -1)

        def test_one_after_half(self):
            arr = [5, 5, 2, 5, 3, 5, 4, 5]
            self.assertEqual(find_majority(arr), 5)

        def test_odd_number(self):
            arr = [1, 1, 1, 2, 2]
            self.assertEqual(find_majority(arr), 1)

    unittest.main()
