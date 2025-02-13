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