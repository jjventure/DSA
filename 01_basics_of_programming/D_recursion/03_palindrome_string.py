"""
DSA Problem: Check Whether a String Is a Palindrome Using Recursion

Problem Statement:
Given a string, determine whether it is a palindrome using recursion.

A palindrome is a string that reads the same forward and backward.

Examples:
    Input:  "madam"
    Output: True

    Input:  "racecar"
    Output: True

    Input:  "hello"
    Output: False

    Input:  "abba"
    Output: True

Requirements:
1. Use recursion to solve the problem.
2. Use two pointers, left and right, to compare characters
   from opposite ends of the string.
3. If the characters at left and right do not match,
   the string is not a palindrome.
4. If the pointers meet or cross, the string is a palindrome.
5. Do not use string slicing, reversed(), or other built-in
   methods to reverse the string.

Function Signature:
    def is_palindrome(string, left, right):

Test Cases:
    is_palindrome("madam", 0, 4)   -> True
    is_palindrome("racecar", 0, 6) -> True
    is_palindrome("hello", 0, 4)   -> False
    is_palindrome("abba", 0, 3)    -> True
"""

def is_palindrome(string, left, right):
    """ Checks if the string is palindrome or not. """

    if left >= right:
        return True

    if string[left] != string[right]:
        return False

    return is_palindrome(string, left + 1, right - 1)


print(is_palindrome("madam", 0, 4))
print(is_palindrome("racecar", 0, 6)) 
print(is_palindrome("hello", 0, 4))   
print(is_palindrome("abba", 0, 3))    

# TC --> O(n), n = len(string)
# SC --> O(n), n = stack space 