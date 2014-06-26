#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main(argv):
    from inv_logic import InversionsCounter

    if len(argv) < 2:
        print("Input file isn't specified. Using test values:")
        print('n = 5')
        n = 5
        print('A = [-6, 1, 15, 8, 10]')
        arr = [-6, 1, 15, 8, 10]
    else:
        with open(argv[1]) as f:
            n = int(f.readline().strip())
            arr = [int(x) for x in f.readline().strip().split(' ')]

    inv_cnt = InversionsCounter()
    print(inv_cnt.count(arr))

    pass

if __name__ == "__main__":
    import sys
    main(sys.argv)
