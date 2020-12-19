#TUPLES
# 1. A tuple consists of a number of values seperated by commas.#
t='intro to python', 'vineet',101
print(t)
print(t[0])
print(t[2])
print(type(t))

#empty & singleton tuples#
empty=()
singleton=1, #Note the , at end

#Nested tuples
# 1. Tuples can be nested.
# 2. Course tuple is copied into student.
#   - Changing course doesn't affect student.#
course='python','vineet',101
student='vector',34,course

#Length oa a tuple
# 1. len function gives the length of a tuple.#
print(len(empty))
print(len(singleton))
print(len(course))
print(len(student))

#More operation on tuples
# 1. Tuples can be concatenated, repeated, indexed & sliced.#