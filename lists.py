#********************************************************************
                                                                  
 #  Team Edge list Challenges!                                     
  
 #  Use this program to learn about Python lists:
    
 #  1. Declare and store data in lists
 #  2. Access list data by index
 #  3. Modify list data by index
 #  4. Multi-dimensional lists (lists inside lists!)
 #  5. List methods: append() and pop()
 #  6. The length of the list - introduce conditionals
 #  7. Strings as sequences - join() split() 
 #  
 #  Follow the -->To Dos ! run the program to test often and debug
 # ***************************************************************





print("------------------- CHALLENGE 1 -------------------")
#This is an empty Python list:
empty_list = []

#this list has 5 Strings. We can print it:
names = ["Julian", "Wolf", "Alex", "Steph", "Alessandro"]
print("names: " + str(names))  

#-->TODO: Declare another list called friends with at least 5 strings inside (if you don't have 5 friends make them up!)

friends = ["Ivy", "Kevin", "Amy", "Aizah", "Saamir"]
print("friends: " +str(friends))

#this list holds numbers
numbers = [12.9, 23.4 , 100, 3.1415 , 500, 1.20]
print("numbers: " + str(numbers)) 

#-->TODO: Declare another list and add in at least 5 numbers. Why five? I don't know. It just feels right.

numbers = [1, 5, 3, 0, 6]
print("numbers: "+str(numbers))


#this list has mixed data types. It's allowed in Python!
random_stuff = ["Aardvark", True, False, 1.23, "Grandpa"]
print("random: " + str(random_stuff))

#-->TODO: Declare and log a list filled with the first 5 things that come into your head, booleans, Strings, numbers are all cool,

random_stuff = ["hannah", "boolean", "montana", "happy", "grapes"]
print("random: " + str(random_stuff))

#-->TODO: Declare and log two more lists with whatever you want. 

animals = ["sheep", "pigs", "dogs", "puppies", "cat"]
print("animals: " + str(animals))
cities = ["new york, los angles, chicago, seattle, tampa"]
print("cities:" + str(cities))

print("------------------- CHALLENGE 2 -------------------")
 
#This code logs the first element of the names list:
print("The first name is " + names[0])

#-->TODO: Print the name of your best friend from your friends list

print("Allison")

#-->TODO: Print the first AND last elements of any list you made, or make a brand new one.

print("New york")
print("Tampa")

print("------------------- CHALLENGE 3 -------------------")
#this code changes the value of the second element of the names list, then we print the list:
names[1] = "Alyssa"
print(names)

#-->TODO: Replace your friends! Modify the list to replace any or all of your friends with new ones.
names[0] = "Dog"
names[1] = "Hannah"
names[2] = "Hansel"
names[3] = "Betty"
names[4] = "Alex"
print(names)

#The code below uses the times_ten() function to multiply the first element in our list by 10:
def times_ten(number):
    number = number * 10
    return number

numbers[0] = times_ten(numbers[0])
print(numbers)

#-->TODO: Write another function that multiplies a number by 1000 and print the list, as above 

def times_hundred(number):
    number=number*1000
    return number

numbers[0] = times_hundred(numbers[0])
print(numbers)

#-->TODO: Replace your random list elements with anything you want, using the index. 

random_stuff = ['bears', 'pig']
random_stuff[1] = "burger" 
print(random_stuff)
print("------------------- CHALLENGE 4 -------------------")

#As it turns out, you can also store lists within lists! Declare them and store them as variables.
child_list_1 = ["This", "is" , "a", "meaningless", "list"]
child_list_2 = ["This" ,"list" , "is", "also" , "meaningless"]
parent_list = [child_list_1, child_list_2]
print("This list has babies: " + str(parent_list))

#-->TODO: Store and print all the lists we have worked on thus far in a new parent list

numbers = [1, 5, 3, 0, 6]
friends = ["Ivy", "Kevin", "Amy", "Aizah", "Saamir"]
random_stuff = ["hannah", "boolean", "montana", "happy", "grapes"]
animals = ["sheep", "pigs", "dogs", "puppies", "cat"]
cities = ["new york, los angles, chicago, seattle, tampa"]

parent_list = [numbers, friends, random_stuff, animals, cities]
print(parent_list)


print("------------------- CHALLENGE 5 -------------------")

#We can add elements into a list wihtout replacing anything. Using append() adds an element to the END of the list:
movies = ["Toy Story 4", "The Dark Knight", "Parasite"]
print("Movies: " + str(movies))
movies.append("Joker")
movies.append("Black Panther")
print("Movies now has: " + str(movies))

#-->TODO: Declare a list with 5 favorite songs

songs = ["cold", "earned it", "middle of the night", "cardigan", "solo"]

#-->TODO: Add 2-3 more songs using .append() and print both before and after.

songs.append("Happy")
songs.append("Sad")
print (songs)

#We can also remove elements using .pop(), which removes the last element or the element at the given index. You can store it after it comes out:
cities = ["New York", "Oakland", "Las Vegas", "Topeka"]
print("cities: " + str(cities))
unwanted_city = cities.pop()
print("unwanted city: " + str(unwanted_city))

#-->TODO: remove your last song using .pop() and print the removed element as above
print("songs: " + str(songs))
unwanted_songs = songs.pop()
print("unwanted songs " + str(unwanted_songs))
#Note: there are more methods to remove and modify list elements. We will cover those later

print("------------------- CHALLENGE 6 -------------------")

#Lists have properties. one of the most important is the size, or length. Here are two examples:
print(f"I have {len(names)} friends")

how_many_cities = len(cities)
print(f"There are {how_many_cities} ciites in my list")

#-->TODO: Print out the number of friends, or other items from other lists using string literals as above

print(f"I have {len(friends)} friends")

how_many_cities = len(cities)
print(f"There are {how_many_cities} cities in my list")

#The len() function is key, especially in conditionals or to simply count how many times to do something.

if len(numbers) > 3:
    print("There are more than 3 numbers in my list")
else:
    print("I need more numbers in my list!!!")

#-->TODO: Write another if/else statement to check the size of your songs list. If you have 5 of less, add two more songs!

if len(songs) > 3:
    print("There are more than 3 songs on my list")
else:
    print("I need more songs on my list")


print("------------------- CHALLENGE 6 -------------------")

#Strings can also be thought of lists:
sentence = "I am a boring sentence."
boring_list = sentence.split(" ") #split the sentence by each space to get a list of words
print("boring sentence as a list: " + str(boring_list))

word = "Abracadabra"
word_split_list = word.split() #split by nothing, and you get each character in the string as its own element.
print("letter by letter: " + str(word_split_list))

#using this you can split strings up by any character!

#-->TODO: Change the name of the person who is late in this sentence and print it.
split_me = "I heard Alex was late to class today."
split_me = split_me.split()
split_me[2] = "nappy"
print(split_me)
#-->TODO: Add an exclamation mark to this sentence using split() and append(), then print. (yes, there are other ways, but...)
make_me_exciting = "What a wonderful day"
make_me_exciting = make_me_exciting.split()
make_me_exciting.append("!")
print(make_me_exciting)

#We can also join our list elements into a string using.....join()!
rejoined = " ".join(boring_list)  #joins it using spaces
print('back in one piece: ' + rejoined)

#-->TODO:  Finally, put the split_me sentence today and the make_me_exciting strings back together and print. You should see a string
rejoined  = " ".join(split_me+make_me_exciting)
print('sentence:' + rejoined)


