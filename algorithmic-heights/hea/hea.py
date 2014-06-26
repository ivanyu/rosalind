#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main(argv):
    from hea_logic import build_heap

    if len(argv) < 2:
        print("Input file isn't specified. Using test values:")
        print('n = 5')
        n = 5
        print('A = [1, 3, 5, 7, 2]')
        arr = [1, 3, 5, 7, 2]
    else:
        with open(argv[1]) as f:
            n = int(f.readline().strip())
            arr = [int(x) for x in f.readline().split(' ')]

    build_heap(arr)
    for el in arr:
        print(el, end=' ')

if __name__ == "__main__":
    import sys
    main(sys.argv)
