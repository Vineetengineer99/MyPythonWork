#TYpe Conversion (Type Cast)
# 1) Conversion of value of one type to other.
# 2) We are used to int <----> Float conversion in math.
#   - int 3 is treated as float 3.0 when a real no. is expected.
#   - float 3.6 is truncated as 3, or rounded up as 4 for integers contexts.
# 3) Types name also work as type converter function in python.#

a=12
print(float(a))  # conversion of int value into float

b=2.234
print(int(b))   # conversion of float value into int, it is truncation not rounding off.

c= 123
print(str(c))  #conversion of int value into string.


#Input
#1) Here you are taking a value from user.#
a=input("Enter a=")
print("a+5 will be:", int(a) +5)