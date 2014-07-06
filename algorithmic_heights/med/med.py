#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main(argv):
    from med_logic import order_statistic

    if len(argv) < 2:
        print("Input file isn't specified. Using test values:")
        print('n = 11')
        n = 11
        print('A = [2, 36, 5, 21, 8, 13, 11, 20, 5, 4, 1]')
        arr = [2, 36, 5, 21, 8, 13, 11, 20, 5, 4, 1]
        print('k = 8')
        k = 8
    else:
        with open(argv[1]) as f:
            n = int(f.readline().strip())
            arr = [int(x) for x in f.readline().strip().split(' ')]
            k = int(f.readline().strip())

    actual_k = k - 1
    result = order_statistic(arr, actual_k)
    print(result)


if __name__ == "__main__":
    import sys
    main(sys.argv)
