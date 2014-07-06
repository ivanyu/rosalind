#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def _z(s):
    """An advanced computation of Z-values of a string."""

    Z = [0] * len(s)
    Z[0] = len(s)

    rt = 0
    lt = 0

    for k in range(1, len(s)):
        if k > rt:
            # If k is outside the current Z-box, do naive computation.
            n = 0
            while n + k < len(s) and s[n] == s[n+k]:
                n += 1
            Z[k] = n
            if n > 0:
                lt = k
                rt = k+n-1
        else:
            # If k is inside the current Z-box, consider two cases.

            p = k - lt # Pair index.
            right_part_len = rt - k + 1

            if Z[p] < right_part_len:
                Z[k] = Z[p]
            else:
                i = rt + 1
                while i < len(s) and s[i] == s[i - k]:
                    i += 1
                Z[k] = i - k

                lt = k
                rt = i - 1
    return Z


def pattern_matching(pattern, genome):
    result = []

    zs = _z('{0}${1}'.format(pattern, genome))
    for i, z in enumerate(zs):
        if z == len(pattern):
            result.append(i - len(pattern) - 1)

    return result


if __name__ == "__main__":
    import unittest

    class PatternMatchingTestCase(unittest.TestCase):
        def test_empty_genome(self):
            pattern = 'AACT'
            genome = ''
            self.assertSequenceEqual(pattern_matching(pattern, genome), [])

        def test_empty_pattern(self):
            pattern = ''
            genome = 'AACGTCGGTTA'
            model = list(range((len(genome))))
            self.assertSequenceEqual(pattern_matching(pattern, genome), model)

        def test_one_letter_genome_match(self):
            pattern = 'A'
            genome = 'A'
            model = [0]
            self.assertSequenceEqual(pattern_matching(pattern, genome), model)

        def test_one_letter_genome_not_match(self):
            pattern = 'T'
            genome = 'A'
            model = []
            self.assertSequenceEqual(pattern_matching(pattern, genome), model)

        def test_mixed_not_overlapped(self):
            pattern = 'GT'
            genome = 'ACGTTTCTAAAGTA'
            model = [2, 11]
            self.assertSequenceEqual(pattern_matching(pattern, genome), model)

        def test_mixed_overlapped(self):
            pattern = 'AA'
            genome = 'GGGAAA'
            model = [3, 4]
            self.assertSequenceEqual(pattern_matching(pattern, genome), model)

    unittest.main()
