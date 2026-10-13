'''

Q10 — First Non-Repeating Character

Problem
Given a string, find the first character that appears exactly once.

Example 1
s = "swiss"

Expected output:
w

Explanation:

Character	Frequency
    s	        3
    w	        1
    i	        1

Although both w and i appear once, w comes first in the original string.

Example 2
s = "aabbcddee"

Expected output:
c

c is the first character that appears exactly once.

Example 3
s = "aabb"

Expected output:
None

Every character appears more than once, so no non-repeating character exists.

Constraints:
The string contains lowercase English letters (a-z).
Return the first non-repeating character, respecting the original string's order.
If no such character exists, return None.
Don't use Counter().

Your goal 🎯
Use character hashing, just as you did in Q7, Q8, and Q9.
Try writing this as a function, since we discussed practicing functions for problems that return an answer.

'''

# Pseudocode:
'''

1) Build the frequency table.
2) loop through s | get the index of the char | if hash_list[index] == 1: return char

'''

def first_non_repeating_character(string:str):

    hash_list = [0] * 26 

    for char in string:
        index = ord(char) - ord("a")
        hash_list[index] += 1 

    for char in string:
        index = ord(char) - ord("a")
        if hash_list[index] == 1:
            return char 
        
    return None 


print(first_non_repeating_character("swiss"))
print(first_non_repeating_character("aabbcddee"))
print(first_non_repeating_character("aabb"))