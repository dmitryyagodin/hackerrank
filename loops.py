"""
Created on Tue Nov  3 23:43:18 2020

@author: Dmitry
https://www.hackerrank.com/challenges/python-loops/problem

Task: The provided code stub reads an integer, n, from STDIN.
For all non-negative integers i < n, print i^2.
"""


if __name__ == '__main__':
    n = int(input())

for i in range(n):
    print(i**2)
