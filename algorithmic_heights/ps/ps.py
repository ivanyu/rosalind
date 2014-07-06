#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main(argv):
    from ps_logic import partial_sort

    if len(argv) < 2:
        print("Input file isn't specified. Using test values:")
        print('n = 10')
        n = 10
        print('A = [4, -6, 7, 8, -9, 100, 12, 13, 56, 17]')
        arr = [4, -6, 7, 8, -9, 100, 12, 13, 56, 17]
        print('k = 3')
        k = 3
    else:
        with open(argv[1]) as f:
            n = int(f.readline().strip())
            arr = [int(x) for x in f.readline().split(' ')]
            k = int(f.readline().strip())

    result = partial_sort(arr, k)
    for el in result:
        print(el, end=' ')
    pass

if __name__ == "__main__":
    import sys
    main(sys.argv)
