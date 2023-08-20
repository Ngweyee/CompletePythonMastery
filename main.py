# 1- Pypi introduction
# 2- Pip
# command to install package => pip3 install requests
# upgrade pip => pip3 install --upgrade pip
# list inside the package => pip3 list
import requests

response = requests.get("http://www.google.com")
print(response)

# 3- Virtual Environments
# create virtual environment for different versions
# source env/bin/activate    -> run file from virtual environment file

# 4- Pipenv
# install pipenv
# pipenv --venv  virtual directory run from pipenv
# pipenv shell -> activate the virtual environment
# exit -> deactivate

# 5- Virtual Environment in VSCode
# 6- Pip file
# when we install package using pip env, it generate two classes Pipfile & Pipfile.lock
# Pipfile => source, default packages, packages and requires (to keep track of the dependencies of the project and versions)

# 7- Managing Dependencies
# pipenv graph => list of all the installed dependencies.

# 8- Publishing Packages
# need to install 3 packages globally
# pip3 install setuptools wheel twine
