'''Write a function that takes a list of integers and returns a dictionary containing each number and its frequency.

For example:

nums = [4, 2, 4, 3, 2, 4, 5, 3]

Expected result:

{4: 3, 2: 2, 3: 2, 5: 1}

Requirements:

Use a dictionary.
Write a function that accepts nums and returns the frequency dictionary.
Don't use Counter().
Explain the time and auxiliary space complexity.'''

def frequency_dict(nums):

    result = {}

    for num in nums:
        if num in result:
            result[num] += 1 

        else:
            result[num] = 1 

    return result 

print(frequency_dict(nums = [4, 2, 4, 3, 2, 4, 5, 3]))


# TC --> O(n)
# SC --> O(k), where k = number of distinct elements