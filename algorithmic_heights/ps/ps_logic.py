#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def min_heapify(arr, i, len_limit):
        left_child = 2 * (i + 1) - 1
        right_child = left_child + 1
        minimum = i

        if left_child < len_limit and arr[left_child] < arr[minimum]:
            minimum = left_child
        if right_child < len_limit and arr[right_child] < arr[minimum]:
            minimum = right_child

        if minimum != i:
            t = arr[minimum]
            arr[minimum] = arr[i]
            arr[i] = t
            min_heapify(arr, minimum, len_limit)


def build_heap(arr):
    if len(arr) <= 1:
        return

    i = len(arr) // 2 - 1
    while i >= 0:
        min_heapify(arr, i, len(arr))
        i -= 1


def partial_sort(arr, k):
    if k == 0:
        return []

    build_heap(arr)

    k_rest = k
    result = []
    i = len(arr) - 1
    while i >= 0 and k_rest > 0:
        result.append(arr[0])
        arr[0] = arr[i]
        min_heapify(arr, 0, i)
        i -= 1
        k_rest -= 1
    return result


if __name__ == "__main__":
    import unittest

    class PartialSortTestCase(unittest.TestCase):
        def test_one_element_take_zero(self):
            arr = [6]
            model = []
            result = partial_sort(arr, 0)
            self.assertSequenceEqual(result, model)

        def test_one_element_take_one(self):
            arr = [6]
            model = [6]
            result = partial_sort(arr, 1)
            self.assertSequenceEqual(result, model)

        def test_sorted_array(self):
            arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            model = [1, 2, 3, 4]
            result = partial_sort(arr, 4)
            self.assertSequenceEqual(result, model)

        def test_reverse_sorted_array(self):
            arr = [8, 7, 6, 5, 4, 3, 2, 1]
            model = [1, 2, 3, 4]
            result = partial_sort(arr, 4)
            self.assertSequenceEqual(result, model)

        def test_mixed(self):
            arr = [-12, 2, 1, 3, 4, 5, 6, 7, 8, 100, 0]
            model = [-12, 0, 1, 2]
            result = partial_sort(arr, 4)
            self.assertSequenceEqual(result, model)

    unittest.main()
