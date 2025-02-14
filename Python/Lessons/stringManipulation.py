# Type of inbuilt functions for strings
my_name = 'Abdullahi Bashir'
print(len(my_name))

# Indexing
# print(my_name[-7:])
print(my_name[0:6:2])

print("--------------------")
first_name = my_name.split()[0]
print(first_name)

students = 'My name is Abdullahi Bashir'
# students_list = students.split(sep=",")
students_list = students.split(sep=' ', maxsplit=2)
print(students_list)
# split a string starting from the right

student_left = students.rsplit(sep=" ", maxsplit=2)
print(student_left)

# Escape sequence
# we can escape a sequence of characters in a string using \n and \r
# \n - new line
# \r - carriage return

sentence1 = "I am a teacher at\n University of Nairobi"
print(sentence1)
print("-----------------------")
sentence2 = "I am a teacher at\r University of Nairobi"
print(sentence2)


sentence3 = "i am a student at\r Zindua school"
print(sentence3)

print("-------------------")
# JOINING STRINGS
# we use the .join() method to join strings
# syntax: separator.join(iterable)

my_list = ["i", "am", "a", "student", "at", "zindua", "school"]
print(" ".join(my_list))

print("====================")
# stripping characters from a string
# we use the .strip() method to remove the characters from a string
# syntax: string.strip(characters)

sentence4 = "i am a student zindua school"
print(sentence4.strip("i am school"))
# print(sentence4.strip())