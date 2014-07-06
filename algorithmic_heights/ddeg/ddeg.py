#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main(argv):
    from ddeg_logic import double_degrees

    if len(argv) < 2:
        print("Input file isn't specified. Using test values:")
        print('n = 5')
        n = 5
        print('n = 4')
        m = 4
        graph = [[] for _ in range(n)]

        print('Graph:')
        print('1 2')
        graph[0].append(1)
        graph[1].append(0)
        print('2 3')
        graph[1].append(2)
        graph[2].append(1)
        print('4 3')
        graph[3].append(2)
        graph[2].append(3)
        print('2 4')
        graph[1].append(3)
        graph[3].append(1)
    else:
        with open(argv[1]) as f:
            line = f.readline()
            n, m = [int(x.strip()) for x in line.strip().split()]
            graph = [[] for _ in range(n)]
            for line in f:
                i, j = [int(x.strip()) for x in line.strip().split()]
                graph[i - 1].append(j - 1)
                graph[j - 1].append(i - 1)

    for el in double_degrees(graph):
        print(el, end=' ')


if __name__ == "__main__":
    import sys
    main(sys.argv)
