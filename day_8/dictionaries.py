# Exercises: Day 8

# 1. Create an empty dictionary called dog
dog = {}

# 2. Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'max'
dog['color'] = "black"
dog['breed'] = 5
dog['legs'] = 'whith'
dog['age'] = 3

print('dog:',dog)

# 3. Create a student dictionary
student = {
    'first_name':'toma',
    'last_name': 'ditoma',
    'gender' : 'male',
    'age' : 25,
    'marital status':'single',
    'skills': ['Python','Matlab','R'],
    'country': 'Togo',
    'city' : 'Kara',
    'address' : 'Lama_kara'
}
print('student:',student)

# 4. Get the length of the student dictionary
len(student)
print("length of student",len(student))

# 5. Get the value of skills and check the data type, it should be a list
value_of_skills = student.get('skills')
print(value_of_skills)
print(type(value_of_skills))

# 6. Modify the skills values by adding one or two skills
student['skills'].append('QGIS')
print(student)

# 7. Get the dictionary keys as a list
student.keys
print(student.keys())

# 8. Get the dictionary values as a list
student.values()
print(student.values())

# 9. Change the dictionary to a list of tuples using items() method
student.items()
print(student.items())

# 10. Delete one of the items in the dictionary
del student['city']
print(student)

# 11. Delete one of the dictionaries
del student