'''Q9 — Character Frequency Comparison

Problem
Given two strings, determine whether they contain exactly the same characters with the same frequencies.

Example 1:
s1 = "listen"
s2 = "silent"

Expected output:
True

Both strings contain the same characters with identical frequencies. Their order doesn't matter.

Example 2:

s1 = "hello"
s2 = "world"

Expected output:
False

The strings contain different characters and frequencies.

Example 3:
s1 = "aabbc"
s2 = "abbbc"

Expected output:
False

Both strings have five characters, but their character frequencies differ.

Constraints:
Both strings contain lowercase English letters (a-z).
Character order doesn't matter.
Character frequencies must match exactly.
Don't use sorted() or Counter().

Your goal 🎯
Use the character-hashing technique you've practiced in Q3, Q7, and Q8.'''

# Solution:
'''
1) Check whether the strings have different lengths.
2) Build both frequency tables.
3) Compare the corresponding frequencies.
4) Produce True or False.

'''

s1 = "abc"
s2 = "ab"

# check whether the strings have different lengths
if len(s1) != len(s2):
    print("False")

else:
    # build both frequency tables
    hash_list_s1 = [0] * 26
    hash_list_s2 = [0] * 26

    for char in s1:
        index = ord(char) - ord("a")
        hash_list_s1[index] += 1

    for char in s2:
        index = ord(char) - ord("a")
        hash_list_s2[index] += 1 


    # compare the corresponding frequencies 
    for index in range(0, 26):
        if hash_list_s1[index] != hash_list_s2[index]:
            print("False")
            break 
    else:
        print("True")



# TC --> O(m + n)
# SC --> O(1)