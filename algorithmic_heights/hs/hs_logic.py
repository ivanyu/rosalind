#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def max_heapify(arr, i, len_limit):
        left_child = 2 * (i + 1) - 1
        right_child = left_child + 1
        maximum = i

        if left_child < len_limit and arr[left_child] > arr[maximum]:
            maximum = left_child
        if right_child < len_limit and arr[right_child] > arr[maximum]:
            maximum = right_child

        if maximum != i:
            t = arr[maximum]
            arr[maximum] = arr[i]
            arr[i] = t
            max_heapify(arr, maximum, len_limit)


def build_heap(arr):
    if len(arr) <= 1:
        return

    i = len(arr) // 2 - 1
    while i >= 0:
        max_heapify(arr, i, len(arr))
        i -= 1


def heap_sort(arr):
    build_heap(arr)

    i = len(arr) - 1
    while i > 0:
        t = arr[i]
        arr[i] = arr[0]
        arr[0] = t
        max_heapify(arr, 0, i)
        i -= 1


if __name__ == "__main__":
    import unittest

    class HeapSortTestCase(unittest.TestCase):
        def test_empty_array(self):
            arr = []
            model = sorted(arr.copy())
            heap_sort(arr)
            self.assertSequenceEqual(arr, model)

        def test_one_element_array(self):
            arr = [6]
            model = sorted(arr.copy())
            heap_sort(arr)
            self.assertSequenceEqual(arr, model)

        def test_sorted_array(self):
            arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            model = sorted(arr.copy())
            heap_sort(arr)
            self.assertSequenceEqual(arr, model)

        def test_reverse_sorted_array(self):
            arr = [8, 7, 6, 5, 4, 3, 2, 1]
            model = sorted(arr.copy())
            heap_sort(arr)
            self.assertSequenceEqual(arr, model)

        def test_reverse_one_swap_array(self):
            arr = [2, 1, 3, 4, 5, 6, 7, 8]
            model = sorted(arr.copy())
            heap_sort(arr)
            self.assertSequenceEqual(arr, model)

    unittest.main()
