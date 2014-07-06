#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_reverse_complement(s):
    complements = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }

    result = ''.join(reversed([complements[x] for x in s]))
    return result


if __name__ == "__main__":
    import unittest

    class ReverseComplementsTestCase(unittest.TestCase):
        def test_empty_string(self):
            s = ''
            model = ''
            self.assertEqual(get_reverse_complement(s), model)

        def test_one_symbol(self):
            s = 'A'
            model = 'T'
            self.assertEqual(get_reverse_complement(s), model)

        def test_all_nucleotides(self):
            s = 'GTCA'
            model = 'TGAC'
            self.assertEqual(get_reverse_complement(s), model)

    unittest.main()
