#NUMBERS
# 1) Numbers are used quite often in programming to keep score in games represent data in visualization, store info in web apps and so on.
# 2) Python treats number in several different ways depending on how they're being used. #

#Integers
# 1) You can (+), (-), (*), (/) integers in python.#

print("\nIntegers")
print(2+3) #add
print(2-3) #subtract
print(11-4) #subtract
print(11*4) #multiply
print(11/4) #divide
print(12/4) #divide
print(2**3) #raise to the power
print(2+3*4) #BODMAS
print((2+3)*4) #BODMAS


#Floats
# 1) Python calls any number with a decimals point a float.
# 2) This term is used in most programming language, and it refers to the fact that a decimal point canappears at any position in a number#

print("\nFloats")
print(0.1+0.3)  #add
print(0.3-0.2)  #subtract
print(0.2*0.3)  #multiply
print(0.3/0.2)  #divide

#Integers and float
# 1) When you divide any two numbers even if they are integers that results in a whole numbers, you'll always get a float#

print("\nIntegers and Float")
print(2/4)  #divide
print(2+1.5) #add
print(2-1.5) #subtract
print(2*1.5) #multiply
print(2**1.5) #rase to the power

#underscore in number
# 1) When you're writing long number you can group digits using underscore to make numbers= more readable.
# 2) When you print number that was defined using underscore, pyhton prints only the digits.#

print("\nUnderscore in numbers")
a= 14_00_000
print(a)

#Multiple assignment
# 1) You can assign values to more than 1 variables using just a single line.
# 2) This can help shorten your programs and make them easier to read; you'll use this technique most often when intializing a set of numbers.#

print("\nMultiple assignment")
a,b,c=12, 23, 34
print(a)
print(b)
print(c)

#Constant
print("\nConstant")
MAX=12345
print(MAX)