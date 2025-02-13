# we use the .find method when we want to search a target for a specified substring.
# syntax: string.find(substring, start, end) "start" and "end" are optional attributes.

# Example 1
my_name = "My name is Abdullahi Bashir"
# print(my_name.find("Abdullahi"))
print(my_name.find("Abdullahi", 0, 20))

# Using the .index() method 
try:
    print(my_name.index("hey"))
except ValueError:
    print("Substring not found")

# counting occurences
# we use the .count() method to count the number of times a substring appears in a target string.
# syntax: string.count(substring, start, end) "start" and "end" are optional attributes.
name2 = "My name is Abdullahi Bashir"
print(name2.count("a", 0, 7))

# replacing substrings
# we use the .replace() method to replace a substring with another substring.
# syntax: string.replace(old_substring, new_substring, count) "count" is an optional attribute.
name3 = "My name is Abdullahi Bashir"
print(name3.replace("Abdullahi", "Abdullahy"))