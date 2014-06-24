#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main(argv):
    if len(argv) < 2:
        print("Input file name isn't specified. Using test input line.")
        input_line = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCT' \
                     'CTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
    else:
        with open(argv[1]) as f:
            input_line = f.readline()

    from collections import Counter

    cnt = Counter()
    for base in input_line:
        cnt[base] += 1

    print('{0} {1} {2} {3}'.format(cnt['A'], cnt['C'], cnt['G'], cnt['T']))


if __name__ == "__main__":
    import sys
    main(sys.argv)
