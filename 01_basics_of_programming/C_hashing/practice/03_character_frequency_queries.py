'''
Q3. Character Frequency Queries

Given a string s containing lowercase English letters and a list
of character queries, find and print how many times each queried
character occurs in s.

Example:

s = "datascience"
queries = ["a", "e", "t", "z", "c"]

Expected output:
a -> 2
e -> 2
t -> 1
z -> 0
c -> 2

Constraints:
1. s contains only lowercase English letters.
2. queries contains only lowercase English letters.
3. Both s and queries can contain a large number of elements.

Goal:
Use character hashing to answer the queries efficiently.
'''
s = "datascience"
queries = ["a", "e", "t", "z", "c"]

hash_list = [0] * 26 

# building hash_list
for char in s:
    ascii_val = ord(char)
    index = ascii_val - ord("a")
    hash_list[index] += 1 

# Querying the hash_list with index
for char in queries:
    ascii_val = ord(char)
    index = ascii_val - ord("a")
    print(hash_list[index])


# TC --> O(n + m)
# SC --> O(26) --> O(1) | It always contains 26 elements, regardless of how many unique characters are in queries.