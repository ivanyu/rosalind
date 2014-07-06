#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Fibo:
    def __init__(self):
        self.memo = dict()

    def calc(self, n):
        if n == 1 or n == 0:
            return n

        if n in self.memo:
            return self.memo[n]

        val = self.calc(n - 1) + self.calc(n - 2)
        self.memo[n] = val
        return val


def main(argv):
    if len(argv) < 2:
        print("Input value isn't specified. Using test value n = 6.")
        n = 6
    else:
        n = int(argv[1])

    print(Fibo().calc(n))


if __name__ == "__main__":
    import sys
    main(sys.argv)
