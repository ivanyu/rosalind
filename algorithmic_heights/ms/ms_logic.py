#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Taken from mer problem
def merge(a1, a2):
    result = []
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
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    m = len(arr) // 2
    a1 = merge_sort(arr[:m])
    a2 = merge_sort(arr[m:])
    return merge(a1, a2)


if __name__ == "__main__":
    import unittest

    class MergeSortTestCase(unittest.TestCase):
        def test_empty_array(self):
            arr = []
            model = sorted(arr.copy())
            self.assertSequenceEqual(merge_sort(arr), model)

        def test_one_element_array(self):
            arr = [6]
            model = sorted(arr.copy())
            self.assertSequenceEqual(merge_sort(arr), model)

        def test_sorted_array(self):
            arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            model = sorted(arr.copy())
            self.assertSequenceEqual(merge_sort(arr), model)

        def test_reverse_sorted_array(self):
            arr = [8, 7, 6, 5, 4, 3, 2, 1]
            model = sorted(arr.copy())
            self.assertSequenceEqual(merge_sort(arr), model)

        def test_reverse_one_swap_array(self):
            arr = [2, 1, 3, 4, 5, 6, 7, 8]
            model = sorted(arr.copy())
            self.assertSequenceEqual(merge_sort(arr), model)

    unittest.main()
