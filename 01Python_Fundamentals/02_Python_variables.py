# What is variable 
# A variable is a container for storing data values. 
# So that we can use it later in our code.

# Example: Box filled with some data and we can use it later on
name = "Manish"

# How it is executed behind the code?
# Once print(name) executed -> Python will look for the value assigned to the variable and print it
print(name)

#Update
#Python will reassign the value to the variable name 
name = "Baraa"
print(name)

# Can also assign the value with calculation    
# Variable c will be assigned with the value of a + b in memory
a = 10
b = 20
print(a)
print(b)

#Expected Output: 30
c = a + b

print(c)

#Practice Exercise:

# Variables make updates super easy, one change updates everything

# Identifying the Static and Dynamic parts of the code

print("My name is Manish")
print("Manish love traveling and learning python")
print("Manish wants to become python expert")

# Now we have to change the name in the above statements? Tedious task!
# Use Case of variables - Easy for updating values, avoid hardcoding, make code dynamic and interactive

name = "Baraa"
language = "Python"

name = input("Enter your name: ")
language = input("enter your language: ")

# Static part can be stored in variable

print("My name is",name)
print(name,"love traveling and learning", language)
print(name,"wants to become", language, "expert")

# another way of using variable in print function
print(f"My name is {name}")
print(f"I am {name} and I love traveling and learning new languages")
print(f"{name} is curious and loves to learn new things")

#Python execute code line by line

# name = "Baraa"
print("My name is",name)
print(name,"love traveling and learning", language)
print(name,"wants to become", language, "expert")


#Python execute code line by line

# Variable makes programs dynamic
# Name to store a value
# stored in memory
# Reusable and easy to update anytime


