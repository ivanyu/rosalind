#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def find_2sum(arr):
    if len(arr) <= 1:
        return -1

    working_arr = list(enumerate(arr))
    working_arr.sort(key=lambda x: x[1])
    i = 0
    j = len(working_arr) - 1
    while i < j:
        if (working_arr[i][1] < 0 and working_arr[j][1] < 0 or
                working_arr[i][1] > 0 and working_arr[j][1] > 0):
            break

        if working_arr[i][1] + working_arr[j][1] == 0:
            result = [working_arr[i][0], working_arr[j][0]]
            result.sort()
            return tuple(result)

        elif abs(working_arr[i][1]) > abs(working_arr[j][1]):
            i += 1
        else:
            j -= 1
    return -1


if __name__ == "__main__":
    import unittest
    from itertools import combinations

    class Find2SumTestCase(unittest.TestCase):
        def test_empty_array(self):
            arr = []
            self.assertEqual(find_2sum(arr), -1)

        def test_one_element_array(self):
            arr = [6]
            self.assertEqual(find_2sum(arr), -1)

        def test_all_positive(self):
            arr = [1, 2, 3, 4, 5, 6]
            self.assertEqual(find_2sum(arr), -1)

        def test_all_negative(self):
            arr = [-1, -2, -3, -4, -5, -6]
            self.assertEqual(find_2sum(arr), -1)

        def test_all_zeros(self):
            arr = [0, 0, 0, 0]
            result = find_2sum(arr)
            possible_results = combinations(range(len(arr)), 2)
            self.assertIn(result, possible_results)

        def test_no_pairs1(self):
            arr = [2, -3, 4, 10, 5]
            self.assertEqual(find_2sum(arr), -1)

        def test_no_pairs2(self):
            arr = [-5, 2, 3, 2, -4]
            self.assertEqual(find_2sum(arr), -1)

        def test_zero_pair(self):
            arr = [0, 2, 3, 0, -4]
            self.assertEqual(find_2sum(arr), (0, 3))

        def test_nonzero_pair(self):
            arr = [5, 10, -213, -1, -2, -10]
            self.assertEqual(find_2sum(arr), (1, 5))

        def test_two_nonzero_pairs(self):
            arr = [5, 10, -213, -1, -2, -10, 213, 1000]
            result = find_2sum(arr)
            possible_results = [(1, 5), (2, 6)]
            self.assertIn(result, possible_results)

        def test_two_nonzero_pairs_and_zero_pair(self):
            arr = [5, 10, 0, -213, -1, 0, -2, -10, 213, 1000]
            result = find_2sum(arr)
            possible_results = [(1, 7), (2, 5), (3, 8)]
            self.assertIn(result, possible_results)

    unittest.main()
