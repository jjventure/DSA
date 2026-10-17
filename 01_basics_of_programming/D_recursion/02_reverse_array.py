'''

Suppose we have:

arr = [1, 2, 3, 4, 5]

We want:

[5, 4, 3, 2, 1]

'''

def reverse_array(arr, left, right):

    if left >= right:
        return 

    # swapping logic
    arr[left], arr[right] = arr[right], arr[left] 

    return reverse_array(arr, left + 1, right - 1)


arr = [1, 2, 3, 4, 5]

reverse_array(arr, 0, len(arr) - 1)

print(arr)


# TC --> O(n)
# SC --> O(n), the recursive call stack grows proportionally to the array's length. More precisely the max recursion depth is O(n)