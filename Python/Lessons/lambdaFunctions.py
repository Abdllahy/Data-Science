# LAMBDA FUNCTIONS
raise_to_power = lambda num1, num2 : num1 ** num2
print(raise_to_power(2,3))

# Write a lambda function to concatenate two strings (continent and country)
concatenate_two_strings = lambda continent, country: continent + " : " + country
print(concatenate_two_strings('Africa', 'kenya'))

# def lambda_inside_func (func, value):
#
# def square_root (a):
#     return a**(0.5)
# square_root("chris")

def sqrt (b):
    """returns the square root of a number but if the parameter passed is not a float / integer
    it will return an error message"""
    try:
        return b ** 0.5
    except TypeError:
        print("Input must be an integer or float value")
(sqrt("bi"))
