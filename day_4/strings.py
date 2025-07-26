# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
print("concatenation: ",'Thirty ' + 'Days '+ 'Of ' + 'Python') 

# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
print("concatenation: "+'Coding '+ 'For ' + 'All')

# 3. Declare a variable named company and assign it to an initial value "Coding
company = "Coding For All"

# 4. Print the variable company using print().
print(company)

# 5. Print the length of the company string using len() method and print().
print("Length of the company string: ",len(company))

# 6. Change all the characters to uppercase letters using upper() method.
print("company in upper case: ", company.upper())

# 7. Change all the characters to lowercase letters using lower() method.
print("company in lower case : ",company.lower() )

# 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print("string 'Coding For All' capitalized: ", "Coding For All".capitalize())
print("string 'Coding For All' titled: ", "Coding For All".title())
print("string 'Coding For All' swapcased: ", "Coding For All".swapcase())

# 9. Cut(slice) out the first word of Coding For All string.
print("first word of 'Coding For All string': ","Coding For All string"[0])

# 10. Check if Coding For All string contains a word Coding using the method index,find or other methods.
print("Checking if 'Coding For All' string contains a word 'Coding': ","Coding For All".find("Coding") )

# 11. Replace the word coding in the string 'Coding For All' to Python.
print("Replacing the word 'coding' in the string 'Coding For All' to 'Python': ","Coding For All".replace("Coding","Python") )

# 12. Change Python for Everyone to Python for All using the replace method or other methods.
print("Changing 'Python for Everyone' to 'Python for All': ","Python for Everyone".replace("Everyone","All"))

# 13.Split the string 'Coding For All' using space as the separator (split()) .
print("'Coding For All' being split: ","Coding For All".split(" "))

#14."Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"+" being split at the comma","Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(', '))

# 15.What is the character at index 0 in the string Coding For All.
print("The character at index 0 in the string 'Coding For All' is: ","Coding For All"[0])

# 16.What is the last index of the string Coding For All.
print("The last index of the string 'Coding For All' is: ","Coding For All"[-1])

# 17.What character is at index 10 in "Coding For All" string.
print("The character at index 10 in 'Coding For All is': ","Coding For All"[10])

# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
print("Acronym or an abbreviation for the name 'Python For Everyone': ",'Python For Everyone'.strip("yone"))

# 19. Create an acronym or an abbreviation for the name 'Coding For All'.
print("Acronym or an abbreviation for the name 'Coding For All': ","Coding For All".strip("oil"))
    
#20. Use index to determine the position of the first occurrence of C in Coding For All.
print("The first occurrence of 'C' in ''Coding For All: ","Coding For All".index("C"))

# 21. Use index to determine the position of the first occurrence of F in Coding For All.
print("The first occurrence of 'F' in 'Coding For All': ","Coding For All".index("F"))

# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
print("The position of the last occurrence of 'l' in 'Coding For All People': ","Coding For All People".rfind("l"))

#23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print("the position of the first occurrence of the word 'because' in the sentence: ",'You cannot end a sentence with because because because is a conjunction'.find('because'))

#24. Use rindex to find the position of the last occurrence of the word because in
print("the position of the last occurrence of the word 'because' in the sentence: ",'You cannot end a sentence with because because because is a conjunction'.rfind('because'))


#25.Slice out the phrase 'because because because' in the following sentence:'You cannot end a sentence with because because because is a conjunction'
print("Slicing out the phrase 'because because because': ",'You cannot end a sentence with because because because is a conjunction'[31:54])


#26.Find the position of the first occurrence of the word 'because' in the followin sentence: 'You cannot end a sentence with because because because is aconjunction'
print("the position of the first occurrence of the word 'because' in the sentence: ",'You cannot end a sentence with because because because is a conjunction'.find('because'))

#27.Slice out the phrase 'because because because' in the following sentence:'You cannot end a sentence with because because because is a conjunction'
print("Slicing out the phrase 'because because because': ",'You cannot end a sentence with because because because is a conjunction'[31:54])


# 28. Does ''Coding For All' start with a substring Coding?
print("'Coding For All' starts with substring 'coding': ",'Coding For All'.startswith("Coding"))


#29. Does 'Coding For All' end with a substring coding?
print("'Coding For All'ends with substring 'coding': ",'Coding For All'.endswith("Coding"))

#30. ' Coding For All ' , remove the left and right trailing spaces in the givenstring.
print("removing trailing space in ' Coding For All ':",' Coding For All '.strip())

# 31.Which one of the following variables return True when we use the method isidentifier():
print("30DaysOfPython: ",'30DaysOfPython'.isidentifier())
print("thirty_days_of_python: ", "thirty_days_of_python".isidentifier())


# 32.The following list contains the names of some of python libraries: ['Django','Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
Lis = ['Django','Flask', 'Bottle', 'Pyramid', 'Falcon']
print("List joined: ", '# '.join(Lis))


#33. Use the new line escape sequence to separate the following sentences.
print("I am enjoying this challenge \n" +"I just wonder what is next")


# 34. Use a tab escape sequence to write the following lines.
print('Name\t Age\tCountry  City')
print('Asabeneh 250\tFinland\t Helsinki')

# 35. Use the string formatting method to display the following
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area) # 2 digits after decimal
print(formated_string)

# 36. Make the following using string formatting
print('{} + {} = {}'.format(8,6,14))
