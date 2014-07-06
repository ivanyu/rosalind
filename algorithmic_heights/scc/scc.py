#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main(argv):
    from scc_logic import SCCCounter

    if len(argv) < 2:
        print("Input file isn't specified. Using test values:")
        print('n = 6')
        n = 6
        print('m = 7')
        m = 7
        print('Graph:')
        graph = [[0 for _ in range(n)] for _ in range(n)]
        print('4 1')
        graph[3][0] = 1
        print('1 2')
        graph[0][1] = 1
        print('2 4')
        graph[1][3] = 1
        print('5 6')
        graph[4][5] = 1
        print('3 2')
        graph[2][1] = 1
        print('5 3')
        graph[4][2] = 1
        print('3 5')
        graph[2][4] = 1
    else:
        with open(argv[1]) as f:
            line = f.readline()
            n, m = [int(x.strip()) for x in line.strip().split()]
            graph = [[0 for _ in range(n)] for _ in range(n)]
            for edge in range(m):
                line = f.readline()
                i, j = [int(x.strip()) for x in line.strip().split()]
                graph[i - 1][j - 1] = 1

    print(SCCCounter(graph).count())


if __name__ == "__main__":
    import sys
    main(sys.argv)
