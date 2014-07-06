#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main(argv):
    from hs_logic import heap_sort

    if len(argv) < 2:
        print("Input file isn't specified. Using test values:")
        print('n = 9')
        n = 5
        print('A = [2, 6, 7, 1, 3, 5, 4, 8, 9]')
        arr = [2, 6, 7, 1, 3, 5, 4, 8, 9]
    else:
        with open(argv[1]) as f:
            n = int(f.readline().strip())
            arr = [int(x) for x in f.readline().split(' ')]

    heap_sort(arr)
    for el in arr:
        print(el, end=' ')
    pass

if __name__ == "__main__":
    import sys
    main(sys.argv)
