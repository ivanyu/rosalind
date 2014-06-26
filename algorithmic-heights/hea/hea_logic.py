#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def max_heapify(arr, i):
        left_child = 2 * (i + 1) - 1
        right_child = left_child + 1
        maximum = i

        if left_child < len(arr) and arr[left_child] > arr[maximum]:
            maximum = left_child
        if right_child < len(arr) and arr[right_child] > arr[maximum]:
            maximum = right_child

        if maximum != i:
            t = arr[maximum]
            arr[maximum] = arr[i]
            arr[i] = t
            max_heapify(arr, maximum)


def build_heap(arr):
    if len(arr) <= 1:
        return

    i = len(arr) // 2 - 1
    while i >= 0:
        max_heapify(arr, i)
        i -= 1

if __name__ == "__main__":
    import unittest

    class MaxHeapTestCase(unittest.TestCase):
        def test_empty_array(self):
            arr = []
            model = []
            build_heap(arr)
            self.assertSequenceEqual(arr, model)

        def test_one_element(self):
            arr = [6]
            model = [6]
            build_heap(arr)
            self.assertSequenceEqual(arr, model)

        def test_two_level_correct(self):
            arr = [3, 1, 2]
            model = [3, 1, 2]
            build_heap(arr)
            self.assertSequenceEqual(arr, model)

        def test_two_level_unheapified(self):
            arr = [1, 2, 3]
            model = [3, 2, 1]
            build_heap(arr)
            self.assertSequenceEqual(arr, model)

        def test_mixed(self):
            arr = [1, 3, 5, 7, 2]
            model = [7, 5, 1, 3, 2]
            build_heap(arr)
            self.assertSequenceEqual(arr, model)

    unittest.main()
