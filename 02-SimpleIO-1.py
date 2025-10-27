# 2. simple IO
# 
# using input and print

# if you ever wanted to ask the user to enter a value, you would use input

var = input()

# both input and print are functions
# using input will stop the program from executimg before a user enters a value and it enter
# to simplify it input takes an argument of type string
# whatever you type in that string, that text will be shown in the terminal

var = input("upisi br: ")

terminal:
upisi br: 

# now you have to enter a value and than click enter

var = input("upisi br: ")

terminal:
upisi br: 12345

# the variable var now has value of 
# var = "12345"
# now, why is it a string? you may ask
# it ia obvious that 12345 is a number, but input alway returns a string

int(input()) # will try to convert string to int.

# the program will crash if the string does not equal to a number.

# print is much simpler, it takes a value and it shows it on terminal.
# so it would work like this

print("hi")

terminal:
hi

print(123, True)

terminal
123
True
