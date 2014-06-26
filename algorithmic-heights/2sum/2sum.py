#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main(argv):
    from find_2sum_logic import find_2sum

    arrays = []
    if len(argv) < 2:
        print("Input file isn't specified. Using test values:")
        print('k = 4')
        k = 4
        print('n = 5')
        n = 5
        print('A1 = [2, -3, 4, 10, 5]')
        arrays.append([2, -3, 4, 10, 5])
        print('A2 = [8, 2, 4, -2, -8]')
        arrays.append([8, 2, 4, -2, -8])
        print('A3 = [-5, 2, 3, 2, -4]')
        arrays.append([-5, 2, 3, 2, -4])
        print('A4 = [5, 4, -5, 6, 8]')
        arrays.append([5, 4, -5, 6, 8])
    else:
        with open(argv[1]) as f:
            line = f.readline().strip()
            k, n = [int(x.strip()) for x in line.split(' ')]
            for _ in range(k):
                line = f.readline().strip()
                if not line:
                    break
                a = [int(x) for x in line.split(' ')]
                arrays.append(a)

    for a in arrays:
        r = find_2sum(a)
        if r == -1:
            print(-1)
        else:
            print('{0} {1}'.format(r[0] + 1, r[1] + 1))

if __name__ == "__main__":
    import sys
    main(sys.argv)
