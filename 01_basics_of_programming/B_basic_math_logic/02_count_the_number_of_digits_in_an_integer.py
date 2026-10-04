# Count the number of digits in an integer.

n = 5438 

num = n 
count = 0 

while num > 0:
    count += 1 
    num //= 10 

print(count)