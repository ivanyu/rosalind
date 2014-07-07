#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def find_clumps(genome, k, L, t):
    if k > L:
        return []

    result = []
    patterns_occurrences = dict()
    for i in range(len(genome) - k + 1):
        pattern = genome[i:i+k]

        if pattern in result:
            continue

        if pattern not in patterns_occurrences:
            patterns_occurrences[pattern] = []

        occurrences = patterns_occurrences[pattern]
        occurrences.append(i)

        if len(occurrences) >= t:
            cnt = 1
            for j in range(-1 - 1, -1 - t, -1):
                if occurrences[-1] - L + k <= occurrences[j]:
                    cnt += 1
                else:
                    break
            if cnt >= t:
                result.append(pattern)
    return result


if __name__ == "__main__":
    import unittest

    class ClumpsFindingTestCase(unittest.TestCase):
        def test_empty_genome(self):
            genome = ''
            k = 5
            L = 10
            t = 4
            model = []
            self.assertSequenceEqual(find_clumps(genome, k, L, t), model)

        def test_empty_zero_pattern_length(self):
            genome = 'AAGCTAAT'
            k = 0
            L = 10
            t = 4
            model = ['']
            self.assertSequenceEqual(find_clumps(genome, k, L, t), model)

        def test_one_letter(self):
            genome = 'AAGCTAAT'
            k = 1
            L = 2
            t = 2
            model = ['A']
            self.assertSequenceEqual(find_clumps(genome, k, L, t), model)

        def test_two_letters_in_middle(self):
            genome = 'AAGCTACTGT'
            k = 2
            L = 8
            t = 2
            model = ['CT']
            self.assertSequenceEqual(find_clumps(genome, k, L, t), model)

        def test_two_letters_borders(self):
            genome = 'AAGCTACTGT'
            k = 2
            L = 5
            t = 2
            model = ['CT']
            self.assertSequenceEqual(find_clumps(genome, k, L, t), model)

        def test_pattern_longer_than_window(self):
            genome = 'AGCT'
            k = 4
            L = 2
            t = 1
            model = []
            self.assertSequenceEqual(find_clumps(genome, k, L, t), model)

        def test_pattern_and_window_same_size(self):
            genome = 'AGCT'
            k = 4
            L = 4
            t = 1
            model = ['AGCT']
            self.assertSequenceEqual(find_clumps(genome, k, L, t), model)

        def test_some_patters_out_of_window(self):
            genome = 'AAGCTACTCTCAA'
            k = 2
            L = 5
            t = 3
            model = []
            self.assertSequenceEqual(find_clumps(genome, k, L, t), model)

    unittest.main()
