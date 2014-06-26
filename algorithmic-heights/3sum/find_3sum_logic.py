#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def find_3sum(arr):
    if len(arr) <= 2:
        return -1

    working_arr = list(enumerate(arr))
    working_arr.sort(key=lambda x: x[1])

    for i in range(len(working_arr) - 3):
        a1 = working_arr[i][1]

        j = i + 1
        k = len(working_arr) - 1

        while j < k:
            a2 = working_arr[j][1]
            a3 = working_arr[k][1]
            sum = a1 + a2 + a3

            if sum == 0:
                result = [working_arr[i][0],
                          working_arr[j][0],
                          working_arr[k][0]]
                result.sort()
                return tuple(result)
            elif sum > 0:
                k -= 1
            else:
                j += 1
    return -1


if __name__ == "__main__":
    import unittest
    from itertools import combinations

    class Find3SumTestCase(unittest.TestCase):
        def test_empty_array(self):
            arr = []
            self.assertEqual(find_3sum(arr), -1)

        def test_one_element_array(self):
            arr = [6]
            self.assertEqual(find_3sum(arr), -1)

        def test_all_positive(self):
            arr = [1, 2, 3, 4, 5, 6]
            self.assertEqual(find_3sum(arr), -1)

        def test_all_negative(self):
            arr = [-1, -2, -3, -4, -5, -6]
            self.assertEqual(find_3sum(arr), -1)

        def test_all_zeros(self):
            arr = [0, 0, 0, 0]
            result = find_3sum(arr)
            possible_results = combinations(range(len(arr)), 3)
            self.assertIn(result, possible_results)

        def test_no_triples(self):
            arr = [2, -3, 4, 10, 5]
            self.assertEqual(find_3sum(arr), -1)

        def test_zero_triple(self):
            arr = [0, 2, 3, 0, -4, 0]
            self.assertEqual(find_3sum(arr), (0, 3, 5))

        def test_nonzero_triple(self):
            arr = [-5, 2, 3, 2, -4]
            result = find_3sum(arr)
            possible_results = [(0, 1, 2), (0, 1, 4), (1, 3, 4)]
            self.assertIn(result, possible_results)

        def test_two_nonzero_triples(self):
            arr = [5, 10, -213, -1, -2, -9, 213, 1000, -4]
            result = find_3sum(arr)
            possible_results = [(0, 3, 8), (1, 3, 5)]
            self.assertIn(result, possible_results)

        def test_two_nonzero_triples_and_zero_triple(self):
            arr = [5, 10, 0, -213, -1, 0, -2, -10, 210, 3, 0]
            result = find_3sum(arr)
            possible_results = [(1, 2, 7), (2, 5, 10), (3, 8, 9)]
            self.assertIn(result, possible_results)

    unittest.main()
