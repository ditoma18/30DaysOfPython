#Day-3 Operators 
# 1 Declare your age as integer variable 
age = 19

# 2. Declare your height as a float variable 
height = 175.5

# 3. Declare a variable that store a complex number 
comp_number = 3-5j

#4. Write a script that prompts the user to enter base and height of the triangle 
#and calculate an area of this triangle (area = 0.5 x b x h). 
base = float(input("Enter base: "))
height = float(input("Enter height: "))
area = 0.5 * base * height 
print("The area of the triangle is", area) 

#5. Write a script that prompts the user to enter side a, side b, and side c of the 
#triangle. Calculate the perimeter of the triangle (perimeter = a + b + c). 
a = float(input("Enter side a: ")) 
b = float(input("Enter side b: ")) 
c = float(input("Enter side c: "))
perimeter = a + b + c
print("The perimeter of the triangle is", perimeter) 

#6. Get length and width of a rectangle using prompt. Calculate its area (area = 
#length x width) and perimeter (perimeter = 2 x (length + width))
length = float(input("Length of the rectangle: ")) 
width = float(input("Width of the rectangle: "))
area = length * width 
perimeter = (2 * (length + width))
print("The perimeter of the rectangle is", perimeter, "and the area of that rectangle is", area)
 
# 7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and 
#circumference (c = 2 x pi x r) where pi = 3.14. 
pi = 3.14
r = float(input("radius of a circle: "))
area = pi * r * r
circum = 2 * pi * r
print("The area of the circle is", area ,"and its circumference is", circum)


# 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2 
slope1 = 2
x_intercept = 2/2
y_intercept = 2 * 0 - 2
print("The slope, x-intercept and y-intercept of y = 2x -2 are respectively:",slope1,"; ",x_intercept,"; ",y_intercept)

#9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10) 
m =(10-2)/(6-2)
print("slope2 = ",m)
# Euclidian distance
euc_dist = 0.5 * (6-2)**2 + (10-2)**2
print(" The Euclidean distance between point (2, 2) and point (6,10) is",euc_dist)

# 10. Compare the slopes in tasks 8 and 9. 
print("the slope are the same: ",slope1 == m) # the slope are the same

#11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and 
#figure out at what x value y is going to be 0. 
x = -3
y = x**2 + 6*x + 9
print("y = ",y)
print("y is going to be 0 at x =",x)

# 12. Find the length of 'python' and 'dragon' and make a falsy comparison statement. 
print("length of python:",len("python"))
print("length of dragon:",len("dragon"))
print("length of python is greater than length of dragon:", len("python")>len("dragon"))

# 13. Use and operator to check if 'on' is found in both 'python' and 'dragon' 
print("'on' is found in both 'python' and 'dragon' : ",'on' in 'python' and 'on' in 'dragon')

# 14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence. 
print("'jargon' is in the sentence: ",'jargon' in 'I hope this course is not full of jargon')

# 15. There is no 'on' in both dragon and python
print("There is no 'on' in both dragon and python : ", not 'on' in 'dragon' and not 'on' in 'python') 

#16. Find the length of the text python and convert the value to float and convert it to string 
len_python = len("python")
print("length of python:",len_python)
print("length of python in float:",float(len_python))
print("length of python in string:",str(float(len_python)))

# 17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python? 
number = 8
print("Even: ",number % 2 == 0) # If the output is true then the number is even

# 18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7. 
print("the floor division of 7 by 3 is equal to the int converted value of 2.7 :" ,7 // 3 == int(2.7))

# 19. Check if type of '10' is equal to type of 10
print("type of '10' is equal to type of 10 : ",type('10') == type(10))

# 20. Check if int('9.8') is equal to 10 
print("Check if int('9.8') is equal to 10 :", int(9.8) == 10 )

#21. Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person? 
hour = float(input("Enter hours: "))
rate_per_hr = float(input("Enter rate per hour: ")) 
pay = hour * rate_per_hr
print("Your weekly earning is",pay)

#22. Write a script that prompts the user to enter number of years. Calculate the 
#number of seconds a person can live. Assume a person can live hundred years 
year = float(input("Enter number of years you have lived: "))
num_sec_liv = 31536000 * year
print("You have lived for", num_sec_liv , "seconds")


# 23. Write a Python script that displays the following table 
print("1 1 1 1 1")
print("2 1 2 4 8 ")
print("3 1 3 9 27 ")
print("4 1 4 16 64")
print("5 1 5 25 125")
