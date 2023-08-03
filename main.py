# 1- Defining Functions
# 2- Arguments


def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome Aboard")


greet("Ngwe Yee", "Shoon")


# 3- Types of Functions
# 1. preform a task
# 2. return a value


def greet(name):
    print(f"Hi {name}")


print(
    greet("Eli")
)  # return "Hi Eli" and None (default return value of the function or absence of the value)


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Eli")
print(message)

# 4- Keyword Arguments
def increment(number, by):
    return number + by


print(increment(2, by=1))  # by=1 is keyword argument

# 5- Default Arguments
def defualt_increment(number, by=1):
    return number + by


print(defualt_increment(2))
print(defualt_increment(2, 5))

# 6- xargs
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


result = multiply(1, 2, 3, 4, 5)  # () tuple => list contain objects
print(f"total is {result}")

# 7- xxargs
def save_user(**user):
    print(user)
    print(user["id"])
    print(user["name"])
    print(user["age"])
    print(user["is_student"])


save_user(id=1, name="Eli", age=29, is_student=False)

# 8- Scope => def: the region of the code where a variable is defined.
def scope_greet():
    scope_message = "a"
    return scope_message


print(scope_greet())

# message variable is inside the scope of scope_greet() function. Cannot access from the outside of the function.
# print(scope_message)


message = "g"


def greet(name):
    # global message  # rely on the global variable from above
    # message = "l"
    print(message)


def send_email(name):
    global message  # rely on the global variable from above
    message = "l"
    print(message)


name = "Eli"
greet(name)
send_email(name)


# 9- Debugging
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
        return total


print("Start")
print(multiply(1, 2, 3))

# Exercise
def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return "FizzBuzz"
    elif input % 3 == 0:
        return "Fizz"
    elif input % 5 == 0:
        return "Buzz"
    else:
        return input


print(fizz_buzz(6))
