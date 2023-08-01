# Variables && Variable Names
import math

student_count = 1000
rating = 4.99
is_published = False
course_name = "Python Programming"
print(student_count)
print(rating)
print(is_published)
print(course_name)

# Strings
course = "Python Programming"
print(len(course))
print(course[0])
print(course[-1])
print(course[0:3])
print(course[0:])
print(course[:3])
print(course[:])

# Escape Sequences
# \'
# \"
# \\
# \n

course = "Eli's Python 'Programming Journey"
print(course)

# Formatted String
first = "Ngwe Yee"
second = "Shoon"
full = first + " " + second
print(full)
full_name = f"{first} {second}"
full_name = f"{len(first)} {2 + 2}"
print(full_name)

# String Methods
course = " python programming "
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())
print(course.lstrip())
print(course.rstrip())
print(course.find("pro"))  # return index
print(course.replace("p", "j"))
print("pro" in course)
print("swift" not in course)

# Numbers
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 % 3)
print(10 // 3)
print(10**3)

x = 10
x = x + 3
x += 3
print(x)

# Working with Numbers
print(round(2.9))
print(abs(2.2))
print(math.ceil(2.3))
print(math.floor(2.5))
print(math.factorial(5))


# Type Conversion

print(bool(0))
print(bool(1))
print(bool(-1))
print(bool(5))
print(bool(""))
print(bool("False"))
