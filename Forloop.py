#For LOOP
# General form
# for variable in sequence:
# stmt#

# Q1. Print sum reciprocal of the first 100 natural no.s#
rsum=0.0
for i in range (1,101):
    rsum=rsum+1/i
print(rsum)

#For loop in python
#1. First evaluate the sequence to get a list of values.
#2. If there are more value in the sequence then goto step 3, otherwise exit the loop.
#3. Find the variable to the next value in the sequence.
#4. Execute statement.
#5. Goto step 2. #

# Geometric progression
# 1. Given +ve real no.s r & a, & a +ve integer n, the nth term of the geometric progression with
#   as the first term & r as the common ratio is ar^n-1#

#WAP that given r,a &n display the first n terms of the corresponding geometric progression.
r=float(input('r='))
a=float(input('a='))
n=int(input('n='))
term=a
print(term)
for i in range (1,n):
    term= term*r
    print(term)

#Nested loops.
# 1. Loop within a loop.
# 2. Many interation of inner loop. -> one iteration of outer loop.#
for i in range(1,9):
    for j in range(1,6):
        print(i*j, end=' ')
    print()

for i in range(1,6):
    for j in range(1,2*i):
        print(j, end=' ')
    print()

for i in range(1,4):
    for j in range(1,2*i):
        print(j, end=' ')
    print()