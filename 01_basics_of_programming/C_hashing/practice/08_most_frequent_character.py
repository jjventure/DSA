''' Q8 — Most Frequent Character

Given a string, find the character that occurs most frequently.

Input:
s = "banana"

Expected output:
a

Explanation:

a → 3 occurrences
n → 2 occurrences
b → 1 occurrence

Constraints:

The string contains lowercase English letters.
If multiple characters tie for the highest frequency, return the one that appears first in the string.

Goal: Use character hashing.'''

s = "banana"

highest_frequency = 0 

# build the frequency table 
hash_list = [0] * 26

for char in s:
    index = ord(char) - ord("a")
    hash_list[index] += 1 

# Find the highest frequency
for frequency in hash_list:
    if frequency > highest_frequency:
        highest_frequency = frequency

# iterate through "s" from left to right 
for char in s:
    index = ord(char) - ord("a")

    if hash_list[index] == highest_frequency:
        highest_frequency_character = char 
        break 

print(highest_frequency_character)


# TC --> O(n)
# SC --> O(1)