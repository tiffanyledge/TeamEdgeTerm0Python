# -------------------------------------------- 

	# You've just learned about variables, conditionals, functions, and user input. 
	# You've also created a basic calculator in a previous project.
	
	# Now imagine you are going out to eat.
	# Are you at a restaurant for a meal? Are you grabbing boba? Or are you just going to an ice cream parlor?
	# At the end of the meal, you get the bill. 

	# How do you think restaurants automate that math?

					# Let's try it!

# -------------------------------------------- 

# Scenario Parameters: 

	# When you eat out, you have the option to order one or multiple items.
	# What kind of items are available to order? There's usually a menu.
	# Allow your user to order a drink, meal, and dessert.

	# At the end of the order, the receipt comes and you have to calculate the total cost:
	# Don't forget the tax and tip!

# After this program finishes running, it should output a receipt with:
        #1. the items you ordered and their cost 
	#2. a total for your order before tax
	#3. a total for your order after tax
	#4. the amount of your tip 
	#5. the total including tax and tip

# -------------------------------------------- 

subtotal = 0
tip_fraction = 0
total = 0

# -------------------------------------------- 

# Part 1:
# Let's start by creating the variables we'll need to keep track of the user's order
# as well as TAX and tip

# Remember: Your user should be able to order at least 3 items (a drink, meal, and dessert item). 

# --------------------------------------------
Liquid1 = "Lemonade"
Liquid2 = "Iced Tea"
Solid1 = "Chicken Sandwich"
Solid2 = "Chicken Tenders"
Solid3 = "Chicken Salad"
Sweet1 = "Chip"
Sweet2 = "Gummy Bear"

# -------------------------------------------- 

# Part 2:
# Next, let's display the menu. Include the food item name and it's cost. 

# Write a function that will display the menu:
# - Print each item available and it's cost. You should have at least 3 items available (a drink, meal, and dessert item). 

# --------------------------------------------

print ("Menu")	

print ("Drinks:")
print ("1. Lemonade 		$3.00")
print ("2. Iced Tea		$2.75")
print ("Food:")
print ("3. Chicken Sandwich 	$7.75")
print ("4. Chicken Tenders	$5.00")
print ("5. Chicken Salad	$6.75")
print ("Snacks:")
print ("6. Chips		$1.00")
print("7. Gummy Bears		$2.00")


# -------------------------------------------- 

# Part 3:
# Let's take the order. What did the user order? What does it cost?

# Write a function that will take the order:
# - Prompt the user to enter a drink, dessert, and meal (Bonus: give them the option to not order an item)
# - Return the cost 

# Remember! Functions are meant to be reusable, so write a function that will work when called repeatedly!

# --------------------------------------------

drink=""
drink_cost=0
food=""
food_cost=0
sweet=""
sweet_cost=0

print ("Welcome to Foody Foodies!")
def get_drinks ():
	question = input("What drink would you like to order? (Enter 1 or 2)")
	global drink
	global drink_cost
	if  question == "1":
		drink = Liquid1
		drink_cost = 3.00
	elif question == "2":
		drink = Liquid2
		drink_cost = 2.75
def get_food ():
	question = input("What food would you like to order? (Enter 3,4 or 5)")
	global food
	global food_cost
	if question == "3":
		food = Solid1
		food_cost = 7.75
	elif question == "4":
		food = Solid2
		food_cost = 5.00
	elif Solid3 == "5":
		food = Solid3
		food_cost = 10.99
def get_snack ():
	question = input("What snack would you like? (Enter 6 or 7)")
	global sweet
	global sweet_cost
	if question == "6":
		sweet = Sweet1
		sweet_cost = 1.00
	elif question == "7":
		sweet = Sweet2
		sweet_cost = 2.00

	


get_drinks()
get_food()
get_snack()


price =  food_cost + drink_cost + sweet_cost

print (f"Your total is {price}")


# -------------------------------------------- 

# Part 4:
# Now that you have the costs of everything ordered, let's calculate the cost of the order(including tip and tax).

# Write a function that will calculate the cost of the order, including:
# - Cost of all  ordered items
# - Tax (Look up the sales tax of your city)
# - Tip (Give the user the option to enter how much they want to tip)

# Remember! Functions are meant to be reusable, so write a function that will work when called for each person!

# -------------------------------------------- 
# Total=Liquid1 + Liquid2 + Solid1 + Solid2 + Solid3 + Sweet1 + Sweet2 
# print (Total)


#Liquid1 = "$3.00"
#Liquid2 = "$2.75"
#Solid1 = "$7.75"
#Solid2 = "$5.00"
#Solid3 = "$10.99"
#Sweet1 = "$1.00"
#Sweet2 = "$2.00"



tax = 0.08875
tip = input ("What percent tip would you like to give? (15, 20, 25)")
def cost_order():
	global subtotal
	global tip_fraction
	global total
	extra_tax = (round(price*tax,2))
	subtotal = (round(extra_tax + price,2))
	tip_fraction = (round(int(tip)/100,2))
	total = (round((subtotal*tip_fraction) + subtotal, 2))
	print(total)

cost_order()




# -------------------------------------------- 

# Part 5:
# Let's print out a receipt.

# Write a function that will take the values of the order and total cost and print it out in an appealing way.

# The receipt should include:
# - Cost of each item
# - Tax for the order
# - Tip for the order
# - Total cost for the order


# -------------------------------------------- 
def food_choice():
	print (f"{drink} = {drink_cost}")
	
	print (f"{food} = {food_cost}")
	
	print (f"{sweet} = {sweet_cost}")




def receipt():
	print ("This is your receipt:")
	food_choice()
	print (f"Subtotal:{subtotal}")
	print (f"Tax:{tax}")
	print (f"Tip:{tip_fraction}")
	print (f"Total:{total}")
	print ("Bye!")
receipt()

# -------------------------------------------- 

# Part 6: Food Order Bot

# Call all of your functions to get your food order bot up and running!

# --------------------------------------------







# -------------------------------------------- 

# Part 7: Upchallenges!

# How many of these upchallenges can you implement?

# - Make sure the user is only entering valid values. If they enter an invalid value, prompt them to re-enter. 
# - The displayed prices should only have two decimal places.
# - Implement a rewards system (stamp cards, buy one get one, etc)

# --------------------------------------------
