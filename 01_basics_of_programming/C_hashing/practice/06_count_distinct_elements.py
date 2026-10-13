'''
Q6. Count Distinct Elements

Given a list of integers, find the total number of distinct
(unique) elements present in the list.

Example:

nums = [1, 2, 2, 3, 4, 4, 5, 5, 5]

Expected output:
5

Explanation:

The distinct elements are:
1, 2, 3, 4, 5

Therefore, there are 5 distinct elements.

Constraints:
1. nums contains integers.
2. nums can contain a large number of elements.

Goal:
Use a hashing-based approach to efficiently count the number
of distinct elements.
'''

# nums = [1, 2, 2, 3, 4, 4, 5, 5, 5]

# count = 0 
# hash_list = []

# for num in nums:
#     if num not in hash_list:
#         hash_list.append(num)
#         count += 1 

# print(count)


# TC --> O(n x k) ~ O(n^2)
# SC --> O(k)


# Using dictionary-based approach
nums = [1, 2, 2, 3, 4, 4, 5, 5, 5]

seen = {}
count = 0

for num in nums:
    if num not in seen:
        seen[num] = True 
        count += 1 

print(count)

# TC --> O(n)
# SC --> O(k)

''' 
Key takeaway from this problem: lookup for: 
                                            list --> O(k)
                                            dict --> O(1) 
'''