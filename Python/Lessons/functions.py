def square():
    new_value = 4 ** 2
    print(new_value)

square()

def divide_by_2 (value):
    new_value = value / 2
    print(new_value)
divide_by_2(4)

print("---------------------------")

def square(value):
    new_value = value ** 2
    return new_value

number = square(2)
print(number)

print("---------------------------")

def multiply_by_100(prediction1, prediction2):
    new_value1 = prediction1 * 100
    new_value2 = prediction2 * 100
    return new_value1, new_value2
predictions = multiply_by_100(5,6,)
print(predictions)

print("---------------------------")
