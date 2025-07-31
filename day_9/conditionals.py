# Exercises: Day 9
# Exercises: Level 1

# 1. 
age = int(input('Enter your age: '))
if age >= 18 :
    print("You are old enough to learn to drive.")
else:
    print(f"You need {18 - age} more years to learn to drive.")

# 2. 
my_age = 20
your_age = int(input("Enter your age: ")) 
dif = my_age - your_age 
if dif < 0 :
    print(f"You are {abs(dif)} years older than me.")
elif dif > 1 :
    print(f"I'm {abs(dif)} years older than you.")
elif dif == -1:
    print("you are a year older than me")
elif dif == 1 :
    print("I'm a year older than you")
elif dif == 0 :
    print("we are the same age")

# 3.
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))
if a > b :
    print(f"{a} is greater than {b}")
elif a < b :
    print(f"{a} is smaller than {b}")
else :
    print(f"{a} is equal to {b}")



# Exercises: Level 2
# 1. code which gives grade to students according to theirs scores:
score = int(input("Enter your score: "))
if score >= 90 and score <= 100 :
    print("grade: A")
elif score >= 70 and score <= 89 :
    print("grade: B")
elif score >= 60 and score <= 69 :
    print("grade: C")
elif score >= 50 and score <= 59 :
    print("grade: D")
elif score >= 0 and score <= 49 :
    print("grade: F")


# 2. Check if the season is Autumn, Winter, Spring or Summer.
month = input("Month: ").capitalize()
if month == 'September' or month =='October' or month == 'November' :
    print("the season is Autumn") 
elif month == 'December' or month == 'January' or month == 'February' :
    print('the season is Winter')
elif month == 'March' or month == 'April' or month == 'May' :
    print('the season is Spring')
elif month == 'June' or month == 'July' or month == 'August' :
    print('the season is Summer')

# 3. The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter the name of the fruit: ").lower()
if not fruit in fruits :
    fruits.append(fruit)
    print('The modified list :', fruits)
elif fruit in fruits :
    print('That fruit already exist in the list')

# Exercises: Level 3
# 1. Here we have a person dictionary.
person={
'first_name': 'toma',
'last_name': 'ditoma',
'age': 25,
'country': 'Togo',
'is_marred': False,
'skills': ['JavaScript', 'React', 'Node', 'MongoDB',
'Python'],
'address': {
'street': 'Space street',
'zipcode': '02210'
}
}

# * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person.keys() :
    print(f"middle skill in the skills list: '{person['skills'][2]}'")

# 
if 'skills' in person.keys() :
    if 'Python' in person['skills'] :
        print("Toma has 'Python' skill")

#
skills = set(person['skills'])

if {'React', 'Node', 'MongoDB'}.issubset(skills):
    print('He is a fullstack developer')
elif {'Node', 'Python', 'MongoDB'}.issubset(skills):
    print('He is a backend developer')
elif {'JavaScript', 'React'}.issubset(skills):
    print('He is a front end developer')
else:
    print('unknown title')


# 
if person['is_marred'] and person['country'] == 'Finland':
    print("Asabeneh Yetayeh lives in Finland. He is married.")