# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 16:52:39 2024

@author: lucho
"""

#Q1. What will the following code display?
#numbers = [1, 2, 3, 4, 5]
#print(numbers[1:-5])
#Can you debug and fix the output? The code should return the entire list

numbers = [1, 2, 3, 4, 5]
print(numbers[1:-5])

#This initial code will just return in an empty list []
#Why? Because Python reads it as "start at index 1 and go up to (but not include) index -5"
#Since index-5 is element 1 and, and index 1 is element 2, the list comes up 
#empty as there are no elements meeting the criteria
#To fix this we can do either:
    
print(numbers)

#Or if we want to use indices we can do 
print(numbers[0:5])

#Or if we only want to use negative indices
print(numbers[-5:])


#Q2. Design a program that asks the user to enter a store’s sales for each day of the
#week. The amounts should be stored in a list. Use a loop to calculate the total sales for
#the week and display the result.

# First we create an empty list for the total sales of the week
sales_of_week = []

# Now a list of days to ask for input, but let's do this in spanish, because we
# want someone speaking spanish using this.
days_of_week = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

# Ask the user to enter the sales amount for each day
for day in days_of_week:
    while True:
        try:
            # Ask for sales for current day (venta), and check if it's a valid number
            sales = float(input(f"Total de ventas para el dia {day}: $"))
            sales_of_week.append(sales)
            break  # in case input is not valid, exit the loop
        except ValueError:
            print("Dato no valido. Por favor use un valor numerico para el total de ventas.")

# Calculate the total sales for the week
total_sales = sum(sales_of_week)

# Display the total sales for the week
print(f"\nVenta total de la semana: ${total_sales:.2f}")


#Q3. Create a list with at least 5 places you’d like to travel to. Make sure the list isn’t in
#alphabetical order
#Print your list in its original order.
#Use the sort() function to arrange your list in order and reprint your list.
#Use the sort(reverse=True) and reprint your list.

#Let's create the list first:
wanderlist = ["Kyoto", "Munich", "Buenos Aires", "Oxford", "Amsterdam"]

# Print original list
print("Initial list:", wanderlist)

# Let's sort() the list in alphabetical order and print it
wanderlist.sort()
print("Travel list (sorted alphabetically):", wanderlist)

# Finally, let's sort(reverse=True) to arrange the list in reverse alphabetical order and print it
wanderlist.sort(reverse=True)
print("Travel list (sorted in reverse alphabetical order):", wanderlist)


#Q4. Write a program that creates a dictionary containing course numbers and the room
#numbers of the rooms where the courses meet. The program should also create a
#dictionary containing course numbers and the names of the instructors that teach each
#course. After that, the program should let the user enter a course number, then it should
#display the course’s room number, instructor, and meeting time.

# First a dictionary for each category of the information asked
course_rooms = {
    "DATA602": "Room 101",
    "DATA607": "Room 102",
    "DATA606": "Room 103",
    "PSYCH101": "Room 999",
    "PSYCH201": "Room 888"
}

course_instructors = {
    "DATA602": "Prof. Schettini",
    "DATA607": "Prof. Catlin",
    "DATA606": "Prof. Bryer, Prof. Lui, & Prof. Hagstrom",
    "PSYCH101": "Prof. Macek",
    "PSYCH201": "Prof. Brensteinner"
}

course_times = {
    "DATA602": "6:00 AM - 7:30 AM",
    "DATA607": "6:30 PM - 7:30 PM",
    "DATA606": "8:00 PM - 9:00 PM",
    "PSYCH101": "10:00 AM - 11:30 AM",
    "PSYCH201": "9:00 AM - 10:00 AM"
}

# Ask user for input, specifically the course number
course_number = input("What course do you want information on? ")

# Display the course details if the course number is valid, otherwise give feedback
if course_number in course_rooms and course_number in course_instructors and course_number in course_times:
    print(f"\nCourse Number: {course_number}")
    print(f"Room Number: {course_rooms[course_number]}")
    print(f"Instructor: {course_instructors[course_number]}")
    print(f"Meeting Time: {course_times[course_number]}")
else:
    print("Format not valid. Please check and try again, remember to use format ABC123.")


#Q5. Write a program that keeps names and email addresses in a dictionary as
#key-value pairs. The program should then demonstrate the four options:
#look up a person’s email address,
#add a new name and email address,
#change an existing email address, and 
#delete an existing name and email address.

# We start with an empty directory to store names and email addresses
email_directory = {}


# Create the menu options
def display_menu():
    print("\nMenu:")
    print("1. Look up user email")
    print("2. Add new user and email")
    print("3. Change existing user email")
    print("4. Delete existing user and email")
    print("5. End program")  #Had to add an and function or program would just keep going

# Now functions needs to be defined
# Look up an email
def look_up_email():
    name = input("Enter username: ")
    if name in email_directory:
        print(f"{name}'s email address is: {email_directory[name]}")
    else:
        print(f"Name '{name}' not found in the directory.")

# Add a new name and email address
def add_email():
    name = input("Enter username: ")
    if name in email_directory:
        print(f"{name} username already exists.")
    else:
        email = input("Enter email address: ")
        email_directory[name] = email
        print(f"New entry: {name}   email: {email}.")

# Change an existing email address
def change_email():
    name = input("Username to change email: ")
    if name in email_directory:
        email = input(" New email address: ")
        email_directory[name] = email
        print(f"Email for {name} has been updated to: {email}.")
    else:
        print(f"Username '{name}' not found.")

# Delete an existing name and email address
def delete_email():
    name = input("Username to delete: ")
    if name in email_directory:
        del email_directory[name]
        print(f"Deleted {name} from the directory.")
    else:
        print(f"Username '{name}' not found.")

# Main program loop
def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            look_up_email()
        elif choice == "2":
            add_email()
        elif choice == "3":
            change_email()
        elif choice == "4":
            delete_email()
        elif choice == "5":
            print("Exiting program")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Run the program
main()
