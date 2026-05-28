# What is Datatypes? : Empty box with a label, which can store any type of data in it.

# But the assigned value will define the datatype of the variable.

# Example: Empty box (container) with a label (variable name) and we can put any type of data in it, but once we put the value in it, it will define the datatype of that variable.

# Integer
a = 10
# String
b = "Manish" 
b = 'Manish'
# Float
c = 3.14
# Boolean
# Boolean is Case Sensitive, it should be capital T and F
# Use Case: To check some condition and return True or False
d = True
e = False

# NoneType:  We don't have any value assigned
h = None

i ="" # Empty String

# Now updating it with different datatype value
a = "Manish"

a = "Baraa"
# Python will automatically detect and change the datatype (DYNAMIC)

# So python stores variables in different size and different types

# Using built-in function upper() to explain why datatypes are important

print("manish".upper())

# If we try to use upper() function on integer variable, it will give us an error because upper() function is only for string datatype
number = 10
# print( number.upper() )

# AttributeError: 'int' object has no attribute 'upper'
# So here variable is object and upper() is the attribute of string object
# Does upper() belong to integer variable? No

# Empty data is also a datatype in python, it is called NoneType 
# empty_data = None

# Primitive DataTypes / Single Value  DataTypes: Integer, String, Float, Boolean, NoneType

# Multi Value DataTypes: List, Tuple, Set, Dictionary (Will be covered in later videos)

# Functions + DataTypes
# Specific Functions for specific datatypes
# Standalone functions : print(), input(), len(), type() etc , Built in modules, classes <str> and their methods(upper(),replace())
# Methods of class: upper(), lower() for class string
# Comparison Operators: >, <, ==, != etc are like shortcut for functions
# Types based on Sources  : Standard Libraty, Third party libraries, User defined functions

#  Variables and Values are OBJECT  -->  Object are linked to a specific classes(datatypes) --> classes have specifc methods  --> another datatype can't use method of other class

# So FUNCTIONS AND METHODS ARE SAME?

# Syntax of function: function_name(parameters)
print("Hello World") 

# Syntax Method: object_name.method_name(parameters)
print("Hello World".upper())
print("Hello World".lower())

a = "Manish"
b =  90

# Standalone Functions
print(a)
print(b)

print(type(a))
print(type(b))  

print(len(a))
# TypeError: object of type 'int' has no len()

# print(b.upper())

# AttributeError: 'int' object has no attribute 'upper'

print(a.upper())

print(b.bit_length()) 


