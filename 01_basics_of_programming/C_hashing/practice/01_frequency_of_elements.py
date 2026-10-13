'''
Q1. Frequency of Elements

Given a list of integers, find and print the frequency
of every unique element.

Example:
nums = [4, 2, 4, 3, 2, 4, 5, 3]

Expected output:
4 -> 3
2 -> 2
3 -> 2
5 -> 1
'''

nums = [4, 2, 4, 3, 2, 4, 5, 3]

frequency = {}

for num in nums:
    if num not in frequency:
        frequency[num] = 1
    else:
        frequency[num] += 1

print(frequency)

# TC --> O(n)
# SC --> O(k) - where k = number of unique elements 