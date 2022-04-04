
# Questions

# 1 When will a ValueError occur?

# A ValueError will occur when the user enter a floating point number

# When will a ZeroDivisionError occur?

# A ZeroDivisionError will occur when the user enter 0

# 3 Could you change the code to avoid the possibility of a ZerodivisionError?

# Yes

numerator = float(input("Enter the numerator: "))
denominator = float(input("Enter the denominator: "))
while denominator == 0:
    print("The denominator cannot be zero.")
    denominator = float(input("Enter the denominator: "))

fraction = numerator / denominator
print(fraction)

print("Finished.")
