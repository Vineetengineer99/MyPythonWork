#Naming and Using Variables
# 1) Variable names can obtain only letters, numbers and underscores.
# 2) Space are not allowed in variable names, but underscores can be used to separate words in variable names.
# 3) Avoid using python keywords & function names as variables names.
# 4) Variables names should be short but descriptive.
# 5) Using the lowercase letter l & the uppercase letter O.#

name= "vineet kumar singh"
print(name.title())
print(name.upper())
print(name.lower())

first_name="vineet "
last_name="kumar singh"
full_name=f"{first_name}{last_name}"
print(full_name)

message=f"Hello, {full_name}"
print(message)