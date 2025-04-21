# Variables
message = "Hello, World!!!"
print(message)

# Data types
# 1) String
name = "Shahid Ali"
# 2) Integer
age = 21
# 3) Boolean
isMarried = False
# 4) Float
height = 5.9
# 5) List
fruits = ["Apple", "Banana", "Mango"]
# 6) Tuple
fruitsTuple = ("Apple", "Banana", "Mango")
# 7) Dictionary
fruitsDict = {"Apple": 1, "Banana": 2, "Mango": 3}
# 8) Set
fruitsSet = {"Apple", "Banana", "Mango"}
# 9) NoneType
noneType = None
# 10) Complex
complexNumber = 1 + 2j
# 11) Range
rangeNumber = range(1, 10)
# 12) Bytes
bytesNumber = b"Hello"
print(f"Name: {name}, Age: {age}, Is Married: {isMarried}, Height: {height}, List: {fruits}, Tuple: {fruitsTuple}, Dictionary: {fruitsDict}, Set: {fruitsSet}, NoneType: {noneType}, Complex: {complexNumber}, Range: {rangeNumber}, Bytes: {bytesNumber}")


# Variable with same name
name = "Shahid Ali"
name = "John Doe"
print(name)


# Concatenation
firstName = "Shahid"
lastName = "Ali"
fullName = firstName + " " + lastName
print(fullName)


# f-strings
firstName = "Shahid"
lastName = "Ali"
fullName = f"Hello {firstName} {lastName}"
print(fullName)


_name = "Shahid"
name = "Ali"
age = 21
print(f"Hello {_name}, you are {age} years old.")
print(f"Hello {name}, you are {age} years old.")


# Checking data types
name = "Shahid Ali"
print(type(name))
print(id(name))


# Operators
# Operators are used to perform operations on variables and values.
"""
Arithmetic Operators:         +, -, *, /, %, //, **
Comparison Operators:         ==, !=, >, <, >=, <=
Assignment Operators:         =, +=, -=, *=, /=, %=, //=, **=
Bitwise Operators:           &, |, ^, ~, <<, >>
Identity Operators:         is, is not
Membership Operators:      in, not in
Logical Operators:         and, or, not

"""

# Arithmetic Operators
# + - * / % // **
# c = a - b
# c = a * b
# c = a / b
# c = a % b
# c = a // b
# c = a ** b # 10^3 = 10*10*10
a = 10
b = 3
# print(10 + b - 2 * a + 10)
#     10 + 3    -20  + 10
#     10 + 3        -10
#        3

# Comparison Operators
# == != > < >= <=
a = 10
b = 10
# c = a == b
# c = a != b
# c = a > b
# c = a < b
# c = a >= b
# c = a <= b
# print(c)