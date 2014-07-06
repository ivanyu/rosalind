#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main(argv):
    from sdag_logic import shortest_paths

    if len(argv) < 2:
        print("Input file isn't specified. Using test values:")
        print('n = 5')
        n = 5
        print('m = 6')
        m = 6
        print('Graph:')
        graph = [[] for _ in range(n)]
        print('2 3 4')
        graph[1].append((2, 4))
        print('4 3 -2')
        graph[3].append((2, -2))
        print('1 4 1')
        graph[0].append((3, 1))
        print('1 5 -3')
        graph[0].append((4, -3))
        print('2 4 -2')
        graph[1].append((3, -2))
        print('5 4 1')
        graph[4].append((3, 1))
    else:
        with open(argv[1]) as f:
            line = f.readline()
            n, m = [int(x.strip()) for x in line.strip().split()]
            graph = [[] for _ in range(n)]
            for edge in range(m):
                line = f.readline()
                i, j, w = [int(x.strip()) for x in line.strip().split()]
                graph[i - 1].append((j - 1, w))

    for el in shortest_paths(graph, 0):
        print(el if (el is not None) else 'x', end=' ')


if __name__ == "__main__":
    import sys
    main(sys.argv)
