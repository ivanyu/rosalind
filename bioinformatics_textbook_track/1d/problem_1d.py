#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main(argv):
    if len(argv) < 2:
        print("Input file name isn't specified. Using test data.")
        genome = 'CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGA' \
                 'AACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC'
        k = 5
        L = 75
        t = 4
    else:
        with open(argv[1]) as f:
            genome = f.readline().strip()
            k, L, t = [int(x.strip()) for x in f.readline().split(' ')]

    from problem_logic import find_clumps

    for m in find_clumps(genome, k, L, t):
        print(m, end=' ')


if __name__ == "__main__":
    import sys
    main(sys.argv)
