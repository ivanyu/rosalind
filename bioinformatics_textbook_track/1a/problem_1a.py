#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main(argv):
    if len(argv) < 2:
        print("Input file name isn't specified. Using test data.")
        string_to_examine = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
        k = 4
    else:
        with open(argv[1]) as f:
            string_to_examine = f.readline()
            k = int(f.readline())

    from problem_logic import find_most_frequent_k_measures

    for km in find_most_frequent_k_measures(string_to_examine, k):
        print(km, end=' ')


if __name__ == "__main__":
    import sys
    main(sys.argv)
