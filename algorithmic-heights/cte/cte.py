#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main(argv):
    from cte_logic import cte

    graphs = []
    edges_of_interest = []
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
        print('2 4 2')
        graph[1][3] = 2
        edges_of_interest.append((1, 3))
        print('3 2 1')
        graph[2][1] = 1
        print('1 3 2')
        graph[0][2] = 2
        print('1 4 3')
        graph[1][3] = 3
        print('2 1 10')
        graph[1][0] = 10
        print('1 3 4')
        graph[0][2] = 3
        graphs.append(graph)

        print('Graph 2:')
        print('n = 4')
        n = 4
        print('m = 5')
        m = 5
        graph = [[0 for _ in range(n)] for _ in range(n)]
        print('3 2 1')
        graph[2][1] = 1
        edges_of_interest.append((2, 1))
        print('2 4 2')
        graph[1][3] = 2
        print('4 1 3')
        graph[3][0] = 3
        print('2 1 10')
        graph[1][0] = 10
        print('1 3 4')
        graph[0][2] = 4
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
                    if edge == 0:
                        edges_of_interest.append((i - 1, j - 1))
                graphs.append(graph)

    for g, (a, b) in zip(graphs, edges_of_interest):
        print(cte(g, a, b), end=' ')


if __name__ == "__main__":
    import sys
    main(sys.argv)
