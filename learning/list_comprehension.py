#list conprehenison= a concise way to create list in python
                        #compact and easier to read than traditional loops
                        #[expression for value in iterable if condition]



# double= []
# for x in range(1,11):
#     double.append(x*2)
#     print(double)

# doubles=[x*2 for x in range(1,11)]
# print(doubles)
#THIS IS A LIST COMPREHENSION

#num times 3
# triples= [y*3 for y in range(1,11)]
# print(triples)

# squaring numbers
# squares=[x**2 for x in range(1,11)]
# print(squares)

# now working with strings:
# Fruits= ['apple', 'orange', 'banana', 'pineapple']

# # fruits=[ fruit.upper for fruit in Fruits]
# # print(fruits)
3
# #taking all of the fist characters in the term
# Fruit_char=[fruit[0] for fruit in Fruits]
# print(Fruit_char)

# numbers= [1,-2,3,-4,5,-6]
# positives_nums=[ num for num in numbers if num>=0]
# print(positives_nums)

# negative_nums=[ num for num in numbers if num<0]
# print(negative_nums)

# even_nums= [num for num in numbers if num%2==0]
# print(even_nums)
# odd_nums=[ num for num in numbers if num%2==1]
# print(odd_nums)


# grades= [85,42,79,90,56,61,30]
# passing= [ grade for grade in grades if grade>=60]
# print(passing)


numbers= [3,7,10,15,21]
double_values= [x*2 for x in numbers]
print(double_values)


values=[8,11,20,25,32,47,55]

odd_nums=[y for y in values if y%2==1]
print(odd_nums)


words=['apple', 'banana', 'cherry', 'date']


word_lengths=[len(word) for word in words ]
print(word_lengths)

num_two= [4,5,6,7,8,9,10]

squared_nums=[ x**2 for x in num_two if x%2==0]
print(squared_nums)

names=["Alice", "Bob", "Amanda", "Charlie", "Anna", "David"]

As_only=[ y for y in names if y[0]=='A']
print(As_only)

sentence=["hello", "world" ,"python", "is", "great"]

upper= [z.upper() for z in sentence]
print(upper)
################################################List comprehension###############################################
# List Comprehensions Practice #1
# To do the coding exercise below, you can choose different paths. While the correct path in programming is the one that returns the correct result, I encourage you to try applying list comprehension concepts to begin to assimilate them for the future. They can be very useful in your professional practice!

# Create a square_values list consisting of the numbers in the values list, squared.

# values = [1, 2, 3, 4, 5, 6, 9.5]




# List Comprehensions Practice #2
# To do the coding exercise below, you can choose different paths. While the correct path in programming is the one that returns the correct result, I encourage you to try applying list comprehension concepts to begin to assimilate them for the future. They can be very useful in your professional practice!

# Create an even_values list consisting of the numbers in the values list that (you guessed it!) are even.

# values = [1, 2, 3, 4, 5, 6, 9.5]




# List Comprehensions Practice #3
# To do the coding exercise below, you can choose different paths. While the correct path in programming is the one that returns the correct result, I encourage you to try applying list comprehension concepts to begin to assimilate them for the future. They can be very useful in your professional practice!

# For the following list of temperatures in degrees Fahrenheit, express these same values in a new list of temperature values in degrees Celsius. The conversion between type of units is as follows:

# °C = (°F - 32) * (5/9)

# or expressed in another way:

# (degrees_fahrenheit-32)*(5/9)

# The list of temperatures is as follows:

temperature_fahrenheit = [32, 212, 275]

temp_f=temperature_fahrenheit
# Store this new list in a variable called degrees_celsius


celcius=[((temp-32)*(5/9)) for temp in temp_f]
print(celcius)

