"""
Task
The provided code stub reads two integers from STDIN, a and b.
Add code to print three lines where:

1. The first line contains the sum of the two numbers.
2. The second line contains the difference of the two numbers (first - second).
3. The third line contains the product of the two numbers.

Created on Tue Nov  3 23:30:43 2020

@author: Dmitry

"""


if __name__ == '__main__':
    a = int(input())
    b = int(input())

def arithmetic(a, b):
    return print(a + b, a - b, a * b, sep='\n')

arithmetic(a, b)
