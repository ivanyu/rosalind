#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main(argv):
    from sq_logic import detect_sq_cycles

    graphs = []
    if len(argv) < 2:
        print("Input file isn't specified. Using test values:")
        print('k = 2')
        k = 2

        print('Graph 1:')
        print('n = 4')
        n = 4
        print('m = 5')
        m = 5
        g = [[0 for i in range(n)] for _ in range(n)]
        print('3 4')
        g[2][3] = 1
        g[3][2] = 1
        print('4 2')
        g[3][1] = 1
        g[1][3] = 1
        print('3 2')
        g[2][1] = 1
        g[1][2] = 1
        print('3 1')
        g[2][0] = 1
        g[0][2] = 1
        print('1 2')
        g[0][1] = 1
        g[1][0] = 1
        graphs.append(g)

        print('Graph 2:')
        print('n = 4')
        n = 4
        print('m = 4')
        m = 4
        g = [[0 for i in range(n)] for _ in range(n)]
        print('1 2')
        g[0][1] = 1
        g[1][0] = 1
        print('3 4')
        g[2][3] = 1
        g[3][2] = 1
        print('2 4')
        g[1][3] = 1
        g[3][1] = 1
        print('4 1')
        g[3][0] = 1
        g[0][3] = 1
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
                    g[j - 1][i - 1] = 1
                graphs.append(g)

    for g in graphs:
        r = detect_sq_cycles(g)
        print(1 if r else -1, end=' ')


if __name__ == "__main__":
    import sys
    main(sys.argv)
