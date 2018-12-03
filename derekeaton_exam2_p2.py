#!/usr/bin/env python3
"""
Python Exam Problem 5
A program that reads in two files and prints out
all words that are common to both in sorted order
"""
from __future__ import print_function


def fileset(filename):
    """
    Takes the name of a file and opens it.
    Read all words and add them to a set.
    Args:
        filename: The name of the file
    Return:
        a set with all unique words in the file
    """
    with open(filename, mode='rt', encoding='utf-8') as reading:
        hold = set()
        for line in reading:
            temp = line.split()
            for item in temp:
                hold.add(item)
        return hold


def main():
    """
    Test your module
    """
    print("Enter the name of a file: ", end='')
    file1 = input()
    print("Enter the name of a file: ", end='')
    file2 = input()
    words1 = fileset(file1)
    words2 = fileset(file2)
    shared = words1.intersection(words2)
    for word in shared:
        print(word)

if __name__ == "__main__":
    main()
    exit(0)
