# Using list as a sequence 
items = [1,2,3,4,5]
for item in items:
    print(f'Round: {item}')

# Using String as a sequence 

items = 'Python'
for item in items:
    print(f'Letter: {item}')

#Using Range as a sequence

for item in range(1,10,2):
    print(f"Odd Number {item}")

# Real Use case for For Loop
# Using loop to load tables from source to target
# Data preparation using Loop - Can be iterated through columns

scores = [89,50,60,75]
total = 0
for score in scores:
    total += score
    print(f'Current Total {total}')
print(f'final total: {total}')

# Cleaning the data using for loop

files = [' report.csv ', 'DATA.csv ','final.TXT']
for file in files:
    file = file.strip().lower().replace('.txt','.csv')
    print(f'{file}')

#1 Python Challenge 
for item in range(0,11):
    print(f" 7 * {item} = {7 * item} " )

# Advance For Loops
# Break Statement - stop the loop immediately

names = ['Manish','marie','', 'Kumar']
for name in names:
    if name == '':
        print('Empty value detected')
        break
    else :
        print(f'{name}')

# Continue to skip one loop cycle without stopping the loop

names = ['Manish','marie','', 'Kumar']
for name in names:
    if name == '':
        print('Empty value detected')
        continue
    else :
        print(f'{name}')
# Pass statement - used when we want to do nothing in the loop but want to keep the loop running
names = ['Manish','marie','', 'Kumar']
for name in names:
    if name == '':
        # pass #todo: Handle empty values
        name = name.replace('','unknwon')
    print(name)
