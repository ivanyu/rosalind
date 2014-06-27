#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def partition(arr):
    if len(arr) <= 1:
        return

    p = arr[0]
    i = 0
    j = 0
    k = 1
    while k < len(arr):
        current = arr[k]
        if current <= p:
            t = arr[j + 1]
            arr[j + 1] = arr[k]
            arr[k] = t
            j += 1
            if current < p:
                t = arr[i]
                arr[i] = arr[j]
                arr[j] = t
                i += 1
        k += 1


if __name__ == "__main__":
    import unittest

    class PartitionTestCase(unittest.TestCase):
        def _test_partitioning(self, arr):
            pivot = arr[0]
            partition(arr)
            stage = 0
            for a in arr:
                if stage == 0:
                    if a == pivot:
                        stage = 1
                        continue
                    self.assertLess(a, pivot)
                elif stage == 1:
                    if a > pivot:
                        stage = 2
                        continue
                    self.assertEqual(a, pivot)
                elif stage == 2:
                    self.assertGreater(a, pivot)

        def test_empty_array(self):
            arr = []
            partition(arr)
            self.assertEqual(arr, [])

        def test_one_element_array(self):
            arr = [6]
            partition(arr)
            self.assertEqual(arr, [6])

        def test_all_less(self):
            arr = [10, 1, 2, 3, 4, 5]
            self._test_partitioning(arr)

        def test_all_greater(self):
            arr = [10, 11, 12, 13, 14, 15]
            self._test_partitioning(arr)

        def test_all_multiple_pivots(self):
            arr = [10, 1, 5, 10, 2, 1, 3, 10, 0, 22, 11, 215, -48]
            self._test_partitioning(arr)

        def test_mixed(self):
            # arr = [5, 1, 7, 4, 6, 9, 2, 3, 5, 2, 8, 2, 9]
            arr = [32167, 60525, 62168, -68066, -14730, -25297, -40314,
                   -97524, 39712, -48079]
            self._test_partitioning(arr)

    unittest.main()
