# Basic if-else statement
SCORE = 50 
if SCORE >= 90:
    print("Grade: A")   
else:
    print("Grade: Not A")

# if-elif-else statement

SCORE = 95
if SCORE >= 90 :
    print('Grade: A')
elif SCORE < 90 and SCORE >= 80 :
    print('Grade: B')
elif SCORE < 80 and SCORE >= 70:
    print('Grade: C')
else:
    print('Grade: F')

# Nested if Statement
# In a boolean variable using input funtion any user input will be treated as TRUE except empty string which is treated as FALSE

SCORE = int(input('Enter Your Score'))
sumbmitted_project = input('submitted_project ? yes/no')

if SCORE >= 95 :
    if sumbmitted_project.lower() == 'yes':
        print('A+')
    else :
        print('A')
else:
    print('other grade')
    

# Evaluating two contitions using logical operators'
SCORE = int(input('Enter Your Score: '))
sumbmitted_project = input('submitted_project ? yes/no: ')
if SCORE >= 95 and sumbmitted_project.lower() == 'yes' :
    print('A+')
elif SCORE >= 90:
    print('A')
elif SCORE >= 80:
    print('B')
elif SCORE >= 70:
    print('C')
elif SCORE >= 60 or sumbmitted_project.lower()=='yes':
    print('D')
else:
    print('Fail')

# Independent If-else statement

SCORE = int(input('Enter the Score: '))
submitted_project = input('submitted_project ? yes/no: ')

if SCORE >=90:
    print('Good Score')
else:
    print('Bad Score')
if submitted_project.lower() == 'yes':
    print('Submitted')
else:
    print('Not Submitted')

#Inline if statements

SCORE = 90
GRADE = "A" if SCORE>=90 else "B" if SCORE>= 80 else "other grades"
print(GRADE)

# Case - Match
# Convert the full country  name into 2 letter abbreviations

country = input('Enter your country: ') 
if country == "Unites States":
    print('US')
elif country == "India":
    print('IN')
elif country == "Germany":
    print('DE')

# else :
#     print('unknown')

match country:
    case "Unites States": 
        print('US')
    case "India" : 
        print('IN')
    case "Germany":
        print('DE')
    case _: 
        print('unbkwon Country')