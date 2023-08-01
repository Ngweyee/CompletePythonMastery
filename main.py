# Comparison Operators
ten = 10
print(ten > 3)
print(ten >= 3)
print(ten < 20)
print(ten <= 20)
print(ten == ten)
print(ten == "10")
print(ten != "10")
print("bag" > "apple")
print("bag" > "Bag")
print(ord("b"))
print(ord("B"))

# Conditional Statements
temperature = 23
if temperature > 30:
    print("It is hot")
    print("Drink more water")
elif temperature > 20:
    print("It is a nice day")
else:
    print("It's cold")

print("Done")


# Ternary Operator
age = 16
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)

# Logical Operators
high_income = True
good_credit = True
is_student = False

if high_income or good_credit:  # and, or
    print("Eligible")
else:
    print("Not Eligible")


if (high_income or good_credit) and not is_student:
    print("Eligible")
else:
    print("Not Eligible")

# Short-circuit evaluation
high_income = False
good_credit = True
student = True

if high_income or good_credit and not student:
    print("Eligible")

# Changing Comparisons Operators
# age should be between 18 and 65
age = 22

# if age >= 18 and age < 65 :
if 18 <= age < 65:
    print("Eligible")


# Exercise
if 10 == "10":
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("c")

# For loops
for number in range(3):
    print("Attempt ", number + 1, (number + 1) * ".")

for number in range(1, 10, 2):
    print("Attempt ", number, number * ".")

# For ... Else
successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
else:
    print("Attempted 3 times and fail")

# Nested Loop
for x in range(5):
    for y in range(3):
        print(f"({x} , {y})")

# Iterables
print(type(5))
print(type(range(5)))

for x in range(5):
    print(x)

for x in "Python":
    print(x)

for x in [1, 2, 3, 4]:
    print(x)

# While Loops
number = 100
i = 0
while number > 0:
    print(number)
    number //= 2

print(" ")

command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)

# infinite loops
while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break


# Exercise
data = range(1, 10)
count = 0
for i in data:
    if i % 2 == 0:
        print(i)
        i += 1
        count += 1

print(f"There are {count} even numbers")
