#Exercises: Day 11 
# Exercises: Level 1 
# 1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def  add_two_numbers(a, b) :
    return a + b

# 2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle. 
def area_of_circle (r) :
    pi = 3.14
    area = pi * r * r
    return area

'''
 3. Write a function called add_all_nums which takes arbitrary number of 
arguments and sums all the arguments. Check if all the list items are number 
types. If not do give a reasonable feedback. 
'''
def add_all_nums(*num) :
    total = 0
    for n in num :
        if n.isnumeric() :
            total += n
        else :
            print(n,"is not a number")


# 4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. 
# Write a function which converts °C to °F, convert_celsius_to-fahrenheit. 
def convert_celsius_to_fahrenheit(c):
    F = (c * (9/5)) + 32
    return F


# 5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month) :
    if month.lower in ['december', 'january', 'february'] :
        print('Winter')
    elif month.lower in ['march', 'april', 'may'] :
            print('Spring')

    elif month.lower in ['june', 'jully', 'august'] :
            print('Summer')

    if month.lower in ['september', 'october', 'november'] :
            print('Autumn')


# 6. Write a function called calculate_slope which return the slope of a linear equation 
def calculate_slope(x1, y1, x2, y2):
    if x2 == x1:
        raise ValueError("Slope is undefined for a vertical line (x2 - x1 = 0)")
    slope = (y2 - y1) / (x2 - x1)
    return slope

# 7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function 
# which calculates solution set of a quadratic equation, solve_quadratic_eqn. 
def solve_quadratic_eqn(a, b, c) :
     x1 = (-b - ((b**2 - 4*a * c)**0.5))/(2*a)
     x2 = (-b + ((b**2 - 4*a * c)**0.5))/(2*a)
     print(f"solutions of the equation are {x1} and {x2}")


# 8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(list) :
     for l in list :
          print(l)

# 9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops). 
def reverse_list(LIST):
     TSIL = []
     for i in range(len(LIST)-1, -1, -1):
          TSIL.append(LIST[i])
     print("reversed list:",TSIL)


# 10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items 
def capitalize_list_items(lisstt):
     cap_list = []
     for s in lisstt:
          cap_list.append(s.capitalize())
     return cap_list
          
# 11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end. 
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'] 
def add_item(Liste, item):
     return Liste.append(item)
     
# 12. Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(liste, item) :
     return liste.remove(item)

# 13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range. 
def sum_of_numbers(n) :
     total = 0
     for i in range(n+1) :
          total += i
     return total
     
# 14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range. 
def sum_of_odds(n):
    total = 0
    for i in range(n+1) :
         if i%2 != 0 :
              total += i
    return total
         
#15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range. 
def sum_of_odds(n):
    total = 0
    for i in range(n+1) :
         if i%2 == 0 :
              total += i
    return total

# Exercises: Level 2 
# 1. Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number. 
def sum_of_odds(n):
    total = 0
    for i in range(n+1) :
         if i%2 == 0 :
              total += i
    return total


# 1. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(n):
    fact = 1
    for i in range(n) :
        fact *= i    
    return fact
 
# 2. Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(p):
     if p.is_empty :
          print("empty")
     else :
          print("is not empty")

# 3. Write different functions which take lists. They should calculate_mean, 
# calculate_median, calculate_mode, calculate_range, calculate_variance, 
# calculate_std (standard deviation). 
from collections import Counter
import math

def calculate_mean(lst):
    return sum(lst) / len(lst)

def calculate_median(lst):
    lst_sorted = sorted(lst)
    n = len(lst)
    mid = n // 2
    if n % 2 == 0:
        return (lst_sorted[mid - 1] + lst_sorted[mid]) / 2
    else:
        return lst_sorted[mid]

def calculate_mode(lst):
    counter = Counter(lst)
    most_common = counter.most_common()
    max_count = most_common[0][1]
    modes = [val for val, count in most_common if count == max_count]
    return modes if len(modes) > 1 else modes[0]

def calculate_range(lst):
    return max(lst) - min(lst)

def calculate_variance(lst):
    mean = calculate_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)

def calculate_std(lst):
    return math.sqrt(calculate_variance(lst))


# Exercises: Level 3 

# 1. Write a function called is_prime, which checks if a number is prime. 
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 2. Write a functions which checks if all items are unique in the list. 
def are_items_unique(lst):
    return len(lst) == len(set(lst))

# 3. Write a function which checks if all the items of the list are of the same data type. 
def are_same_type(lst):
    return all(type(item) == type(lst[0]) for item in lst)

# 4. Write a function which check if provided variable is a valid python variable 
def is_valid_variable(var):
    import keyword
    return var.isidentifier() and not keyword.iskeyword(var)

# 5. Go to the data folder and access the countries-data.py file. 
#Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order 
def most_spoken_languages(data, top_n=10):
    lang_counter = Counter()
    for country in data:
        for lang in country['languages']:
            lang_counter[lang] += 1
    return lang_counter.most_common(top_n)

#Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order. 
def most_populated_countries(data, top_n=10):
    sorted_by_pop = sorted(data, key=lambda x: x['population'], reverse=True)
    return [{"country": c["name"], "population": c["population"]} for c in sorted_by_pop[:top_n]]