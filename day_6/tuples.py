# Exercises: Level 1
# 1. Create an empty tuple
empty_tuple = ()
print("empty tuple:",empty_tuple)

# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ("Luc", "Jean", "Mathieu", "Andre", "Marc")
print("brothers tuple:",brothers)
sisters = ("Ama", "Ane", "Afi", "Rose")
print("Sisters tuple:",sisters)

# 3. Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print("siblings:",siblings)

# 4. How many siblings do you have?
num_of_siblings = len(siblings)
print(f"I have {num_of_siblings} siblings")

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
# Since the tuple is imuable let's create a new tuple called parents and add it to the siblings tuple to have the family
parents = ("Romeo", "Juliete")
family_members = siblings + parents
print("Family members:",family_members)

# Exercises: Level 2

#1. Unpack siblings and parents from family_members
siblings, parents = family_members[0:9], family_members[-2:]
print("Unpacked siblings:",siblings)
print("Unpacked parents:",parents)

# 2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("mango", "orange", "banana", "lemon")
vegetable = ('tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
animals = ("chiken", "duck", "goat")
food_stuff_tp = fruits + vegetable + animals
print("Food stuff tuple:",food_stuff_tp)

# 3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print("Food stuff list:",food_stuff_lt)

# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_items = food_stuff_lt[5:7]
print("Middle food stuff:",middle_items)

# 5. Slice out the first three items and the last three items from food_staff_lt list
first_three_item = food_stuff_lt[0:3]
last_three_item = food_stuff_lt[-3:]
print("first three items of the list:",first_three_item)
print("last three items of the list:",last_three_item)

#6. Delete the food_staff_tp tuple completely
del food_stuff_tp

# 7. Check if an item exists in tuple
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
# Check if 'Estonia' is a nordic country
print('Estonia' in nordic_countries)
# Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries)