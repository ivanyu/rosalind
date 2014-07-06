#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def partition(arr, a, b):
    if b - a <= 1:
        return a, a

    p = arr[a]
    i = a
    j = a
    k = a + 1
    while k < b:
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
    return i, j


def quick_sort_internal(arr, a, b):
    if a >= b:
        return

    i, j = partition(arr, a, b)
    quick_sort_internal(arr, a, i)
    quick_sort_internal(arr, j + 1, b)


def quick_sort(arr):
    quick_sort_internal(arr, 0, len(arr))

if __name__ == "__main__":
    import unittest

    class QuickSortTestCase(unittest.TestCase):
        def test_empty_array(self):
            arr = []
            model = sorted(arr.copy())
            quick_sort(arr)
            self.assertSequenceEqual(arr, model)

        def test_one_element_array(self):
            arr = [6]
            model = sorted(arr.copy())
            quick_sort(arr)
            self.assertSequenceEqual(arr, model)

        def test_sorted_array(self):
            arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            model = sorted(arr.copy())
            quick_sort(arr)
            self.assertSequenceEqual(arr, model)

        def test_reverse_sorted_array(self):
            arr = [8, 7, 6, 5, 4, 3, 2, 1]
            model = sorted(arr.copy())
            quick_sort(arr)
            self.assertSequenceEqual(arr, model)

        def test_reverse_one_swap_array(self):
            arr = [2, 1, 3, 4, 5, 6, 7, 8]
            model = sorted(arr.copy())
            quick_sort(arr)
            self.assertSequenceEqual(arr, model)

    unittest.main()
