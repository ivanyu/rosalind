#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main(argv):
    from mer_logic import merge

    if len(argv) < 2:
        print("Input file isn't specified. Using test values:")
        print('n = 4')
        n = 4
        print('A = [2, 4, 10, 18]')
        a1 = [2, 4, 10, 18]
        print('m = 3')
        m = 3
        print('B = [-5, 11, 12]')
        a2 = [-5, 11, 12]
    else:
        with open(argv[1]) as f:
            n = int(f.readline().strip())
            a1 = [int(x) for x in f.readline().strip().split(' ')]
            m = int(f.readline().strip())
            a2 = [int(x) for x in f.readline().strip().split(' ')]
    for el in merge(a1, a2):
        print(el, end=' ')

if __name__ == "__main__":
    import sys
    main(sys.argv)
