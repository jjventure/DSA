'''
Q4. Find the Most Frequent Element

Given a list of integers, find the element that occurs
the most number of times.

Example:

nums = [2, 5, 2, 3, 5, 2, 4, 5, 5]

Expected output:
5

Explanation:
2 occurs 3 times.
3 occurs 1 time.
4 occurs 1 time.
5 occurs 4 times.

Therefore, 5 is the most frequent element.

Constraints:
1. nums contains integers.
2. nums can contain a large number of elements.

Goal:
Use a frequency-based approach to find the most frequent element
efficiently.
'''

# dictionary-based approach
frequency = {}

highest_frequency = 0 
most_frequent = 0 

nums = [2, 5, 2, 3, 5, 2, 4, 5, 5]

# building the dictionary
for num in nums:
    if num in frequency:
        frequency[num] += 1 
    else:
        frequency[num] = 1 

# finding the most frequent element 
for num, count in frequency.items():
    if count > highest_frequency:
        highest_frequency = count 
        most_frequent = num 

print(most_frequent) 

# TC --> O(n + k) --> O(n)
# SC --> O(k) | where k = number of unqiue elements. 