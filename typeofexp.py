#Element of python
# 1)A pyhton program is a sequence of defination & commands (statement).
# 2)Commands manipuate objects.
# 3)Each object is associated with a type.
# 4)Type: - A set of value.
#         - A set of operation on these values.
# 5)Experession: An operation combination of object and operators.#

#Type
# 1) We have been using types.
# 2) In school mathematics.
#   - Natural number: * Value: 1, 2, 3....
#                     * Operation: + - * / < >....
#   - Complex number: * Value: 5+3i, 7+2i....
#                     * Operation: + - * / conjugate
#                     * Oparaion >,< are NOT VALID#

#Types in Python
# 1) int: Bounder integers. eg. 7877, -34
# 2) float: Real number. eg. 3.14, 2.0
# 3) long: Long integers with unlimited precision.
# 4) str: String. eg. 'hello' , 'C'.
# 5)Scalar: -Indivisible objects that do not have internal structures.
#           -int(Signed integers), float(floating point), bool(Boolean), Nonetype.
# * Nonetype is a special types with a single value.
# * The value is called None.
# 6)Non-Scalar: - Object having internal structures.
#               - str(strings).#

#Findimg types of expressions.
# 1) You can use 'type' function to find the type of an expression.#
a=50
print(type(a)) #int

b=-50
print(type(b)) #int

c=True
print(type(c)) #bool

d='aman'
print(type(d)) #str

e=3.455
print(type(e)) #float