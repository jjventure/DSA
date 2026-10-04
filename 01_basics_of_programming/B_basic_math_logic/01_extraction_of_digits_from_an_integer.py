# Extract digits from an integer from right to left.

n = 5873 

while n > 0:
    last_digit = n % 10 
    print(last_digit)
    n //= 10