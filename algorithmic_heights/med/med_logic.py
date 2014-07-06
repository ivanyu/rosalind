#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def partition(arr):
    if len(arr) <= 1:
        return 0, 0

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
    return i, j


def order_statistic(arr, k):
    if k >= len(arr):
        raise Exception("Invalid k: " + str(k))

    current_k = k
    current_arr = arr
    while True:
        i, j = partition(current_arr)
        p = current_arr[i]
        if current_k < i:
            current_arr = current_arr[:i]
        elif current_k > j:
            current_arr = current_arr[j + 1:]
            current_k -= (j + 1)
        else:
            return current_arr[i]


if __name__ == "__main__":
    import unittest

    class OrderStatisticTestCase(unittest.TestCase):
        def test_one_element_array(self):
            arr = [6]
            self.assertEqual(order_statistic(arr, 0), 6)

        def test_ordered_array_first(self):
            arr = [1, 2, 3, 4, 5, 6, 7]
            sorted_by_os = [order_statistic(arr, k) for k in range(len(arr))]
            self.assertSequenceEqual(sorted_by_os, sorted(arr))

        def test_reverse_ordered_array(self):
            arr = [7, 6, 5, 4, 3, 2, 1]
            sorted_by_os = [order_statistic(arr, k) for k in range(len(arr))]
            self.assertSequenceEqual(sorted_by_os, sorted(arr))

        def test_mixed_array(self):
            arr = [4, 4, 2, 6, 1, 7, 8, 1]
            sorted_by_os = [order_statistic(arr, k) for k in range(len(arr))]
            self.assertSequenceEqual(sorted_by_os, sorted(arr))

    unittest.main()
