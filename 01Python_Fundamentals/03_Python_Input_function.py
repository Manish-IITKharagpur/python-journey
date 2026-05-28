#Introduction

# Quick Recap of print function, escape sequence, special characters, triple quotes
# Quick Recap of variables(string and Integer), assigning values, performing calculations, updating variables and dynamic code with variables


# print function to display something to users
print("Hello World")
# input function to get something from users
# Once input function executed -> Python will wait for the user to enter some value and then it will assign that value to the variable name
# text inside input function is called prompt, it will be shown to users when asking for input (Waiting)
input("Enter your name: ")

# Here input function value will be lost if not assigned to any variable, 

name = input("Enter your name: ")
# Static part
# ' , ' for adding space in between
print("Hello, ",name)

# Why we need input function?

# Problem Harcoded inside code  
country = "India" 
print("I am from", country)

# Now if I want to change the country, I have to change the code and update the value of country variable, which is not a good practice
# Use Case of input function - to make code dynamic and interactive, get values from users,

country = input("Enter your country: ")
print("I am from", country)


# Execution behind the scene of print and input function
 
name = "Manish"
print("Hello, ", name)

name = input("Enter your name: ")
print("Hello, ", name)