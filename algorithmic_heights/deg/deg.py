#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main(argv):
    from deg_logic import degrees

    if len(argv) < 2:
        print("Input file isn't specified. Using test values:")
        print('n = 6')
        n = 6
        print('n = 7')
        m = 7
        graph = [[0 for _ in range(n)] for _ in range(n)]

        print('Graph:')
        print('1 2')
        graph[0][1] = 1
        graph[1][0] = 1
        print('2 3')
        graph[1][2] = 1
        graph[2][1] = 1
        print('6 3')
        graph[5][2] = 1
        graph[2][5] = 1
        print('5 6')
        graph[4][5] = 1
        graph[5][4] = 1
        print('2 5')
        graph[1][4] = 1
        graph[4][1] = 1
        print('2 4')
        graph[1][3] = 1
        graph[3][1] = 1
        print('4 1')
        graph[3][0] = 1
        graph[0][3] = 1
    else:
        with open(argv[1]) as f:
            line = f.readline()
            n, m = [int(x.strip()) for x in line.strip().split()]
            graph = [[0 for _ in range(n)] for _ in range(n)]
            for line in f:
                i, j = [int(x.strip()) for x in line.strip().split()]
                graph[i - 1][j - 1] = 1
                graph[j - 1][i - 1] = 1

    for el in degrees(graph):
        print(el, end=' ')


if __name__ == "__main__":
    import sys
    main(sys.argv)
