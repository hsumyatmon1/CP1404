numbers = []
no_of_times = 5
for i in range(no_of_times):
    number = int(input("Number: "))
    numbers.append(number)

print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[-1]))
print("The smallest number is {}".format(min(numbers)))
print("The largest number is {}".format(max(numbers)))
average = sum(numbers) / no_of_times
print("The average of the numbers is {}".format(average))


usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = str(input("Enter username: "))

if username in usernames:
    print("Access granted.")
else:
    print("Access denied.")
