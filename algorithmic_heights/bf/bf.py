#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main(argv):
    from bf_logic import bf

    if len(argv) < 2:
        print("Input file isn't specified. Using test values:")
        print('n = 9')
        n = 9
        print('m = 13')
        m = 13
        print('Graph:')
        graph = [[0 for _ in range(n)] for _ in range(n)]
        print('1 2 10')
        graph[0][1] = 10
        print('3 2 1')
        graph[2][1] = 1
        print('3 4 1')
        graph[2][3] = 1
        print('4 5 3')
        graph[3][4] = 3
        print('5 6 -1')
        graph[4][5] = -1
        print('7 6 -1')
        graph[6][5] = -1
        print('8 7 1')
        graph[7][6] = 1
        print('1 8 8')
        graph[0][7] = 8
        print('7 2 -4')
        graph[6][1] = -4
        print('2 6 2')
        graph[1][5] = 2
        print('6 3 -2')
        graph[5][2] = -2
        print('9 5 -10')
        graph[8][4] = -10
        print('9 4 7')
        graph[8][3] = 7
    else:
        with open(argv[1]) as f:
            line = f.readline()
            n, m = [int(x.strip()) for x in line.strip().split()]
            graph = [[0 for _ in range(n)] for _ in range(n)]
            for line in f:
                i, j, w = [int(x.strip()) for x in line.strip().split()]
                graph[i - 1][j - 1] = w

    for el in bf(graph, 0):
        to_print = el if (el is not None) else 'x'
        print(to_print, end=' ')


if __name__ == "__main__":
    import sys
    main(sys.argv)
