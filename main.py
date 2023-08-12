from array import array
from sys import getsizeof
from pprint import pprint

# 1- Lists
letters = ["a", "b", "c", "d"]
print(letters)
matrix = [[0, 1], [2, 3]]
print(matrix)
zeros = [0] * 5
combined = zeros + letters
print(combined)
numbers = list(range(20))
print(numbers)
chars = list("Hello World")
print(len(chars))

# 2- Accessing Items
letters = ["a", "b", "c", "d"]
print(letters[0])
print(letters[-1])
# letters[0] = "A"
print(letters)
print(letters[0:3])
print(letters[:3])
print(letters[0:])
print(letters[::2])

numbers = list(range(20))
print(numbers[::2])
print(numbers[::-1])

# 3- List Unpacking
numbers = [1, 2, 3]
first, second, third = numbers

data = [1, 2, 4, 5, 3, 6, 2, 6, 7, 4]
f, s, *other = data
f, *other, last = data
print(f, last)
print(other)


first = numbers[0]
second = numbers[1]
third = numbers[2]

# 4-Looping over lists
letters = ["a", "b", "c", "d"]
for char in enumerate(letters):
    print(char)  # (0, 'a'), (1, 'b'), (2, 'c'),(3, 'd') => tuples (read only)
    print(char[0])  # index


# unpacking and tuple
for index, char in enumerate(letters):
    print(index, char)

# 5- Adding and Removing item
letters = ["a", "b", "c"]

# Adding
letters.append("d")
letters.insert(0, "A")
print(letters)


# Removing
letters.pop()
letters.remove("b")  # value want to remove
del letters[0:1]  # delete with range
print(letters)

# 6- Finding Items
letters = ["a", "b", "c"]
print(letters.count("d"))
if "d" in letters:
    print(letters.index("d"))

# 7- Sorting Lists
numbers = [3, 51, 2, 8, 6]
# numbers.sort()
# print(numbers)
# numbers.sort(reverse=True)
# print(numbers)
print(
    sorted(numbers, reverse=True)
)  # doesn't modify the original list, generate new sorted list
print(numbers)  # original list

items = [
    ("Product1", 15),
    ("Product2", 9),
    ("Product3", 16),
]


def sort_items(item):
    return item[1]


items.sort(key=sort_items)
print(items)

# 8- Lambda Functions

# items.sort(key=lambda parameters: expression)
items.sort(key=lambda item: item[1])
print(items)

# 9- Maps
items = [
    ("Product1", 15),
    ("Product2", 9),
    ("Product3", 16),
]
prices = []


# for item in items:
#     prices.append(item[1])  # transform list of tuples item into list of prices
#
# print(prices)

x = list(map(lambda item: item[1], items))

# 10- filter function
filtered = list(filter(lambda item: item[1] >= 10, items))

# 11- Lists Comprehensions
prices = list(map(lambda item: item[1], items))
prices = [item[1] for item in items]
print(prices)
# 10- filter function
filtered = list(filter(lambda item: item[1] >= 10, items))
filtered = [item for item in items if item[1] >= 10]
print(filtered)

# 12- Zip Function
list1 = [1, 2, 3]
list2 = [10, 20, 30, 40]

print(list(zip(list1, list2)))
print(list(zip("defg", list2)))

# 12- Stack LIFO => LAST IN - FIRST OUT
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
last = browsing_session.pop()
print(last)
print(browsing_session)
print("redirect ", browsing_session[-1])
# browsing_session.clear()
if not browsing_session:
    print("Disable the Back Button")

# Recap
# browsing_session = [1, 2]
# browsing_session.append(1)  # Add on the top of the stack
# browsing_session.pop()  # Remove on the top of the stack
# if not browsing_session:  # Check whether item in the stack is empty or not
# item = browsing_session[-1]  # Get the item on the top of the stack

# 13- Queues FIFO => FIRST IN - FIRST OUT
from collections import deque

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)

if not queue:
    print("empty")
else:
    print("It is not empty")

# Tuple
point = 1, 2
print(type(point))
point = ()
print(type(point))
point = (1, 2) * 3
print(type(point))
print(point)
point = (1, 2) + (3, 4)
print(type(point))
print(point)
point = tuple([1, 2])
print(point)
point = tuple("Hello World")
print(point)
point = (1, 2, 3)
print(point[0:2])
x, y, z = point  # unpack the tuple
if not 10 in point:
    print("Exists")

# point[0] = 10  # Error, Tuple is not immutable

# 16- Swapping Variables
x = 10
y = 11

# need temp(z) variable
# temp = x
# x = y
# y = z

x, y = y, x

print(f"x is {x}")
print(f"y is {y}")

# 17- Arrays
# reference => https://docs.python.org/3/library/array.html#module-array
# Every object inside array show be the same type, which is determined at the time of creating the array
# "i" => typecode (signed int)
numbers = array("i", [1, 2, 3])

# numbers[0] = 1.0 # This line will produce the error, cannot accept float


# 18- Sets
numbers = [1, 1, 2, 3, 4]
unique = set(numbers)
print(unique)
second = {1, 4}
second.add(5)
second.remove(5)
len(second)
print(unique)

first = set(numbers)
second = {1, 5}

print(first | second)  # merge two lists and take unique value for duplicate fees.
print(first & second)  # 1 is the only number that exists in both sets
print(first - second)  # remove same values from first list
print(first ^ second)  # items that are either first or second sets but not both

# TypeError : 'set' object is not support indexing
# print(first[0])

# 19- Dictionaries
point = {"x": 1, "y": 2}
point = dict(x=2, y=2)
point["x"] = 10
point["z"] = 20
if "a" in point:
    print(point["a"])
print(point.get("a", 0))  # will return none, can pass the default value if none
del point["x"]
print(point)

# How to loop over dictionary
for key in point:
    print(f"Key is {key} and value is {point[key]}")

# another way
for x in point.items():
    print(x)  # each iteration returns a tuple

# unpack the above code from tuple to key and value
for key, value in point.items():
    print(key, value)  # each iteration returns a tuple

# 20- Dictionary Comprehensions
data_values = []
# for x in range(5):
#     values.append(x * 2)

# [expression for item in items]
vk = [xx * 2 for xx in range(5)]  # dictionary comprehension []
print(f"x0 is {vk}")
print(vk[1])

# set comprehension
s_val = {a * 2 for a in range(5)}
print(s_val)

# dictionary comprehension
dict_values = {x: x * 2 for x in range(5)}
print(dict_values)

# tuple comprehension
tuple_value = (x * 2 for x in range(5))
print(tuple_value)  # just only produce "generator object"

# 21- generator expressions
# Use Generator expression to create generator object
# when we are dealing with a really large data set or
# potientially dealing with infinite stream of data

gen_value = (x * 2 for x in range(1000000))
print("gen: ", getsizeof(gen_value))  # output 208
# print(len(gen_value))  # generator() no len

# list_size = [x * 2 for x in range(1000000)]
# print("list: ", getsizeof(list_size))  # output => 8448728


# 22- Unpacking Operator
unpack_number = [1, 2, 3]
print(unpack_number)  # output is list => [1, 2, 3]
print(1, 2, 3)  # output is unpacked => 1 2 3
print(*unpack_number)  # add * at the start, it will unpack the list

print([*range(5), *"Eli"])
unpk_first = [1, 2]
unpk_last = [3]
print([*unpk_first, *"Ngwe", *unpk_last, *"Shoon"])

# unpack the dictionary
# if two dictionaries have same key, we use the latest key and value
d_first = {"x": 1}
d_second = {"x": 10, "y": 2}

d_combined = {**d_first, **d_second, "z": 12}
print(d_combined)


# Exercise
# Q: Write a program to find the most repeated character in this text.
sentence = "This is a common interview question"

char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

char_frequency_sorted = sorted(
    char_frequency.items(), key=lambda kv: kv[1], reverse=True
)
pprint(char_frequency_sorted[0])

# Below are quick examples
# Consider the set with integers
myset = set({12, 32, 6, 56, 78, 90, 54, 67})

# Example 1: Sort the elements in the set.
print("Sorted Set: ", sorted(myset))

# Example 2: Sort set in reverse order.
print("Sorted Set: ", sorted(myset, reverse=True))

# Consider the set with strings
myset = set({"hello", "welcome", "to", "sparkby", "Examples"})

# Example 3: Sort the elements in the set.
print("Sorted Set: ", sorted(myset))

# Example 3: Sort elements in custom order
print("Sorted Set: ", sorted(myset, key=len))
