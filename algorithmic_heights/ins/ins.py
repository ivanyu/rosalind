#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main(argv):
    from sort_logic import InsertionSorter

    if len(argv) < 2:
        print("Input file isn't specified. Using test values:")
        print('n = 6')
        n = 6
        print('A = [6, 10, 4, 5, 1, 2]')
        arr = [6, 10, 4, 5, 1, 2]
    else:
        with open(argv[1]) as f:
            n = int(f.readline().strip())
            arr = [int(x) for x in f.readline().strip().split(' ')]

    sorter = InsertionSorter()
    sorter.insertion_sort(arr)
    print(sorter.swaps_done)

if __name__ == "__main__":
    import sys
    main(sys.argv)
