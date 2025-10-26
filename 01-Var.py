# 1. Declaring variables
#
# Variables are "storages" for data
# You can request the data by saying the storage's name
#
# Variable name can include any letter, numbers and underscore
# You can give it a value by doing it like this:

variableName = "Value"  # This variable has type of string
example2 = 3.14         # And this one has type of float
example2_45 = 54        # But this one is int
thirdExample = False    # And this one has type of bool -> can be either True or False

# Invalid variable names:
# 2example = 5   # Cant start with a number
# my-var = 10    # Cant use a -
# print = "Hi"   # Dont overwrite built-in names

# variable can store any type of data, from simple bool to class instances
#
#
# Lets see how to call a variable:

variableName

# Easy, right?
# Just type out the name of the variable
# Your turn!

# [REPLACE THIS LINE WITH YOUR CODE]

# There is one more thing
# You can make placeholders for variables
# What I like to do is this

varName = None
anotherPlaceholder = None

# I typically use None; since we can override its value later on
#
# In one line, you can declare multiple variables

a, b = 1, 2

# That is the same as if we done this

a = 1
b = 2

# So a has the value of 1
# And b has the value of 2
#
# we can use that feature to switch data from one to another variable
# instead of doing this:

a = 1
b = 2
c = a

a = b
b = c

# That can be messy; + we have to make a new temporary variable
# we can do this

a = 1
b = 2

a, b = b, a
