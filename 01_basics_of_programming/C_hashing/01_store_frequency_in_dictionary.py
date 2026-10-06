# store frequency in dictionary

nums = [1, 2, 2, 3, 3, 3]

frequency = {}

# for i in nums:
#     if i not in frequency:
#         frequency[i] = 1 
#     else:
#         frequency[i] += 1 

# print(frequency)


# Using .get() method for frequency counting
for num in nums:
    frequency[num] = frequency.get(num, 0) + 1 

print(frequency)