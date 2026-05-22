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

SCORE = int(input('Enter Your Score'))
sumbmitted_project = input('submitted_project ? yes/no')

if SCORE >= 95 :
    if sumbmitted_project.lower() == 'yes':
        print('A+')
    else :
        print('A')
else:
    print('fail')
    