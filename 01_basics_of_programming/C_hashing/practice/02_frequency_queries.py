'''
Q2. Frequency Queries

Given a list of integers nums and a list of query values,
for each value in queries, find and print how many times
that value occurs in nums.

Example:

nums = [1, 3, 2, 1, 4, 3, 1, 2]
queries = [1, 2, 5, 3]

Expected output:
1 -> 3
2 -> 2
5 -> 0
3 -> 2

Constraints:
1. nums and queries contain integers.
2. Both lists can contain a large number of elements.

Goal:
Use a frequency-based approach to answer the queries efficiently.
'''

nums = [1, 3, 2, 1, 4, 3, 1, 2]
queries = [1, 2, 5, 3]

# Build frequency dictionary from nums 
frequency = {}

for num in nums:
    if num not in frequency:
        frequency[num] = 1 
    else:
        frequency[num] += 1 

# Query dictionary for every element in queries
for element in queries:
    if element not in frequency:
        print(0)
    else:
        print(frequency[element])

# TC --> O(n + m)
# SC --> O(k) - where k = number of unique values in nums.