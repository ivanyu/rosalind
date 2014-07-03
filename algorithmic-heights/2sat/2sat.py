#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main(argv):
    import sys
    from check_2sat_logic import try_satisfy

    sys.setrecursionlimit(10000)

    expressions = []
    if len(argv) < 2:
        print('k = 2')
        k = 2

        print('Clause 1: '
              '(x1 or x2) and (-x1 or x2) and (x1 or -x2) and (-x1 or -x2)')
        expressions.append((2, [(1, 2), (-1, 2), (1, -2), (-1, -2)]))

        print('Clause 2: '
              '(x1 or x2) and (x2 or x3) and (-x1 or -x2) and (-x2 or -x3)')
        expressions.append((3, [(1, 2), (2, 3), (-1, -2), (-2, -3)]))
    else:
        with open(argv[1]) as f:
            k = int(f.readline().strip())

            for _ in range(k):
                f.readline()

                line = f.readline()
                n, m = [int(x.strip()) for x in line.strip().split()]
                clauses = []
                for edge in range(m):
                    line = f.readline()
                    i, j = [int(x.strip()) for x in line.strip().split()]
                    clauses.append((i, j))
                expressions.append((n, clauses))

    for n, exp in expressions:
        r = try_satisfy(n, exp)
        if r == 0:
            print('0')
        else:
            print('1', end=' ')
            for i, el in enumerate(r):
                if el == False:
                    print('-', end='')
                print(i + 1, end=' ')
            print('')


if __name__ == "__main__":
    import sys
    main(sys.argv)
