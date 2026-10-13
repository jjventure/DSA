''' Q7 — Count Vowels

Write a program that counts how many vowels are present in a string.

Problem:
s = "datascience"

Expected output:
5

Because the vowels are:
a, a, i, e, e

Constraints:
1. Input contains a string.
2. Consider the vowels: a, e, i, o, u.
For now, assume the string contains lowercase letters.

Goal:
Use character hashing.

Don't use set() yet.
'''
s = "datascience"
vowels = ["a", "e", "i", "o", "u"]

count = 0 
hash_list = [0] * 26 

# Build the frequency table 
for char in s:
    index = ord(char) - ord("a")
    hash_list[index] += 1 

# count how many vowels are present in string: s
for char in vowels:
    index = ord(char) - ord("a")
    count += hash_list[index]

print(count)

# TC --> O(n)
# SC --> O(1)