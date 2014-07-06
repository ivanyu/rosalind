#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class InsertionSorter:
    def __init__(self):
        self.swaps_done = 0

    def insertion_sort(self, arr):
        self.swaps_done = 0
        for i in range(1, len(arr)):
            k = i
            while k > 0 and arr[k] < arr[k - 1]:
                t = arr[k]
                arr[k] = arr[k - 1]
                arr[k - 1] = t
                k -= 1
                self.swaps_done += 1


if __name__ == "__main__":
    import unittest

    class InsertionSortTestCase(unittest.TestCase):
        def test_empty_array(self):
            arr = []
            sorter = InsertionSorter()
            sorter.insertion_sort(arr)
            self.assertSequenceEqual(arr, [])
            self.assertEqual(sorter.swaps_done, 0)

        def test_one_element_array(self):
            arr = [6]
            sorter = InsertionSorter()
            sorter.insertion_sort(arr)
            self.assertSequenceEqual(arr, [6])
            self.assertEqual(sorter.swaps_done, 0)

        def test_sorted_array(self):
            arr = [1, 2, 3, 4, 5, 6, 7, 8]
            arr_model = arr.copy()
            sorter = InsertionSorter()
            sorter.insertion_sort(arr)
            self.assertSequenceEqual(arr, arr_model)
            self.assertEqual(sorter.swaps_done, 0)

        def test_reverse_sorted_array(self):
            arr = [8, 7, 6, 5, 4, 3, 2, 1]
            arr_model = sorted(arr.copy())
            sorter = InsertionSorter()
            sorter.insertion_sort(arr)
            self.assertSequenceEqual(arr, arr_model)
            self.assertEqual(sorter.swaps_done, 28)

        def test_reverse_one_swap_array(self):
            arr = [2, 1, 3, 4, 5, 6, 7, 8]
            arr_model = sorted(arr.copy())
            sorter = InsertionSorter()
            sorter.insertion_sort(arr)
            self.assertSequenceEqual(arr, arr_model)
            self.assertEqual(sorter.swaps_done, 1)

    unittest.main()
