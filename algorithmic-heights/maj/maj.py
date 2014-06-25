#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main(argv):
    from maj_logic import find_majority

    if len(argv) < 2:
        print("Input file isn't specified. Using test values:")
        print('k = 4')
        k = 4
        print('n = 8')
        n = 8
        arrays = [
            [5, 5, 5, 5, 5, 5, 5, 5],
            [8, 7, 7, 7, 1, 7, 3, 7],
            [7, 1, 6, 5, 10, 100, 1000, 1],
            [5, 1, 6, 7, 1, 1, 10, 1]
        ]
        print('Arrays:')
        for a in arrays:
            print(a)
    else:
        arrays = []
        with open(argv[1]) as f:
            k, n = [int(x.strip()) for x in f.readline().split(' ')]
            for i in range(n):
                line = f.readline().strip()
                if line:
                    a = [int(x) for x in line.split(' ')]
                    arrays.append(a)

    for a in arrays:
        print(find_majority(a), end=' ')

if __name__ == "__main__":
    import sys
    main(sys.argv)
