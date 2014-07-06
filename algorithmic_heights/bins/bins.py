#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main(argv):
    from search_logic import search

    if len(argv) < 2:
        print("Input file isn't specified. Using test values:")
        print('n = 5')
        n = 5
        print('m = 6')
        n = 6
        print('A = [10, 20, 30, 40, 50]')
        arr = [10, 20, 30, 40, 50]
        print('ks = [40, 10, 35, 15, 40, 20]')
        ks = [40, 10, 35, 15, 40, 20]
    else:
        with open(argv[1]) as f:
            n = int(f.readline().strip())
            m = int(f.readline().strip())
            arr = [int(x) for x in f.readline().strip().split(' ')]
            ks = [int(x) for x in f.readline().strip().split(' ')]

    for k in ks:
        res = search(arr, k)
        if res >= 0:
            res += 1
        print(res, end=' ')


if __name__ == "__main__":
    import sys
    main(sys.argv)
