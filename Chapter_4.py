#Challenge

#1.) Write a function that takes a number as an input and returns that number squared
def squared(a):
    return a**2

print(squared(7))

#2.) Create a function that accepts a string as a parameter and prints it
def the_string(b):
    return str(b)

print(the_string("Hello, World!"))

#3.) Write a function that takes three required parameters and two optional parameters
def parameters(c, d, e):
    return c + d + e

f = 10
g = 12

required = parameters(5, 6, 7)
x = str(input("include optional values? yes or no: "))
if x == "yes":
    print(required + f + g)
else:
    print(required)


#4.) Write a program with two functions. The first function should take an integer
#    as a parameter and return the result of the integer divided by 2. The second
#    function should take an integer as a parameter and return the result of the 
#    integer multiplied by 4. Call the first function, save the result as a 
#    variable, and pass it as a parameter to the second function
def first_round(h):
    return h/2

pass_var = first_round(16)

def second_round(i):
    return i*4

final_var = second_round(pass_var)

print(pass_var) 
print(final_var)

#5.) Write a function that converts a string to a float and returns the result. Use
#    exception handling to catch the exception that could occur
def converter(j):
    return float(j)

a = input("give me a numeric string: ")
try:
    print(converter(a))
except ValueError:
    print("i said numeric")

#6.) Add a docstring to all of the functions you wrote in challenges 1-5

#prob1 - function to square a number
#prob2 - function to return a string
#prob3 - gives the option of choosing to include additional values or not
#prob4 - cycles the answer of the first function through the second
#prob5 - returns the float value of an inputted string
