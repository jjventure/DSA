"""
DSA Problem: Find the Fibonacci Number Using Recursion

Problem Statement:
Given a non-negative integer n, return the nth Fibonacci number
using recursion.

The Fibonacci sequence is defined as follows:
    F(0) = 0
    F(1) = 1
    F(n) = F(n - 1) + F(n - 2), for n >= 2

The sequence begins:
    0, 1, 1, 2, 3, 5, 8, 13, 21, ...

Examples:

    Input: n = 0
    Output: 0

    Input: n = 1
    Output: 1

    Input: n = 5
    Output: 5

    Input: n = 7
    Output: 13

Requirements:
1. Use recursion to solve the problem.
2. Use the mathematical definition of the Fibonacci sequence.
3. Define appropriate base cases.
4. Return the nth Fibonacci number.
5. Do not use loops, lists, or iterative approaches to calculate
   the result.

Function Signature:
    def fibonacci(n):

Test Cases:
    fibonacci(0)  -> 0
    fibonacci(1)  -> 1
    fibonacci(2)  -> 1
    fibonacci(5)  -> 5
    fibonacci(7)  -> 13

Complexity Analysis:
    Analyze the time and auxiliary space complexity of your
    recursive solution.
"""

def fibonacci(n):
    if (n == 0) or (n == 1):
        return n 

    return fibonacci(n - 1) + fibonacci(n - 2) 



print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(5))
print(fibonacci(7))


# TC --> O(2^n)
# SC --> O(n)