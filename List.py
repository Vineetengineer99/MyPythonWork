#Intro to list.
# 1. A list is a collection of items in a particular order.
# 2. We can make a liat that includes the letter of the alphabet, the dibit from 0-9, or the name of
#    all the people in our country.
# 3. We can put anythong you want into a list, & the items in our list don't have to be related in any 
#    particular way.
# 4. In pyhton, square bracket([]) indicate a list, & individual elements in the list are seperated by commas.#
colors=['blue','red','green','yellow']
print(colors)

#Accessing elements in a list.
# 1. Lists are ordered collection, so we can access the list's elements, by telling pyhton
#   the position, or index of the desired.
# 2. To access an element in a list. write the name of the list followed by the index of the item enclosed 
#   in sq brackets#
print(colors[0])
print(colors[0].title())

#Using individual values from a list
#1. We can use individual value from a list just as you would any other variables.
#2. Ex: we can use f-string to create a mssg based on a value from a list.
#3. Let's try pulling the first bicycle from the list an composing a mssg using that value.#
msg=f"my fav color is {colors[0]}"
print(msg)

#Changing adding and removing elements
# 1. Most list you create will be dynamic.
#  -> Means build a list and then add and remove elements from it as your program runs.#

# MODIFYING ELEMENTS IN A LIST.
# 1. The elements for modifying an elements is similar to the syntax for accessing an elements in a list.
# 2. To change an elements, use the names of the list followed by the index of the elements you want to chnage,
# & then provide the new value you want that item to have.#
motor_cycle=['honda', 'yamaha', 'suzuki']
print(motor_cycle)
motor_cycle[0]='ducati'
print(motor_cycle)

#Adding elements to a list.
# 1. We might want to add a new elements to alist for many reasons.
# 2. Python provides several ways to add new data to existing list.
# 3. Ex: a. We might want to make new alien appear in a game.
#        b. Add new data to visua;ization.
#        c. Add new registered users to a website you've build.#
motor_cycle.append('ducati2')
print(motor_cycle)

#Inserting element to a list.
# 1. By using the insert() method we can add a new elements at any position in your list.
# 2. You do this by specifying the index of the new elements and the value of the new item.#
motor_cycle.insert(0, 'ducati3')
print(motor_cycle)

#Removing elements from a list
# 1. Often, you'll want to remove an item or a set of item from a list.
# 2. You can remove an item according to its position in the list or according to its value.#
del motor_cycle[0]
print(motor_cycle)

#Removing an item using pop() method
# 1. The pop() method removes the last itemz in a list, but if lets you work that item after removing.
# 2. The term pop comes from thinking of a list as a  stacking of items and popping one item off the top
#   of the stack.
# 3. In this analogy, the top of a stack corresponds to the end of a list.#
popped_motor_cycle= motor_cycle.pop()
print(motor_cycle)
print(popped_motor_cycle)
last_owned=motor_cycle.pop()
print(f"The last motorcycle i owned was a {(last_owned)}")

#Popping items from any position in a list.
# 1. To remove an item from any position in a list by including the index of the item you want to
#    remove in parenthesis, we can use pop.
# 2. When you use pop() method each time the item you work with is no longer started in the list.#
first_owned=motor_cycle.pop(0)
print(f"The first motorcycle i owned was a {first_owned}")

#Remving an item by value.
# 1. If you only know the value of the item youu want to remove, you can use the remove() method.
# 2. This method also used to work with a value that's being remove from a list.#
motor_cycle=['honda', 'ducati', 'suzuki']
motor_cycle.remove('ducati')
print(motor_cycle)

#Sorting a list temporarily with  the sorted() function.
# 1. To maintain the original order of a list but present it in a sorted order,
#   you can use the sorted() function.
# 2. The sorted() function lets you displays yours list in a particular order but doesn't affect the acctual
#   order of a list.#
cars=['bmw','audi','toyota','yahama']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
print(sorted(cars))

#Printing a list in reverse order.
# 1. To reverse the original order of a list,
#   you can use the reverse() method.
# 2. The reverse() method changes the order of a list permanently, but you can revert to the
#   original order anytime by applying reverse() to the same list a second time.#
cars.reverse()
print(cars)

#Finding the length of a list.
# 1. We can find length by using the len() function.
# 2. We'll find len() useful when you need to identify the number of aliens that still need to
#   be short down ina game.#
print(len(cars))

#WORKING WITH LIST
# Looping through an entire list.
# 1. You'll often want to run through all entries in alist, programming the same task with each item.
# 2. Or perhaps you'll want to display each headlines froma list of articles on a website.
#   when you want to do the same action with every items in a list, you can use python for loop.#
magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician)

#A dosen book at looping
# 1. The concept of looping is important because it's one of the most common ways a computer
#   automates repetitive tasks.
# 2. When you're using loops for the first time, keep in mind that the set of steps is seperated once for
#   each item in the list, no matter how many items are in the list, no matter how mmany items are in the list.
#   if you have a million items in your list, python repeats these steps a million times & usually very quickly.
# 3. Colon is neccessary.#

# Making numerical lists
# 1. List are ideal storing sets of numbers, & python provcide a variety of tools to help,
#   you work efficiently with list of numbers.#
 
# Using the range() function
# 1. Pyhton range() function makes it easy to genrated a series of numbers#
for value in range (1,5):
    print(value)

#Using range() to make a list of numbers
# 1. If you want to make a list of numbers, you can convert that results of range()
#   direcctly into a list using the list() function.
# 2. When you wrap list() around a call to the range() function, the output will be list of number.
# 3. We can also use the range() function to tell pyhton to skip numbers in a given range.
# 4. You can create almost any set of numbers you want to using the range() function.#
num=list(range(1,6))
print(num)
even=list(range(2,11,2))
print(even)
sqs=[]
for value in range(1,11):
    sq=value**2
    sqs.append(sq)
print(sqs)

#Simple statics with a list of numbers
# 1. Some python function are helpful when working with lists of numbers.#
digits=[1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

#List comprehensions.
# 1. The approach described earlier for genrating the list square consisted of
#   using three or four lines of code.
# 2. A list comprehension combines the for loop & the creation of new element into one line, and
#   automatically appends each new elements.
# 3. A list comp. allows you to generate this same list in just 1 line of code.#
sqs=[value**2 for value in range (1,11)]
print(sqs)

#Working with part of a list.
# 1. You can also work with a specific group of items in list, which python calls a slice.#

#Slicing a list.
# 1. To make a slice, you specify the index of the first & last elements you want to work with.
# 2. If you omit the first index in a slice, pyhton automatically starts your slice at the 
#   begining of the list.#
players=['virat','sachin','dhoni','hardik','rohit']
print(players[0:3])
print(players[1:4])

#Styling youur code.
# 1. Python programmer have agreed on ano. of styling convention to ensure that everyone's
#   code is structured the same way.#

#The style guide.
# 1. When someone wants to make a change to the python language,
#   they write a python enhancement proposal(PEP).
# 2. One of the oldest PEP's is PEP 8, which instructs python programmer on how to style their code.#

#UNPACKING SEQUENCES
# 1. Strings & tuples are example of sequences.
#   - indexing, slicing, concatenation, repetition operation applicable on sequence.
# 2. Sequence unpacking operation can be applied to sequence to get the components
#   - Multiple assignment statement.
#   -LHS & RHS must have equal length.#
student=('vineet',34,('python','amey',101))
name,roll,regdcourse=student
print(name)
print(roll)

x1,x2,x3,x4='aman'
print(x1,x2,x3,x4)

#LISTS
# 
# 1. Ordered sequence of values.
# 2. Written as a sequence of comma-seperated value between square bracket.
# 3. Values can be of diff. type.
#   - usually the items all have the same type.
# 4. List is also a sequence type.
#   - sequence operation are applicable.#
fib=[1,1,2,3,5,8,13,21,34,55]
print(len(fib))
print(fib[3]) #indexing
print(fib[3:]) #slicing
print([0]+fib) #concatenation
print(3*[1,1,2]) #repitition
x,y,z=[1,1,2]
print(x,y,z) # unpacking

#More operation on lists
# 
# L.append(x)
# L.extend(seq)
# L.insert(i,x)
# L.remove(x)
# L.pop(i)
# L.pop()
# L.index(x)
# L.count(x)
# L.sort()
# L.reverse()
# HERE: x is any value; seq is sequence value(list, string, tuple); x is any integer value.#