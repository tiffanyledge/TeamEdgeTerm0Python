import random

# -------------------------------------------- 

	# You've just learned about variables, conditionals.
	# Just from knowing those two topics, you can do so much!
	
	# Let's try to make a simple program that responds to the user.
	# We're going to recreate the Magic 8 Ball!!!
			
			# Never heard of it? That's ok!

					# You got this!

  # -------------------------------------------- 

	# How a Magic 8 Ball Works:

	# The user asks a question and vigoriously shakes the ball. 
	# Then the ball will respond with one of twenty responses, chosen at random. 

	# That's pretty simple right?

 # -------------------------------------------- 

	# Part 1: 
	# Print instructions on the screen and 
	# prompt the user to ask a question
print ("How a Magic 8 Ball works:")
print ("The user asks a question and vigoriously shakes the ball.")
print ("Then the ball will respond with one of twenty responses, chosen at random.")

generator = input ("Ask a question")
  # --------------------------------------------















# -------------------------------------------- 

	# Part 2: Next, we need to randomly select a response from 20 options.

	# Randomly select a number from 0 - 19 
	# Use that to select from the following responses:
		# 0 - It is certain.
		# 1 - It is decidedly so.
		# 2 - Without a doubt.
		# 3 - Yes - definitely.
		# 4 - You may rely on it.
		# 5 - As I see it, yes.
		# 6 - Most likely.
		# 7 - Outlook good.
		# 8 - Yes.
		# 9 - Signs point to yes.
		# 10 - Reply hazy, try again.
		# 11 - Ask again later.
		# 12 - Better not tell you now.
		# 13 - Cannot predict now.
		# 14 - Concentrate and ask again.
		# 15 - Don't count on it.
		# 16 - My reply is no.
		# 17 - My sources say no.
		# 18 - Outlook not so good.
		# 19 - Very doubtful.

	# Look up random.rand_int to see how you can use it to select a random number.

answers = (random.randrange(0, 20))
if answer == 0:
	print("it is certain")
elif answer == 1:
	print("it is decidedly so")
elif answer == 2:
	print("without a doubt")
elif answer == 3:
	print("yes-definitely")
elif answer == 4:
	print("you may rely on it")
elif answer == 5:
	print("as i see it, yes")
elif answer == 6:
	print("most likely")
elif answer == 7:
	print("outlook good")
elif answer == 8:
	print("yes")
elif answer == 9:
	print("signs point to yes")
elif answer == 10:
	print("reply hazy, try again")
elif answer == 11:
	print("ask again later")
elif answer == 12:
	print("better not to tell you now")
elif answer ==13:
	print("cannot predict now")
elif answer == 14:
	print("concentrate and ask again")
elif answer == 15:
	print("don't count on it")
elif answer == 16:
	print("my reply is no")
elif answer == 17:
	print("my source says no")
elif answer == 18:
	print("outlook not so good")
else:
	print("very doubtful")


  # -------------------------------------------- 




















# -------------------------------------------- 

	# Part 3: Customize it!

	# Select your own theme and use case and modify your code!
	
# -------------------------------------------- 

answers = (random.randrange(0, 20))
if answer == 0:
	print("your annoying")
elif answer == 1:
	print("please leave")
elif answer == 2:
	print("how would I know")
elif answer == 3:
	print("I don't care")
elif answer == 4:
	print("duh")
elif answer == 5:
	print("of course")
elif answer == 6:
	print("i guess so")
elif answer == 7:
	print("who knows")
elif answer == 8:
	print("sure")
elif answer == 9:
	print("if you think so")
elif answer == 10:
	print("try again")
elif answer == 11:
	print("stop asking questions")
elif answer == 12:
	print("better not to tell you now")
elif answer ==13:
	print("cannot predict now")
elif answer == 14:
	print("concentrate and ask again")
elif answer == 15:
	print("don't count on it")
elif answer == 16:
	print("my reply is no")
elif answer == 17:
	print("my source says no")
elif answer == 18:
	print("outlook not so good")
else:
	print("it doesn't look good")

























print ("How to find out what your horoscope says about you")
print ("type in your horoscope sign")
print ("the computer will generate a response based on your sign")

