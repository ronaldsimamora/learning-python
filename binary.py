n = 39
remainders = []
while n > 0:
    remainder = n % 2 # reminder of division by 2
    remainders.append(remainder) # we keep track of reminders
    n //= 2 # we devide n by 2

# reassign the list to its reversed copy and print it
remainders = remainders[::-1]
print(remainders)
