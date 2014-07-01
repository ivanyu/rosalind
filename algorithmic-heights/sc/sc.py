#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main(argv):
    from sc_logic import check_semi_connectedness

    graphs = []
    if len(argv) < 2:
        print('k = 2')
        k = 2

        print('Graph 1:')
        print('n = 3')
        n = 3
        print('m = 2')
        m = 2
        g = [[0 for i in range(n)] for _ in range(n)]
        print('3 2')
        g[2][1] = 1
        print('2 1')
        g[1][0] = 1
        graphs.append(g)

        print('Graph 2:')
        print('n = 3')
        n = 3
        print('m = 2')
        m = 2
        g = [[0 for i in range(n)] for _ in range(n)]
        print('3 2')
        g[2][1] = 1
        print('1 2')
        g[0][1] = 1
        graphs.append(g)
    else:
        with open(argv[1]) as f:
            k = int(f.readline().strip())

            for _ in range(k):
                f.readline()

                line = f.readline()
                n, m = [int(x.strip()) for x in line.strip().split()]
                g = [[0 for _ in range(n)] for _ in range(n)]
                for edge in range(m):
                    line = f.readline()
                    i, j = [int(x.strip()) for x in line.strip().split()]
                    g[i - 1][j - 1] = 1
                graphs.append(g)

    for g in graphs:
        r = check_semi_connectedness(g)
        print('1' if r else -1, end=' ')


if __name__ == "__main__":
    import sys
    main(sys.argv)
