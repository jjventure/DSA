'''
Q. Character Frequency Queries

Given a string s containing lowercase English letters and a list of
characters q, for each character in q, find and print how many times
that character occurs in the string s.

Example:

s = "azyuyyzaaaa"
q = ["d", "a", "y", "a"]

Expected output:
d -> 0
a -> 5
y -> 3
a -> 5

Constraints:
1. 'a' <= s[i] <= 'z'
2. q contains lowercase English letters.

Goal:
Find an efficient solution to answer the frequency queries.
'''

s = "azyuyyzaaaa"
q = ["d", "a", "y", "a"]

hash_list = [0] * 26 

for char in s:
    ascii_val = ord(char)
    index = ascii_val - ord("a") 
    hash_list[index] += 1 

for char in q:
    ascii_val = ord(char)
    index = ascii_val - ord("a") 
    print(hash_list[index])

# TC --> O(N + M)
# SC --> O(26) --> O(1)  