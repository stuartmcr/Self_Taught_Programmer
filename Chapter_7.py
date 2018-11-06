#Challenges

#1.) print each item in the following list: ["the walking dead", "entourage",
#    "the sopranos", "vampire diaries"]
shows = ["the walking dead", "entourage", "the sopranos", "vampire diaries"]
for show in shows:
    print(show)

#2.) print all the numbers from 25 to 50
for i in range(25, 51):
    print(i)

#3.) print each item in the list from the first challenge and their indexes
shows = ["the walking dead", "entourage", "the sopranos", "vampire diaries"]
for index, show in enumerate(shows):
    print(show)
    print(index)
    

#4.) write a program with an infiite loop(q to quit) and a list of numbers.
#    each time through the loop ask the user to guess a number on the list
#    and tell them whether or not they guesses correctly
qs = ["Give me a number: "]

x = 0
while True:
    print("type q to quit")
    a = input(qs[x])
    if a == "q":
        break
    x = ( x + 1) % 1

#5.) Multiply all the numbers in the list [8, 19, 148, 4] with all the
#    numbers in the list [9, 1, 33, 83], and append each result to a third list
list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]

multiplied = []

for i in list1:
    for j in list2:
        multiplied.append(i*j)

print(multiplied)
