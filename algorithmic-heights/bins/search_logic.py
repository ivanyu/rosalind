#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def search(arr, k):
    if not arr or k < arr[0] or k > arr[-1]:
        return -1

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if k == arr[mid]:
            return mid
        if k < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


if __name__ == "__main__":
    import unittest

    class BinarySearchTestCase(unittest.TestCase):
        def test_empty_array(self):
            self.assertEqual(search([], 10), -1)

        def test_one_element_array_exclusive(self):
            self.assertEqual(search([55], 10), -1)

        def test_one_element_array_inclusive(self):
            self.assertEqual(search([10], 10), 0)

        def test_exclusive_less(self):
            self.assertEqual(search([-5, 6, 36, 74, 80, 238, 550], -10), -1)

        def test_exclusive_mid(self):
            self.assertEqual(search([-5, 6, 36, 74, 80, 238, 550], 79), -1)

        def test_exclusive_great(self):
            self.assertEqual(search([-5, 6, 36, 74, 80, 238, 550], 999), -1)

        def test_inclusive_first(self):
            self.assertEqual(search([-5, 6, 36, 74, 80, 238, 550], -5), 0)

        def test_inclusive_mid(self):
            self.assertEqual(search([-5, 6, 36, 74, 80, 238, 550], 80), 4)

        def test_inclusive_last(self):
            self.assertEqual(search([-5, 6, 36, 74, 80, 238, 550], 550), 6)

    unittest.main()
