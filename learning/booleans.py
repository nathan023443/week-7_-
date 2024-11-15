
############################################################################
# Boolean expressions are statements that can be either True or False. In Python, the boolean data type is represented by the built-in data type bool.

# Boolean expressions are commonly used for decision-making in programming.

# Here's a breakdown with examples:

# 1. Comparison Operators:
# These operators are used to compare two values:

# == (Equal to): Checks if the two values are equal.

# python
# # Copy code
# print(5 == 5)  # True
# print(5 == 6)  # False
# # != (Not equal to): Checks if two values are not equal.

# # python
# # Copy code
# print(5 != 5)  # False
# print(5 != 6)  # True
# # < (Less than): Checks if the left value is less than the right value.

# # python
# # Copy code
# print(5 < 6)  # True
# print(6 < 5)  # False
# # > (Greater than): Checks if the left value is greater than the right value.

# # python
# # Copy code
# print(5 > 6)  # False
# print(6 > 5)  # True
# # <= (Less than or equal to): Checks if the left value is less than or equal to the right value.

# python
# Copy code
# print(5 <= 6)  # True
# print(6 <= 6)  # True
# >= (Greater than or equal to): Checks if the left value is greater than or equal to the right value.

# python
# Copy code
# print(5 >= 6)  # False
# print(6 >= 6)  # True
# 2. Logical Operators:
# These operators are used to combine conditional statements:

# and: Returns True if both statements are true.

# python
# Copy code
# x = 5
# print(x > 3 and x < 10)  # True
# or: Returns True if at least one of the statements is true.

# python
# Copy code
# x = 5
# print(x > 3 or x > 10)  # True
# not: Reverse the result, returns False if the result is true.

# python
# Copy code
# x = 5
# print(not(x > 3 and x < 10))  # False
# 3. Membership Operators:
# in: Returns True if a sequence with the specified value is present in the object.

# python
# Copy code
# x = [1, 2, 3, 4, 5]
# print(3 in x)
# print(8 in x)  # True
# not in: Returns True if a sequence with the specified value is not present in the object.

# python
# Copy code
# x = [1, 2, 3, 4, 5]
# print(6 not in x)  # True
# 4. Identity Operators:
# is: Returns True if both variables are the same object.

# python
# Copy code
# x = [1, 2, 3]
# y = [1, 2, 3]
# z = x
# print(x is z)  # True, because z is the same object as x
# print(x is y)  # False, because x and y are not the same objects
# is not: Returns True if both variables are not the same object.

# python
# Copy code
# x = [1, 2, 3]
# y = [1, 2, 3]
# print(x is not y)  # True
# Remember, every boolean expression will evaluate to either True or False, and understanding this concept is fundamental for decision-making in programming.


#######################boolean expressions challenges#####################
# 20 points each challenge...
# problem 1: Check if a number is both even and divisible by 5.
# The program prompts the user for a number, checks whether it meets both conditions 
# (even and divisible by 5), and then outputs the result to the console.

# Prompt the user for a number
# num = int(input('enter in a number: '))
# Even_list= [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70,72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
# # Check if the number is even and divisible by 5
# print(num in Even_list and(num% 5==0))
# Output the result to the console


# Problem 2: Number in Range
# Description:
# Create a program that checks whether a given number falls within a specified range, such as 10 to 20 (inclusive).

# Input: A number (integer)
num= int(input('enter a number'))
# Output: "The number is within the range." or "The number is outside the range."
10<num<20


# Hint:
# Use the and operator to check if the number is greater than or equal to 10 and less than or equal to 20.

# Problem 3: Password Strength Checker
# Description:
# Write a program that checks if  a user's password meets the following criteria:
listofletters=int()
# At least 8 characters long

# Contains at least one digit (0-9)

# Input: Password (string)

# Output: "Password is strong." or "Password is weak."

# Hint:
# Use the len() function to check the length and the any() function with a generator expression to check for a digit.

# Problem 4: Odd or Even and Multiple of 3
# Description:
# Create a program that determines if a number is odd or even and also checks if it is a multiple of 3.

# Input: A number (integer)
# Output:
# "Even and a multiple of 3."
# "Even but not a multiple of 3."
# "Odd and a multiple of 3."
# "Odd but not a multiple of 3."
# Hint:
# Use % for both the even check and the multiple of 3 check.

# Problem 5: Vowel or Consonant
# Description:
# Write a program that takes a single character as input and checks whether it is a vowel or a consonant. Assume the input is a lowercase letter.

# Input: A character (string of length 1)
# Output: "Vowel" or "Consonant"
# Hint:
# Use the in operator to check if the character belongs to the set {'a', 'e', 'i', 'o', 'u'}.