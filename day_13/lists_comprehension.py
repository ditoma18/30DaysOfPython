# ===============================
# EXERCICES - DAY 13
# ===============================

# 1. Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_numbers = [num for num in numbers if num <= 0]
print("1. Nombres négatifs ou zéro :", negative_numbers)

# 2. Flatten a list of lists of lists to a one-dimensional list
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flatten_list = [num for sublist1 in list_of_lists for sublist2 in sublist1 for num in sublist2]
print("2. Liste aplatie :", flatten_list)

# 3. Using list comprehension create the following list of tuples
result = [(i, 1, i**1, i**2, i**3, i**4, i**5) for i in range(11)]
print("3. Liste de tuples (puissances) :")
for row in result:
    print(row)

# 4. Flatten the list of countries into uppercase with ISO code
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output4 = [[country.upper(), country[:3].upper(), city.upper()] for pair in countries for (country, city) in pair]
print("4. Liste pays/ville avec codes ISO :")
print(output4)

# 5. Change the list to list of dictionaries
output5 = [{'country': country.upper(), 'city': city.upper()} for pair in countries for (country, city) in pair]
print("5. Liste de dictionnaires :")
print(output5)

# 6. List of full names concatenated as strings
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
output6 = [f"{prenom} {nom}" for pair in names for (prenom, nom) in pair]
print("6. Liste de noms complets :")
print(output6)

# 7. Lambda function for slope and y-intercept
# Equation linéaire : y = mx + b
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
intercept = lambda x1, y1, x2, y2: y1 - slope(x1, y1, x2, y2) * x1

# Exemple d'utilisation
x1, y1 = 2, 3
x2, y2 = 5, 11
m = slope(x1, y1, x2, y2)
b = intercept(x1, y1, x2, y2)
print("7. Pente (slope) :", m)
print("   Ordonnée à l'origine (intercept) :", b)
