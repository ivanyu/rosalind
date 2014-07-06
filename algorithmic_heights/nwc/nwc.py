#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main(argv):
    from nwc_logic import detect_nwc

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
        graph = [[0 for _ in range(n)] for _ in range(n)]
        print('1 4 4')
        graph[0][3] = 4
        print('4 2 3')
        graph[3][1] = 3
        print('2 3 1')
        graph[1][2] = 1
        print('3 1 6')
        graph[2][0] = 6
        print('2 1 -7')
        graph[1][0] = -7
        graphs.append(graph)

        print('Graph 2:')
        print('n = 3')
        n = 3
        print('m = 4')
        m = 4
        graph = [[0 for _ in range(n)] for _ in range(n)]
        print('1 2 -8')
        graph[0][1] = -8
        print('2 3 20')
        graph[1][2] = 20
        print('3 1 -1')
        graph[2][0] = -1
        print('3 2 -30')
        graph[2][1] = -30
        graphs.append(graph)
    else:
        with open(argv[1]) as f:
            k = int(f.readline().strip())

            for _ in range(k):
                # f.readline()

                line = f.readline()
                n, m = [int(x.strip()) for x in line.strip().split()]
                graph = [[0 for _ in range(n)] for _ in range(n)]
                for edge in range(m):
                    line = f.readline()
                    i, j, w = [int(x.strip()) for x in line.strip().split()]
                    graph[i - 1][j - 1] = w
                graphs.append(graph)

    for g in graphs:
        r = detect_nwc(g)
        print('1' if r else '-1', end=' ')


if __name__ == "__main__":
    import sys
    main(sys.argv)
