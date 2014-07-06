#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main(argv):
    from bfs_logic import bfs

    if len(argv) < 2:
        print("Input file isn't specified. Using test values:")
        print('n = 6')
        n = 6
        print('n = 6')
        m = 6
        graph = [[0 for _ in range(n)] for _ in range(n)]

        print('Graph:')
        print('4 6')
        graph[3][5] = 1
        graph[5][3] = -1
        print('6 5')
        graph[5][4] = 1
        graph[4][5] = -1
        print('4 3')
        graph[3][2] = 1
        graph[2][3] = -1
        print('3 5')
        graph[2][4] = 1
        graph[4][2] = -1
        print('2 1')
        graph[1][0] = 1
        graph[0][1] = -1
        print('1 4')
        graph[0][3] = 1
        graph[3][0] = -1
    else:
        with open(argv[1]) as f:
            line = f.readline()
            n, m = [int(x.strip()) for x in line.strip().split()]
            graph = [[0 for _ in range(n)] for _ in range(n)]
            for line in f:
                i, j = [int(x.strip()) for x in line.strip().split()]
                graph[i - 1][j - 1] = 1
                # If edge is set it cannot be unset.
                if graph[j - 1][i - 1] != 1:
                    graph[j - 1][i - 1] = -1

    for el in bfs(graph, 0):
        print(el, end=' ')


if __name__ == "__main__":
    import sys
    main(sys.argv)
