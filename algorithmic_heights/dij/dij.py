#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main(argv):
    from dij_logic import dijkstra

    if len(argv) < 2:
        print("Input file isn't specified. Using test values:")
        print('n = 6')
        n = 6
        print('n = 10')
        m = 6
        graph = [[0 for _ in range(n)] for _ in range(n)]

        print('Graph:')
        print('3 4 4')
        graph[2][3] = 4
        print('1 2 4')
        graph[0][1] = 4
        print('1 3 2')
        graph[0][2] = 2
        print('2 3 3')
        graph[1][2] = 3
        print('6 3 2')
        graph[5][2] = 2
        print('3 5 5')
        graph[2][4] = 5
        print('5 4 1')
        graph[4][3] = 1
        print('3 2 1')
        graph[2][1] = 1
        print('2 4 2')
        graph[1][3] = 2
        print('2 5 3')
        graph[1][4] = 3
    else:
        with open(argv[1]) as f:
            line = f.readline()
            n, m = [int(x.strip()) for x in line.strip().split()]
            graph = [[0 for _ in range(n)] for _ in range(n)]
            for line in f:
                i, j, w = [int(x.strip()) for x in line.strip().split()]
                graph[i - 1][j - 1] = w

    for el in dijkstra(graph, 0):
        print(el, end=' ')


if __name__ == "__main__":
    import sys
    main(sys.argv)
