'''
Q5. Find the Least Frequent Element

Given a list of integers, find the element that occurs
the least number of times.

Example:

nums = [4, 4, 2, 2, 2, 7, 7, 9]

Expected output:
9

Explanation:
4 occurs 2 times.
2 occurs 3 times.
7 occurs 2 times.
9 occurs 1 time.

Therefore, 9 is the least frequent element.

Constraints:
1. nums contains integers.
2. nums can contain a large number of elements.

Goal:
Use a frequency-based approach to find the least frequent
element efficiently.
'''

frequency = {}

nums = [4, 4, 2, 2, 2, 7, 7, 9]

# Building the frequency dictionary 
for num in nums:
    if num in frequency:
        frequency[num] += 1 
    else:
        frequency[num] = 1 

first_num, first_count = next(iter(frequency.items()))
least_frequent_element = first_num
least_frequent_count = first_count 

# finding the least frequent element from the dictionary we built
for num, count in frequency.items():
    if count < least_frequent_count:
        least_frequent_count = count 
        least_frequent_element = num 

print(least_frequent_element)


# TC --> O(n + k) ~ O(n)
# SC --> O(k)