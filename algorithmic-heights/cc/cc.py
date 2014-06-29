#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main(argv):
    from cc_logic import cc

    if len(argv) < 2:
        print("Input file isn't specified. Using test values:")
        print('n = 12')
        n = 12
        print('m = 13')
        m = 13
        print('Graph:')
        graph = [[] for _ in range(n)]
        print('1 2')
        graph[0].append(1)
        graph[1].append(0)
        print('1 5')
        graph[0].append(4)
        graph[4].append(0)
        print('5 9')
        graph[4].append(8)
        graph[8].append(4)
        print('5 10')
        graph[4].append(9)
        graph[9].append(4)
        print('9 10')
        graph[8].append(9)
        graph[9].append(8)
        print('3 4')
        graph[2].append(3)
        graph[3].append(2)
        print('3 7')
        graph[2].append(6)
        graph[6].append(2)
        print('3 8')
        graph[2].append(7)
        graph[7].append(2)
        print('4 8')
        graph[3].append(7)
        graph[7].append(3)
        print('7 11')
        graph[6].append(10)
        graph[10].append(6)
        print('8 11')
        graph[7].append(10)
        graph[10].append(7)
        print('11 12')
        graph[10].append(11)
        graph[11].append(10)
        print('8 12')
        graph[7].append(11)
        graph[11].append(7)
    else:
        with open(argv[1]) as f:
            line = f.readline()
            n, m = [int(x.strip()) for x in line.strip().split()]
            graph = [[] for _ in range(n)]
            for edge in range(m):
                line = f.readline()
                i, j = [int(x.strip()) for x in line.strip().split()]
                graph[i - 1].append(j - 1)
                graph[j - 1].append(i - 1)

    print(cc(graph))


if __name__ == "__main__":
    import sys
    main(sys.argv)
