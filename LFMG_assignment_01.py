#Q1 Fix all the syntax and logical errors in the given source code 
#add comments to explain your reasoning

# This program gets three test scores and displays their average.  It congratulates the user if the 
# average is a high score. The high score variable holds the value that is considered a high score.

HIGH_SCORE = 95
 
# Get the test scores and convert them to integers, without "int" it would be a string
test1 = int(input('Enter the score for test 1: '))
test2 = int(input('Enter the score for test 2: '))
test3 = int(input('Enter the score for test 3: ')) #adding this to get the third test score

# Calculate the average test score.
#Parentheses added to ensure addition goes before division.
average = (test1 + test2 + test3) / 3

# Print the average.
print('The average score is', average)

# If the average is a high score, congratulate the user.
# We have to keep the format of HIGH_SCORE consistent in all caps
if average >= HIGH_SCORE: 
    print('Congratulations!')
    print('That is a great average!') #moved to be inside the if block

#Q2
#The area of a rectangle is the rectangle’s length times its width. Write a 
# program that asks for the length and width of two rectangles and prints to the
# user the area of both rectangles. 

# Similar to Q1, get length and width of first rectangle and convert them to 
# numeric values. In this case we'll use floats so we can use decimals.
length1 = float(input("Enter length of rectangle 1: "))
width1 = float(input("Enter width of rectangle 1: "))

# Ask for the length and width of the second rectangle
length2 = float(input("Enter length of rectangle 2: "))
width2 = float(input("Enter width of rectangle 2: "))

# Calculate the areas
area1 = length1 * width1
area2 = length2 * width2

# Print the results
print("The area of rectangle 1 is:", area1)
print("The area of rectangle 2 is:", area2)

#Q3 
#Ask a user to enter their first name and their age and assign it to the variables name and age. 
#The variable name should be a string and the variable age should be an int.  

# Like in the previous questions, get information and convert them to 
# types of varibales requested. In this case only age needs to be converted to int.
name = input("What was your name again?: ")
age = int(input("And how old are you?: "))

#Using the variables name and age, print a message to the user stating something along the lines of:
# "Happy birthday, name!  You are age years old today!"
# Print the results
print("Hey my cousin is also called", name, ", Happy Birthday! I remember when I was", age )

