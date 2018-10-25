#Challenges

#1.) Print every character in the string "Camus"
task_1 = "Camus"
print(task_1[0])
print(task_1[1])
print(task_1[2])
print(task_1[3])
print(task_1[4])

#2.) Write a program that collects two strings from a user, inserts them into the
#    string "yesterday i wrote a (response1). I sent it to (response2!)" and
#    prints a new string
a = input("give me a noun: ")
b = input("give me a name: ")

c = "yesterday i wrote a {}. i sent it to {}".format(a, b)
print(c)

#3.) Use a method to make the string "aldous Huxley was born in 1894."
#    grammatically correct by capitalizing the first word of the sentence
d = "aldous Huxley was born in 1894".capitalize()
print(d)

#4.) Take the string "where now? who now? when now?" and call a method that
#    returns a list that looks like: ["where now?", "who now?", "when now?"]
e = "where now? who now? when now?".split("?")
print(e)

#5.) Take the list ["the", "fox", "jumped", "over", "the", "fence", "."] and
#    turn it into a grammatically correct string. There should be a space 
#    between each word, but no space between the word fence and the period
f = ["the", "fox", "jumped", "over", "the", "fence", "."]
g = " ".join(f)
print(g)

#6.) Replace every instance of "s" in "A screaming comes across the sky" with
#    a dollar sign


#7.) Use a method to find the first index of the character "m" in the string
#    "Hemingway"


#8.) Find a dialogue in your favorite book and turn it into a string


#9.) Create the string "three three three" using concatenation, and then again
#    using multiplication


#10.) Slice the string "it was a bright cold day in april, and the clocks were
#    striking thirteen" to only include characters before the comma