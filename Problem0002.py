#!/usr/bin/env python3

import sys

# function to calculate fibonacci sequence numbers
def fib(n):
    """Return the fibonacci sequence number"""
    if n <= 1: 
        return n
    else:
        return fib(n-1) + fib(n-2)

# get user input for upper limit
print("Enter an upper limit for fibanocci sequence number:")
fib_num_limit = int(input())

# variable to hold sum of even fibonacci numbers
sum_total = 0

# counter for fibonacci sequence iterations
iterator = 0

# loop until we hit the user entered limit
while fib(iterator) <= fib_num_limit:
    n = fib(iterator)
    
    # use the modulus operator to check for a remainder.. no remainder, even number
    if(n % 2 == 0):
        print(str(n))
        sum_total += n
    
    iterator += 1

print("the sum of all even number fibonnaci numbers up to %d is %d" %  (fib_num_limit,sum_total))

