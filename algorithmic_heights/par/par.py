#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main(argv):
    from par_logic import partition

    if len(argv) < 2:
        print("Input file isn't specified. Using test values:")
        print('n = 9')
        n = 9
        print('A = [7, 2, 5, 6, 1, 3, 9, 4, 8]')
        arr = [7, 2, 5, 6, 1, 3, 9, 4, 8]
    else:
        with open(argv[1]) as f:
            n = int(f.readline().strip())
            arr = [int(x) for x in f.readline().strip().split(' ')]

    partition(arr)
    for el in arr:
        print(el, end=' ')


if __name__ == "__main__":
    import sys
    main(sys.argv)
