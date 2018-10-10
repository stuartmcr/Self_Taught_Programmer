#Challenge

#1.) Print three different strings
print("string one")
print("another string")
print("the last string")

#2.) Write a program that prints a message if a variable is less than 10, and 
#    different message if the variable is greater than or equal to 10
x = int(input("pick a number between 1 and 20: "))

if x >= 10:
    print("x is greater than or equal to 10")
else:
    print("x is less than 10")

#3.) Write a program than prints a message if a variable is less than or equal 
#    to 10, another message if the variable is greater than 10 but less than or
#    equal to 25, and another message if the variable is greater than 25
y = int(input("pick a number between 1 and 40: "))

if y <= 10:
    print("y is less than or equal to 10")
elif y > 10 and y <= 25:
    print("y is greater than 10 but less than or equal to 25")
else:
    print("y is greater than 25")


#4.) Create a program that divides two variables and prints the remainer
a = int(input("input an odd number over 40: "))
b = int(input("pick an even number under 20: "))

c = a%b
print(c)


#5.) Create a program that takes two variables, divides them, and prints the quotient
d = int(input("input an odd number over 30: "))
e = int(input("pick an even number under 10: "))

f = d/e
print(f)

#6.) Write a program with a variable 'age' assigned to an integer that prints
#    different strings depending on what integer 'age' is
age = int(input("how old are you? "))

if age < 18:
    print("sorry, no voting for you")
elif age >= 18 and age < 21:
    print("scratch-offs are gonna have to do")
else:
    print("dobby is a free elf")

