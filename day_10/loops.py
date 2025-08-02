# Exercises: Day 10
# Exercises: Level 1

# 1. Iterate 0 to 10 using for loop, do the same using while loop.
for i in range(11):
    print(i)

v = 0
while v < 11 :
    print(v)
    v = v+1

# 2. Iterate 10 to 0 using for loop, do the same using while loop.
for i in range(-10, 1):
    print(abs(i))

v = -10
while v < 1 :
    print(abs(v))
    v = v+1

# 3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
v = 1
while v < 8 :
    print("#"*v)
    v = v+1

# 4. Use nested loops to create the following:
for i in range(8) :
    for k in range(7) :
        print('#', end='')
    print("#")


# 5. Print the following pattern:
for i in range(11) :
    print(f"{i} x {i} = {i * i}")


# 6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
skills = ['Python', 'Numpy','Pandas','Django', 'Flask']
for skill in skills :
    print(skill)

#7. Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(101) :
    if i % 2 == 0 :
        print(i)

#8. Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(101) :
    if i % 2 != 0 :
        print(i)


# Exercises: Level 2

# 1.Use for loop to iterate from 0 to 100 and print the sum of all numbers. The sum of all numbers is 5050.
s = 0
for i in range(101) :
    s += i 
print(f'The sum of all numbers is {s}.')

# 1. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
x = 0
y = 0
for i in  range(101) :
    if i % 2 == 0 :
        x += i

    elif i % 2 != 0 :
        y += i
print(f'The sum of all evens is {x}. And the sum of all odds is {y}.')

# Exercises: Level 3

# 1. Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
# 
land_countries = [country for country in countries if 'land' in country.lower()]
print("Countries containing 'land':", land_countries)


# 2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []

for i in range(len(fruits) - 1, -1, -1):
    reversed_fruits.append(fruits[i])

print("Reversed fruits:", reversed_fruits)


#3. Go to the data folder and use the countries_data.py file.
#i. What are the total number of languages in the data
# 
languages = []
for country in countries_data:
    languages.extend(country['languages'])

unique_languages = set(languages)
print("Total number of unique languages:", len(unique_languages))


#ii. Find the ten most spoken languages from the data
from collections import Counter

lang_counter = Counter()

for country in countries_data:
    for lang in country['languages']:
        lang_counter[lang] += 1

most_common_langs = lang_counter.most_common(10)
print("Top 10 most spoken languages (by number of countries):")
for lang, count in most_common_langs:
    print(f"{lang}: {count} countries")


#iii. Find the 10 most populated countries in the world
sorted_by_population = sorted(countries_data, key=lambda x: x['population'], reverse=True)

top10_populated = sorted_by_population[:10]
print("Top 10 most populated countries:")
for country in top10_populated:
    print(f"{country['name']}: {country['population']} people")

