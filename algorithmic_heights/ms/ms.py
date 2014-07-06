#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main(argv):
    from ms_logic import merge_sort

    if len(argv) < 2:
        print("Input file isn't specified. Using test values:")
        print('n = 10')
        n = 10
        print('A = [20, 19, 35, -18, 17, -20, 20, 1, 4, 4]')
        arr = [20, 19, 35, -18, 17, -20, 20, 1, 4, 4]
    else:
        with open(argv[1]) as f:
            n = int(f.readline().strip())
            arr = [int(x) for x in f.readline().strip().split(' ')]

    for el in merge_sort(arr):
        print(el, end=' ')

if __name__ == "__main__":
    import sys
    main(sys.argv)
