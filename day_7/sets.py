# Exercises: Day 7
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercises: Level 1
# 1. Find the length of the set it_companies
length_it_companies = len(it_companies)
print("length of it companies:",length_it_companies)

# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

# 3. Insert multiple IT companies at once to the set it_companies
IT_companies = ['OpenAI','Meta','Tesla']
it_companies.update(IT_companies)
print(it_companies)

# 4. Remove one of the companies from the set it_companies
it_companies.remove('Meta')
print(it_companies)

# 5. What is the difference between remove and discard
'''
remove() raises an error (KeyError) if the item is not found in the set.
discard() does not raise an error if the item is not found — it simply does nothing.
'''

# Exercises: Level 2

# 1. Join A and B
A.union(B)
print("A and B joined:",A.union(B))

#2. Find A intersection B
A.intersection(B)
print("The intersection of A and B are:",A.intersection(B))

# 3. Is A subset of B
A.issubset(B)
print("Is A subset of B?",A.issubset(B))

# 4. Are A and B disjoint sets
A.isdisjoint(B)
print("Are A and B disjoint sets?",A.isdisjoint(B))

# 5. Join A with B and B with A
A.union(B)
print(A.union(B))
B.union(A)
print(B.union(A))

# 6. What is the symmetric difference between A and B
A.symmetric_difference(B)
print("The symmetric difference between A and B:",A.symmetric_difference(B))

# 7. Delete the sets completely
del A
del B
del it_companies

# Exercises: Level 3
#1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
len(age_set)
len(age)
print(len(age),'compared to',len(age_set)) # the length of the list is the bigger one

# 2. Explain the difference between the following data types: string, list, tuple and set
''' 
String:
A string is a sequence of characters enclosed in quotes (e.g., "Hello"). 
It is immutable (cannot be changed) and ordered.
List:
A list is an ordered, mutable collection that can contain elements of different data types 
(e.g., [1, "apple", 3.5]).
Tuple:
A tuple is similar to a list — it can hold multiple data types — but it is immutable 
(cannot be changed after creation) and ordered (e.g., (1, "banana", 4.2)).
Set:
A set is an unordered, mutable collection of unique elements (no duplicates). 
It can hold different data types, but it's not indexed (e.g., {1, 2, 3, "apple"}).
'''
# 3. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to getthe unique words.
#sentence = ['I', 'am', 'a', 'teacher', 'and', 'I', 'love', 'to', 'inspire', 'and', 'teach', 'people']
sentence = 'I am a teacher and I love to inspire and teach people'
sentence_split = sentence.split()
sentence_to_set = set(sentence_split)
print("Number of unique words:",len(sentence_to_set))
print(sentence_to_set)