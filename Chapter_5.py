#Challenges

#1.) Create a list of your favorite musicians
fav_musicians = ["kygo", "avicii"]
print(fav_musicians)

#2.) Create a list of tuples, with each tuple containing the longitude
#    and latitude of somewhere you've lived or visited
scotland = (89.3, 78.2)
houston = (45.3, 12.7)
print(scotland)
print(houston)

#3.) Create a dictionary that contains different attributes about
#    you: height, favorite color, favorite author, etc.
stu_stu = {"height":74, "color":"blue", "author":"dan brown", "artist":"kygo"}
print(stu_stu)

#4.) Write a program that lets the user ask your height, favorite color, or
#    favorite author, and returns the result from the dictionary you created 
#    in the previous challenge
a = input("What would you like to know - height, color, author, or artist? ")
if a in stu_stu:
    descrip = stu_stu[a]
    print(descrip)
else:
    print("Not Found")

#5.) Create a dictionary mapping your favorite musicians to a list of your
#    favorite songs by them
my_artists = dict()

my_artists["glitch mob"] = "fortune days"
my_artists["kygo"] = "firestone"
my_artists["tyga"] = "taste"

print(my_artists)

#6.) Lists, tuples, and dictionaries are just a few of the containers built
#    into Python. Research Python sets. When would you use a set?