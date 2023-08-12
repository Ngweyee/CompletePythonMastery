from timeit import timeit  # to calculate the execution time of code

# 1- Exceptions
# date = int(input("Enter Date: ")) # Error
# print(date)

# 2- Handling Exception & 3- Handling Different Exceptions
try:
    age = int(input("Enter Age 1: "))
    xFactor = 10 / age
except (ValueError, ZeroDivisionError):  # handling more than one exception
    print("You didn't enter a valid age")
else:
    print("No exceptions were thrown.")
    print("Execution continues.")

# 4- Cleaning Up
try:
    myfile = open("app.py")
    age = int(input("Enter Age 2 : "))
    xFactor = 10 / age
except (ValueError, ZeroDivisionError):  # handling more than one exception
    print("You didn't enter a valid age")
except FileNotFoundError:
    print("There is no such file")
else:
    print("No exceptions were thrown.")
finally:
    myfile.close()

# 5- The With Statement
# 4- Cleaning Up
try:
    with open("app.py") as file:
        print("File is opened.")
    age = int(input("Enter Age 3 : "))
    xFactor = 10 / age
except (ValueError, ZeroDivisionError):  # handling more than one exception
    print("You didn't enter a valid age")
else:
    print("No exceptions were thrown.")

# 6- Raising Exceptions
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)

# 7- Cost of Exceptions
first_code = """ 
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)
"""

second_code = """ 
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age



xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""

print("Exectuion time for First Code :", timeit(first_code, number=10000))
print("Exectuion time for Second Code :", timeit(second_code, number=10000))
