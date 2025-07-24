# Exercice1
# 'Day 2: 30 Days of python programming'
# Variables in Python
first_name = 'Parfait'
print(first_name)
last_name = 'Akounda'
print(last_name)
full_name = 'Parfait Akounda'
print(full_name)
country = 'Togo'
print(country)
city = 'Kara'
print(city)
age = 185
print(age)
year = 2025
print(year)
is_married = False
print(is_married)
is_true = True
print(is_true)
is_light_on = True
print(is_light_on)

# Declaration of multiple variables on one line
first_name, last_name, full_name, country, city, age, year, is_married, is_true, is_light_on = 'Parfait','Akounda','Parfait Akounda','Togo', 'Kara', 185, 2025, False, True, True

# Exercice2

# 1 data type of our variable listed above
print(type(first_name)) 
print(type(last_name)) 
print(type(full_name)) 
print(type(country)) 
print(type(city)) 
print(type(age)) 
print(type(year)) 
print(type(is_married)) 
print(type(is_true))
print(type(is_light_on)) 

#2 length of my first name
print("The length of the first name is : ",len(first_name))

#3 Comparison of the length of my first name and my last name
print("The length of the first name is : ",len(first_name))
print("The length of the last name is : ",len(last_name))
# comparison : The length of my last name is equal to the length of my first name
print("The length of my last name is equal to the length of my first name")
#4 Declaration
num_one = 5
print("num one is",num_one)
num_two = 4
print("num two is",num_two)

#5 addition
total = num_one + num_two
print("total = ",total)

# 6 subtraction
diff = num_one - num_two
print("diff = ",diff)

#7 multiplication
product = num_two * num_one
print("product = ",product)

#8 Division
division = num_one/num_two
print("division = ",division)

#9 remainder
remainder = num_two / num_one
print("remainder= ", remainder)

# 10 exponential
exp = num_one ** num_two
print("exp = ", exp)

#11 floor division
floor_division = num_one / num_two
print("floor_division = ", floor_division)

# 12 The radius of a circle is 30 meters.
radius = 30
# area of the circle
area_of_circle = 3.14 * (radius ** 2)
print("The area of the circle is,",area_of_circle)
# circumfernecce of the circle
circum_of_circle =2 * 3.14 * radius
print("The circumfernecce of the circle is,", circum_of_circle)
# Let's take radius as user input and calculate the area.
radius = int(input("Give the radius of the circle: "))
area_of_circle = 3.14 * (radius ** 2)
print("The area of the circle is,",area_of_circle)

# 13 Let's use the built-in input function 
first_name = input('Give your first name : ')
last_name = input('Give your last name : ')
country = input('Give the name of your country : ')
age = input('How old are you? : ')

# 14 Python reserved words or keywords
help('keywords')










