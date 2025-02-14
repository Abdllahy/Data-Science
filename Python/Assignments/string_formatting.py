# FORMATTING IN STRINGS (With Code Examples)
# Look into the following methods of formatting 
#    a) Positional Formatting
#         i) Reodering Values
#         ii) Named Placeholders
#         iii) Format Specifiers
#    b) Formatted String iterals 
#         i) F-strings
#         ii) Type Conversion
#         iii) Format Specifiers(datetime)
#         iv) Escape Sequences in F-strings
#    c) Template Method of Formatting strings
#         i) Substitution
#         ii) Safe Substitution


# Why should you use 
#  - `stt.format()
#  - f-strings
#  - Template strings 
# """

# Positional Formatting
# Positional formatting is the most common type of string formatting. 
# It uses the format() method to format a string by replacing placeholders with values. 
# The placeholders are defined using curly braces {} and the values are passed as arguments to the format() method.

# Example 1
print("I am learning {} at {}".format("Python", "Zindua School"))
print("-----------------------")

# Example 2
course = "Python"
school = "Zindua School"
print("I am learning {} at {}".format(course, school))
print("-----------------------")

# Reordering Values
# You can reorder the values by specifying the index of the values in the format() method. 
# The index is defined inside the curly braces {} and starts from 0.

# let's compare these examples
# Example 3
print("This {} program is part of the {} course".format("Python", "Data Science"))
print("-----------------------")

# Example 3.1
print("{1} career is such a vital path in the {0} ecosystem".format("Tech", "Data Science"))
print("-----------------------")

# Named Placeholders
shopping_dict = {"item": "Laptop", "price": 80000}
print("The cost of this {value[item]} is ksh {value[price]}".format(value=shopping_dict))
print("-----------------------")

# Format Specifier
# Format specifiers are used to format the output of the values. 
# They are defined after a colon : inside the curly braces {}.

# Example 4
print("The value of {} is approximately {:f}".format("pi", 3.14159))

print("-----------------------")

# Example 4.1
print("The value of {} is approximately {:.2f}".format("pi", 3.14159))
print("-----------------------")

# Formatted String Literals - f-strings
# f-strings are a new way to format strings in Python. 
# They are prefixed with the letter f and the placeholders are defined using curly braces {}.

# Example 5
name = input("Enter your name: ")
course = "Python"
print(f"Hello, {name}. Welcome to the {course} course")
print("-----------------------")


# Format Specifiers - datetime
from datetime import datetime
print(f"The current date and time is {datetime.now():%Y-%m-%d %H:%M:%S}")

# Template Method of Formatting strings
#         i) Substitution

zindua_school_courses = ["Python", "Data Science", "Machine Learning"]
your_course = input("Enter your course: ")
from string import Template
if your_course in zindua_school_courses:
    print(Template("I am learning $course at Zindua School").substitute(course=your_course))
else:
    print("Course not found")

print("-----------------------")
#         ii) Safe Substitution
# Safe substitution is a method of formatting strings that uses the safe_substitute() method. 
# It is similar to the substitute() method but it does not raise an exception if the placeholder is not found.

# Example 6
from string import Template
fav_meal = Template("$name likes to eat $meal")
print(fav_meal.safe_substitute(name="James", meal="Pizza"))
print("-----------------------")