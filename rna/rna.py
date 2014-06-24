#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main(argv):
    if len(argv) < 2:
        print("Input file name isn't specified. Using test input line.")
        input_line = 'GATGGAACTTGACTACGTAAATT'
    else:
        with open(argv[1]) as f:
            input_line = f.readline()

    result = input_line.replace('T', 'U')
    print(result)


if __name__ == "__main__":
    import sys
    main(sys.argv)
