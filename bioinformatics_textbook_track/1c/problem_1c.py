#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main(argv):
    if len(argv) < 2:
        print("Input file name isn't specified. Using test data.")
        pattern = 'ATAT'
        genome = 'GATATATGCATATACTT'
    else:
        with open(argv[1]) as f:
            pattern = f.readline().strip()
            genome = f.readline().strip()

    from problem_logic import pattern_matching

    for m in pattern_matching(pattern, genome):
        print(m, end=' ')


if __name__ == "__main__":
    import sys
    main(sys.argv)
