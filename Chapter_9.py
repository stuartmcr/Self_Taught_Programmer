#Challenges

#1.) Find a file on your computer and print its contents using Python
import csv

my_list = list()
with open("file.csv", "r") as f:
    my_list.append(f.read())

print(my_list)


#2.) Write a program that asks a user a question, and saves their answer
#   to a file
import csv

x = input("Who's your fav artist?: ")
with open("file.csv", "w", newline='') as f:
    w = csv.writer(f, delimiter = ",")
    w.writerow(str(x))
