name_file = open('name.txt', 'w')
name_file.write(input("Enter your name: "))     # write
name_file.close()

name_file = open('name.txt', 'r')
print("Your name is ", name_file.read())        # read
name_file.close()

numbers_file = open('numbers.txt', 'w')
numbers_file.write("17" + "\n")
numbers_file.write("42" + "\n")
numbers_file.write("200" + "\n")
numbers_file.close()

numbers_file = open('numbers.txt', 'r')
first_number_str = numbers_file.read(2)
second_number_str = numbers_file.read(4)

first_number_int = int(first_number_str)
second_number_int = int(second_number_str)
total = first_number_int + second_number_int
print("The total of {} and {} is {}".format(first_number_int, second_number_int, total))
numbers_file.close()

numbers_file = open('numbers.txt', 'r')
print(numbers_file.read())
numbers_file.close()
