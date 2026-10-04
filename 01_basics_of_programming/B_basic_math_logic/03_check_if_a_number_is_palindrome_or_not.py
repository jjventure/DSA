# check if a number is palindrome or not. 

def num_is_palindrome(n):
    num = n 
    result = 0 

    while num > 0:
        last_digit = num % 10 
        result = (result * 10) + last_digit 
        num //= 10

    return result == n 

print(num_is_palindrome(121))