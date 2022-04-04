import random


print(random.randint(5, 20))  # line 1

# The smallest number you can see on line 1 is 5.
# The largest number you can see on line 1 is 20.

print(random.randrange(3, 10, 2))  # line 2

# The smallest number you can see on line 2 is 3.
# The largest number you can see on line 2 is 9.
# Line 2 could not have produce a 4 because the sequence is 3, 5, 7, 9

print(random.uniform(2.5, 5.5))  # line 3
# The smallest number you can see on line 3 is 2.5000000000.
# The largest number you can see on line 3 is 5.500000000.

print("To produce a random number between 1 and 100 inclusive")
print(random.randint(1, 100))
