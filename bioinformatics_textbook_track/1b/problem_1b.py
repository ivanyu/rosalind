#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main(argv):
    if len(argv) < 2:
        print("Input file name isn't specified. Using test data.")
        s = 'AAAACCCGGT'
    else:
        with open(argv[1]) as f:
            s = f.readline().strip()

    from problem_logic import get_reverse_complement

    print(get_reverse_complement(s))


if __name__ == "__main__":
    import sys
    main(sys.argv)
