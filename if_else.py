"""
Created on Tue Nov  3, 2020
https://www.hackerrank.com/challenges/py-if-else/problem

"""

if __name__ == '__main__':
    n = int(input().strip())

def weird(n):
    assert n in range(1,101)
    if n % 2 == 0 and (n > 20 or n in range(2,6)):
        print("Not Weird")
    else:
        print("Weird")

weird(n)
