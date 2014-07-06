#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main(argv):
    from ts_logic import TopoligicalSorter

    if len(argv) < 2:
        print("Input file isn't specified. Using test values:")
        print('n = 4')
        n = 4
        print('m = 5')
        m = 5
        print('Graph:')
        graph = [[0 for i in range(n)] for _ in range(n)]
        print('1 2')
        graph[0][1] = 1
        print('3 1')
        graph[2][0] = 1
        print('3 2')
        graph[2][1] = 1
        print('4 3')
        graph[3][2] = 1
        print('4 2')
        graph[3][1] = 1
    else:
        with open(argv[1]) as f:
            line = f.readline()
            n, m = [int(x.strip()) for x in line.strip().split()]
            graph = [[0 for i in range(n)] for _ in range(n)]
            for line in f:
                i, j = [int(x.strip()) for x in line.strip().split()]
                graph[i - 1][j - 1] = 1

    tser = TopoligicalSorter(graph)
    for v in tser.sort():
        print(v + 1, end=' ')


if __name__ == "__main__":
    import sys
    main(sys.argv)
