'''Q. # For each element in list m, find and print how many times that element occurs in list n.

Given two lists of integers, m and n:

n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]

For each element in m, find and print how many times that
element occurs in n.

Example:

n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]

Expected output:
10  -> 1
111 -> 0
1   -> 1
9   -> 0
5   -> 4
67  -> 0
2   -> 2

Constraints:
1. Both m and n can contain up to 10^8 elements.
2. The elements of m and n are integers.

Goal:
Find an efficient solution that can handle very large lists.'''

n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]

# Brute-force solution:
# for num in m:
#     count = 0 
#     for x in n:
#         if x == num:
#             count += 1 

#     print(count)



# Improved solution | Using a dictionary for frequency counting
# frequency = {}

# # building dictionary 
# for num in n:
#     if num not in frequency:
#         frequency[num] = 1 
#     else:
#         frequency[num] += 1 

# # Querying dictionary
# for x in m:
#     if x in frequency:
#         print(frequency[x])
#     else:
#         print(0)



# Optimal solution 
hash_list = [0] * 11 

for num in n:
    hash_list[num] += 1

for num in m:
    if (num < 1) or (num > 10):
        print(0)

    else:
        print(hash_list[num])