# 1- Python Standard Library
import ssl

# 2- Working with Path
from pathlib import Path
from time import ctime
import shutil
from zipfile import ZipFile
import csv
import json
import sqlite3
import time
from datetime import datetime, timedelta
import random
import string
import webbrowser

Path(r"C:\Program Files\Microsoft")  # Window
Path("usr/local/bin")  # MacOS, Linux
Path()  # path of the current folder
Path() / Path("ecommerce")  # combine path objects together
Path() / "ecommerce" / "__init__.py"  # combine path object and string
Path.home()

path = Path("ecommerce/__init__.py")  # sub folder and file
path.exists()
path.is_file()
path.is_dir()
print(path.name)  # file name with extension under this path
print(path.stem)  # file name without extension
print(path.suffix)  # file extension
print(path.parent)  # return parent folder "ecommerce"
path1 = path.with_name(
    "file.txt"
)  # /Users/eli/PycharmProjects/CompletePythonMastery/ecommerce/file.txt
print(path1.absolute())
print(path1)
path2 = path.with_suffix(".txt")
print(path2.absolute())
print(path2)

# 3- Working with Directories
# PosixPath and WindowPath class
# PosixPath is the standard use in Linux
# WindowPath is the standard use in Window
path3 = Path("ecommerce")
paths = [p for p in path3.iterdir() if p.is_dir()]
print(paths)
py_files = [p for p in path3.rglob("*.py")]
print(py_files)

# 4- Working with files
fpath = Path("ecommerce/__init__.py")
# fpath.exists()
# fpath.rename("name.txt")
# fpath.unlink() # delete the name
print(fpath.stat())
print(ctime(fpath.stat().st_ctime))  # creation time

# with open("__init__.py", "r") as file:
#     ...


# print(fpath.read_text())
# fpath.write_text("...")
# fpath.write_bytes()

# copy file and move to another
source = Path("ecommerce/__init__.py")
target = Path() / "__init__.py"

# It is a little bit tedious.
# target.write_text(source.read_text())

# Can use "shutil" class.
# It provides numbers of high leve operations for copying and
# moving files and the directories.
shutil.copy(source, target)
print(target.absolute())

# 5- Working with Zip Files
# import Zipfile from zipfile Module

# with ZipFile("files.zip", "w") as zip:
#     for path in Path("ecommerce").rglob("*.*"):
#         zip.write(path)


# read all file list from zip file
with ZipFile("files.zip") as zip:
    print(zip.namelist())
    info = zip.getinfo("ecommerce/__init__.py")
    print(info.file_size)
    print(info.compress_size)
    zip.extractall("extract")  # extrace files from zip to another directory

# 6- Working with CSV Files
# import csv module

# Writing csv file


# with open("data.csv", "w") as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow(["transaction_id", "product_id", "price", "quantity"])
#     writer.writerow(["100", "1", "1000", "3"])
#     writer.writerow(["101", "2", "230", "10"])
#     writer.writerow(["102", "3", "340", "8"])


# Read the csv file
with open("data.csv") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)


# 7- Working with JSON files
# import json module

# create json and write in path
# movies = [
#     {"id": 1,"Title": "Terminator", "Year": 1984},
#     {"id": 2,"Title": "Kindergarten Cop ", "Year": 1993}
# ]
#
# json_data = json.dumps(movies)
# Path("movies.json").write_text(json_data)
# Read json file and print out
json_data = Path("movies.json").read_text()
movies = json.loads(json_data)
print(movies)

# 8- Working with a SQLite Database
# import sqlite3 module

# Creating db and writing json data to database
# get the connection with Database using sqlite3.connect

# movies = json.loads(Path("movies.json").read_text())
# with sqlite3.connect("db.sqlite3") as connection:
#     command = "INSERT INTO Movies VALUES(?, ?, ?)"
#     for movie in movies:
#         connection.execute(
#             command, tuple(movie.values())
#         )  # sqlite3.OperationalError: no such table: Movies
#     connection.commit()


# Reading data from database
with sqlite3.connect("db.sqlite3") as connection:
    command = "SELECT * FROM Movies"
    cursor = connection.execute(command)
    # for row in cursor:
    #     print(row)
    movies = cursor.fetchall()
    print(movies)


# 9- Working with Timestamps
# import time
# floatiing point => numbers of seconds from the beginning of time 1692177694.655951


def send_emails():
    for i in range(10000):
        pass


start = time.time()
send_emails()
end = time.time()
duration = end - start
print(duration)

# 10- Working with DateTimes
# import datetime

dt1 = datetime(2018, 1, 1) + timedelta(days=1, seconds=1000)
print(dt1)
now = datetime.now()
print(now)
str_dt = datetime.strptime("2018/01/01", "%Y/%m/%d")
print(str_dt)
ts_dt = datetime.fromtimestamp(time.time())
print(ts_dt)
print(f"{ts_dt.year}/{ts_dt.month}")
print(ts_dt.strftime("%Y/%m"))
# compare date time
print(now > dt1)

# 11- Working with Time Deltas
duration = now - dt1
print(duration)
print("days ", duration.days)
print("seconds ", duration.seconds)
print("total seconds ", duration.total_seconds())

# 12- Generating random values

print(random.random())
print(random.randint(1, 20))
print(random.choice([1, 2, 3, 4]))
print(random.choices([1, 2, 3, 4], k=2))
print("".join(random.choices("abcdefghij", k=5)))
print(
    "".join(
        random.choices(string.ascii_letters + string.digits + string.punctuation, k=5)
    )
)
numbers = [4, 7, 9, 6]
random.shuffle(numbers)
print(numbers)

# 13- Opening the browser
# import webbrowser

print("Deployment Completed")
# webbrowser.open("https://www.google.com")

# 14- Sending emails
# 15- Working with Templates
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
from string import Template


def send_message():

    template = Template(Path("template.html").read_text())
    message = MIMEMultipart()

    receiver_email = "shooneli707@gmail.com"
    app_password = "qtugcwgmrqslfomr"

    message["from"] = "Ngwe Yee"
    message["to"] = receiver_email
    message["subject"] = "This is a python test "
    body = template.substitute(name="john")
    message.attach(MIMEText(body, "html"))
    message.attach(MIMEImage(Path("taeyeon.jpg").read_bytes()))
    try:
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(receiver_email, app_password)
            smtp.ehlo()
            smtp.send_message(message)
            print("Sent...")
    except Exception as e:
        print(e)
    finally:
        pass


# uncomment below line to send message
# send_message()

# 16- Command-line Arguments
import sys

if len(sys.argv) == 1:
    print("USAGE python3 main.py <password>")
else:
    password = sys.argv[1]
    print("Password: ", password)

# 17- Running external programs on the python script
import subprocess

try:
    # completed = subprocess.run(["ls", "-l"], capture_output=True, text=True, check=True)
    completed = subprocess.run(["false"], capture_output=True, text=True, check=True)
    # completed = subprocess.run(
    #     ["python3", "other.py"], capture_output=True, text=True, check=True
    # )
    print("args", completed.args)  # ['ls', '-l']
    print("returncode", completed.returncode)  # 0 -> success, any value -> error
    print("stderr", completed.stderr)  # None, b'' -> b means binary object
    print("stdout", completed.stdout)  # None, b''
except subprocess.CalledProcessError as ex:
    print(ex)
