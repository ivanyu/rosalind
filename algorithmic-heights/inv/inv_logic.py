#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class InversionsCounter:
    # Taken from mer problem and modified
    @staticmethod
    def _merge_with_inv_counting(a1, a2):
        result = []
        invs = 0
        i = 0
        j = 0
        while i < len(a1) or j < len(a2):
            if i == len(a1):
                result.extend(a2[j:])
                break
            if j == len(a2):
                result.extend(a1[i:])
                break
            if a1[i] <= a2[j]:
                result.append(a1[i])
                i += 1
            else:
                result.append(a2[j])
                j += 1
                invs += len(a1[i:])
        return result, invs

    def _merge_sort_with_inv_counting(self, arr):
        if len(arr) <= 1:
            return arr, 0

        m = len(arr) // 2
        a1, invs1 = self._merge_sort_with_inv_counting(arr[:m])
        a2, invs2 = self._merge_sort_with_inv_counting(arr[m:])
        a_merged, invs_merge = self._merge_with_inv_counting(a1, a2)
        total_inv = invs1 + invs2 + invs_merge
        return a_merged, total_inv

    def count(self, arr):
        _, invs = self._merge_sort_with_inv_counting(arr)
        return invs


if __name__ == "__main__":
    import unittest

    class MergeSortTestCase(unittest.TestCase):
        def setUp(self):
            self.inv_cnt = InversionsCounter()

        def test_empty_array(self):
            arr = []
            self.assertEqual(self.inv_cnt.count(arr), 0)

        def test_one_element_array(self):
            arr = [6]
            self.assertEqual(self.inv_cnt.count(arr), 0)

        def test_sorted_array(self):
            arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            self.assertEqual(self.inv_cnt.count(arr), 0)

        def test_simple_reversed(self):
            arr = [2, 1]
            self.assertEqual(self.inv_cnt.count(arr), 1)

        def test_complex_reversed(self):
            arr = [4, 3, 2, 1]
            self.assertEqual(self.inv_cnt.count(arr), 6)

        def test_all_equals(self):
            arr = [1, 1, 1, 1, 1]
            self.assertEqual(self.inv_cnt.count(arr), 0)

        def test_some_equals(self):
            arr = [5, 5, 1, 2]
            self.assertEqual(self.inv_cnt.count(arr), 4)

        def test_mixed(self):
            arr = [5, 1, 2, 4, 6, 3]
            self.assertEqual(self.inv_cnt.count(arr), 6)

    unittest.main()
