#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main(argv):
    from par3_logic import partition

    if len(argv) < 2:
        print("Input file isn't specified. Using test values:")
        print('n = 9')
        n = 9
        print('A = [4, 5, 6, 4, 1, 2, 5, 7, 4]')
        arr = [4, 5, 6, 4, 1, 2, 5, 7, 4]
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
