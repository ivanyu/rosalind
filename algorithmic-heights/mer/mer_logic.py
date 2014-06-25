#!/usr/bin/env python3
# -*- coding: utf-8 -*-


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


if __name__ == "__main__":
    import unittest

    class MergeTestCase(unittest.TestCase):
        def test_empty_arrays(self):
            a1 = []
            a2 = []
            model = []
            self.assertEqual(merge(a1, a2), model)

        def test_full_and_empty(self):
            a1 = [1, 2, 3, 4]
            a2 = []
            model = a1.copy()
            self.assertEqual(merge(a1, a2), model)

        def test_empty_and_full(self):
            a1 = []
            a2 = [1, 2, 3, 4]
            model = a2.copy()
            self.assertEqual(merge(a1, a2), model)

        def test_one_elements(self):
            a1 = [1]
            a2 = [2]
            model = [1, 2]
            self.assertEqual(merge(a1, a2), model)

        def test_equal(self):
            a1 = [1, 2, 3, 4, 5, 6]
            a2 = a1.copy()
            model = []
            for x in a1:
                model.append(x)
                model.append(x)
            self.assertEqual(merge(a1, a2), model)

        def test_first_after_second(self):
            a1 = [5, 6, 7, 8]
            a2 = [1, 2, 3, 4]
            model = a2.copy()
            model.extend(a1)
            self.assertEqual(merge(a1, a2), model)

        def test_second_after_first(self):
            a1 = [1, 2, 3, 4]
            a2 = [5, 6, 7, 8]
            model = a1.copy()
            model.extend(a2)
            self.assertEqual(merge(a1, a2), model)

        def test_mixed(self):
            a1 = [-20, 1, 5, 8, 10, 502]
            a2 = [-305, 2, 3, 6, 11, 20, 399]
            model = a1.copy()
            model.extend(a2)
            model.sort()
            self.assertEqual(merge(a1, a2), model)

    unittest.main()
