# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 10:16:10 2020

@author: Dmitry
https://www.hackerrank.com/challenges/merge-the-tools/problem

Example: in: AABCAAADA 3
         out: AB CA AD
"""


def merge_the_tools(string, k):
    while len(string) > 0:
        substr = string[:k]
        merge = ''
        for i in substr:
            if i not in merge:
                merge += i
        string = string[k:]
        print(merge)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
