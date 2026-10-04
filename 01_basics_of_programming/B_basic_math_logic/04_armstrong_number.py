# Check if a number is an Armstrong number.

def is_armstrong_number(n):
    num = n 
    number_of_digits = len(str(num))
    total = 0 

    while num > 0:
        last_digit = num % 10 
        total += (last_digit ** number_of_digits)
        num //= 10 

    return total == n 

print(is_armstrong_number(153))  # True
print(is_armstrong_number(123))  # False
print(is_armstrong_number(370))  # True
print(is_armstrong_number(9474)) # True