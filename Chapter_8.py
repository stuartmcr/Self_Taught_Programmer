#Challenges

#1.) Call a different function from the "statistics" module
import statistics
import random

v = random.randint(1,10)
w = random.randint(1,10)
x = random.randint(1,10)
y = random.randint(1,10)
z = random.randint(1,10)

numbers = []
numbers.append(v)
numbers.append(w)
numbers.append(x)
numbers.append(y)
numbers.append(z)
print(numbers)

a = statistics.mean(numbers)
b = statistics.median(numbers)
c = statistics.mode(numbers)

print(a)
print(b)
print(c)


#2.) Create a module named cubed with a function that takes a number
#    as a parameter, and returns the number cubed. Import and call the
#   function from another module
