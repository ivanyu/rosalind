#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main(argv):
    from qs_logic import quick_sort

    if len(argv) < 2:
        print("Input file isn't specified. Using test values:")
        print('k = 7')
        k = 7
        print('A = [5, -2, 4, 7, 8, -10, 11]')
        arr = [5, -2, 4, 7, 8, -10, 11]
    else:
        with open(argv[1]) as f:
            k = int(f.readline().strip())
            arr = [int(x) for x in f.readline().strip().split(' ')]

    quick_sort(arr)
    for el in arr:
        print(el, end=' ')


if __name__ == "__main__":
    import sys
    main(sys.argv)
