# String Datatypes

# printing datatype of string variable
# name = "Manish"
# print(type(name))
# print("your name is",name)

# # Integer
# age = 24
# print(type(age))
# print("your age is", age)

# Using str() Function to convert integer to string
# Use Case: building a message that mixes text and numbers
# age = 24

# # print("your age is "+ age)
# print("your age is " + str(age))
# print(type(age))
# age += 5
# print("your age after 5 years will be " + str(age))

# Now changing the datatype of age variable to string
# age = str(age)
# print(type(age))
# age += 5

# Expected TypeError: can only concatenate str (not "int")
# print(age)

# Here Concatenation will not give error
# print(age + " years old")


# String Function Math - len() and count()

# password = "manish123"
# password must be 8 characters long
# password_length = (len(password))

# # print(varibal_name) , len(password)
# # str.upper(), str.lower()

# if password_length < 8:
#     print("Password must be at least 8 characters long")
# else:
#     print("password length", password_length)
#     print("Password is valid")

# Counting Frequency: How many times string appears in text
# Use Case : can be checked for special characters  (quality of password)

# text = """ Python is easy to learn.
# Python is a high level programming language.
# Python is used for web development, data science, machine learning, artificial intelligence and many more.
# """
# case Sensitive
# print(text.count("Python"))

# Transformation of String: reshaping the string value

# Date Format: 2026/05/10 -> 2026-05-10
# date = "2026/05/10"
# print(date.replace("/", "-"))

# transformation
# price = "1234,56"
# print(price.replace(",", "."))

# Replacing with no values
# phone = "123-456-789"
# print(phone.replace("-", ""))

# price  = "$1,234.56"
# print(price.replace("$", "").replace(",", ""))

# String concatenation: Joining two or more strings together
# first_name = "Manish"
# last_name = "Raj"
# full_name = first_name + " " + last_name
# print(full_name)

# # Common Use case
# folder = "C:/Users/Baraa"
# file_name = "document.txt"
# file_path = folder + "/" + file_name
# print(file_path)

# F-string : Lets you easily put variables and expressions directly inside string value
# Use Case: generating a user profile summary or order confirmation message
# name = "sam"
# age = 34
# is_student = False

# print("My name is " + name + ". I am " + str(age) + " years old and student status is " + str(is_student) + "." )

# Using F-string : Short readable cleaner, easier to read, If multiple value is present

# print(f"My name is {name}. I am {age} years old and student status is {is_student}.")/

# Not only value also expressions

# print(f"2+3 = {2+3}")


# If you want curly bracket in the output

# print(f"{{This is my curly bracket}}")

# split() : breaks a string into a list by a separator
# Use Case: parsing a CSV row or extracting parts from a formatted string

# Expected Output list of strings ['a','b','c']
# class of methods <class str > methods split
# code = "Manish-25-USA"
# print(code.split("-"))

# stamp ="2026-05-29"
# print(stamp.split("-"))

# csv_file = "1234,Max,USA,1970-10-05, M"
# print(csv_file.split(","))

# Transformations 'string' * number : repeats the string multiple times
# Use case: while writing code we do separations

# print("=" * 30)

# How to extract specific part of strings
#       012345678
# code = "Manish-25"
#       987654321

# Error: string index out of range
# print(code[-10])
# print(code[-9])
# print(code[-8])
# print(code[-7])
# print("="*10)
# print(code[0])
# print(code[1])
# print(code[2])
# print(code[3])

# Now want to extract parts of string
# print(code [start:end])
# print("="*30)
# if you want to print full string

# print(code[-10:])
# print(code)

# Most complicated string[start:end:skip_position]

# print(code[0:9:2])

# Index and Slicing

# date = "2026-05-29"

# Here we can only specify the end
# Extract year
# print(date[0:4])

# Extract month

# print(date[5:7])

# Extract Day use -ve index
# closer to the -ve index
# print(date[-2:])


# Cleaning white space the string values
# Removing spaces from the string __Manish__
# User enters by giving space
# name = input("Enter your Name: ")
# print(name)
# print(name.rstrip())
# print(name.lstrip())
# print(name.strip())

# using to detect white space in the string
# name = input("Enter your Name: ")
# len_whitespace = len(name)
# len_NoSpace =len(name.strip())
# space_count=len_whitespace - len_NoSpace
# if space_count > 0:
#     print(f"You have {space_count} spaces")
# else :
#     print("string with no white space")

# Using special characters using strip
# name = "$Manish$"
# print(name.strip("$"))

# Upper and lower case method for class of str

# Use case while searching case doesn't matter

# search = "email ".lower().strip()
# data  = "Email".lower().strip()
# print(search == data)


# Searching for string with year 2026
# "2026-May-29"

# Attribute Error : list object has no attribute startswith
# date =["2026-May-29","2021","2024"]
# print(date.startswith("2026"))

# endswith() and startswith() are attribute of str object

# phone ="+48-176-12345"
# print(phone.startswith("+49"))
# date = "manish@123gmail.com"
# print(phone.endswith("@gmail.com"))

# file = "data_backup.csv"
# print(file.endswith("csv"))


# use case : valid email
# email = "manish@1234.com"
# print(email.find("@"))
# print("@" in email)

# Use case : checking for API call
# url = "https://api.company.com/v1/data"
# print("/api" in url)

# find() : always combined with other task to add dynamics

# Search for country code and we know that code is before first "-"
# phone1 = "+48-176-12345"
# phone2 = "48-654-16548"
# phone3 = "0048-123-453"
# print(phone1[phone1.find("-")+1:])

# validation

# country = "USA"
# print(country.isalpha())

# Use Case: Check we have clean phone number
# phone = "+123456789"
# print(phone.isnumeric())


# join() : opposite of split() - joins a list of strings into one string
# parts = ["2026", "05", "29"]
# print("-".join(parts))

# Use Case: building a file path from parts
# folders = ["C:", "Users", "Manish", "Documents"]
# print("\\".join(folders))

# Use Case: turning a list of words into a sentence
# words = ["Python", "is", "awesome"]
# print(" ".join(words))


# 'in' keyword : check if a substring exists inside a string (returns True/False)
# email = "manish@gmail.com"
# print("@" in email)
# print("yahoo" in email)

# Use Case: checking for API endpoint
# url = "https://api.company.com/v1/data"
# print("/api" in url)

# Use Case: spam filter
# message = "Click here to claim your free prize!"
# print("free" in message.lower())


# format() : older way to embed values in strings (before f-strings)
# name = "Manish"
# age = 24
# print("My name is {}. I am {} years old.".format(name, age))

# Named placeholders
# print("My name is {name}. I am {age} years old.".format(name="Manish", age=24))

# Use Case: reusing a template
# template = "Hello {name}, your order {order_id} is confirmed."
# print(template.format(name="Manish", order_id="ORD-001"))
# print(template.format(name="Sam", order_id="ORD-002"))


# zfill() : pads a number string with leading zeros to reach a given width
# Use Case: consistent ID or code formatting
# order_id = "42"
# print(order_id.zfill(5))

# Use Case: formatting month and day with leading zero
# month = "5"
# day = "9"
# print(month.zfill(2) + "-" + day.zfill(2))

# Use Case: employee ID system
# emp_number = "7"
# emp_id = "EMP-" + emp_number.zfill(4)
# print(emp_id)
