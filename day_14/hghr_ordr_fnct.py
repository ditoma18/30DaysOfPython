# Exercises: Day 14 
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland'] 
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham'] 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

# Exercises: Level 1 
# 1. Explain the difference between map, filter, and reduce. 
'''
The difference between map, filter, and reduce is that map is a Higer order function with takes a funtion 
and iterable as parameters like the three order ones but return an iterable, while filter takes a function 
that returns a a boolean as result and reduice return a single value as a result
'''
# 2. Explain the difference between higher order function, closure and decorator 
'''
the difference between higher order function, closure and decorator is that 
A higher order function is a function that can take a function as parameter, return a functtion as a
result of a function or assign a function an object, while closure is the ability of a nested function
to acces the an outer function and use it , and a decorator is a disign function that can add a new functionality
to an object without modifying it strucure
'''
# 3. Define a call function before map, filter or reduce, see examples. 
# Call function before map
def sqrt_of_number(x):
    return x**0.5
# call ffunction before filter
def is_four_letter(y)
    if len(y) == 4
        print("Yes")
# call function before reduce
def sum_numbers(num)
    return sum(num)

# 4. Use for loop to print each country in the countries list. 
for c in countries:
    print (c)

# 5. Use for to print each name in the names list. 
for na in names:
    print(na)

# 6. Use for to print each number in the numbers list.
for n in numbers:
    print(n)

# Exercises: Level 2 
# 1. Use map to create a new list by changing each country to uppercase in the countries list 
def uppercasd_items(list):
    LIST = []
    for i in list:
        LIST.append(i.upper())
    return LIST
COUNTRIES  = map(uppercased_items, countries)
print("COUNTRIES = ",COUNTRIES)

# 2. Use map to create a new list by changing each number to its square in the numbers list 
def square_num(numb):
    squared_numbers = []
    for n in numb:
        squared_numbers.append(i**2)
    return squared_numbers
squared_numbers = map(square_num, numbers)
print(squared_numbers)

# 3. Use map to change each name to uppercase in the names list 
def uppercasd_items(list):
    LIST = []
    for i in list:
        LIST.append(i.upper())
    return LIST
NAMES  = map(uppercased_items, names)
print("NAMES = ",NAMES)

# 4. Use filter to filter out countries containing 'land'. 
def contain_land(list):
    for i in list:
        if "land" in i:
            return True
        else :
            return False
country_land =filter(contain_land, countries)
print("names with land :",lst(country_land))

# 5. Use filter to filter out countries having exactly six characters.
def have_six_char(list):
    for i in list:
        if len(i) == 6:
            return True
        else:
            False
fitted_country = filter(have_six_char, countries)
print("countries having exactly six characters",lst(fitted_country))

# 6. Use filter to filter out countries containing six letters and more in the country list. 
def have_six_more_char(list):
    for i in list:
        if len(i) >= 6:
            return True
        else:
            return False
fitted_country = filter(have_six_more_char, countries)
print("countries having exactly six characters",lst(fitted_country))

# 7. Use filter to filter out countries starting with an 'E' 
def start_with_E(list):
    for i in list :
        if i.startswith("E"):
            return True
        else :
            return False
fitted_country = filter(satrts_with_E, countries)
print("countries having exactly six characters",lst(fitted_country))

# 8. Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback)) 

# 9. Declare a function called get_string_lists which takes a list as a parameter 
#and then returns a list containing only string items. 
def get_string_lists(list):
    string_list =[]
    for i in list:
        string_list.append(str(i))
    return string_list

# 10. Use reduce to sum all the numbers in the numbers list.
sum_of_num = reduce(lambda numbers: sum(numbers), numbers) 
print("sum of numbers=",sum_of_num)

# 11. Use reduce to concatenate all the countries and to produce this sentence:
def concatenate(list):
    return "{}, {}, {}, {}, {}, {}, and, {} are north European countries".format(i for i in list) 

# 12. Declare a function called categorize_countries that returns a list of countries 
# with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')). 
def contain_land(list):
    for i in list:
        if "land" in i:
            return True
        else :
            return False
country_land =filter(contain_land, countries)
print("names with land :",lst(country_land))

# 13. Create a function returning a dictionary, where keys stand for starting letters 
# of countries and values are the number of country names starting with that letter.
def dict_func(list):
    dict = {}
    for i in list:
        first_l = i[0]:
        dict[first_l] = dict.get(first_l , 0) + 1
    return dict
 
# 14. Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder. 
def get_first_ten_countries(countries):
    ten_first_country = []
    for i in range(len(countries))
        if i < 11 :
            ten_first_country.append(countries[i])
    return ten_first_country

#15. Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
def get_last_ten_countries(countries)
    ten_last_country = []
    for i in range(len(countries))
        if i > len(countries)-10 :
            ten_last_country.append(countries[i])
    return ten_last_country


# 1. Use the countries_data.py (https://github.com/Asabeneh/30-Days-OfPython/blob/master/data/countries-data.py) file and follow the tasks below: 
o Sort countries by name, by capital, by population 
o Sort out the ten most spoken languages by location. 
o Sort out the ten most populated countries. 