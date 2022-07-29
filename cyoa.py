
game_play = True
current_room=" "
active = True

class Characters:
    def __init__(self, name, job, inventory):
        self.name = name
        self.job = job
        self.inventory = inventory

Detective1 = Characters("Joseph", "Detective", [])
Player = Characters("", "Player", [])


class Rooms: 
    def __init__(self, name, description, items, choice):
        self.name = name
        self.description = description
        self.items = items
        self.choice = choice

    
Outside = Rooms("Outside", "You are currently outside of the house 🏠.", [], ["hall"])

Hall = Rooms("Hallway", "Welcome. This is the grand entrance. A crime scene investagator will inform you on the current situation. \nInvestagator 👮: Hello, Ms. Donatella was found stabbed multiple times in the living room and Ms. Louella was found shot in the thigh and head with a gun in their bedroom. There's defense wounds on Ms. Donatella but not on Ms. Louella. There are no signs of an invasion and it seems that the suspect either..... The only people who had the key to this house was the other than the parents was the nanny and cleaner. The suspect used items in this house to kill as many of the items are missing. We're currently tracking down the nanny as she hasn't been active since the day of the murder. " , [], ["living room", "stairs"])

Living_Room = Rooms("Living Room", "This is the living room, Ms. Donatella was found here 🛋️ . She was discovered here by her mother around noon. She was found in the lying on the floor stabbed in the abdomen and the stomach. Defense wounds were found on her arms and hands. It seems that multiple items had been used to attack Ms. Donatella and There's a big spot of blood that has been soaked into the white rug. It seems as though the suspect used tools from this house to attack. There were more than 1 object that Ms. Donatella was stabbed with. It seems like something wooden... The tv was left on and nothing was touched in this room. ", [], ["kitchen", "basement", "hall"])

Kitchen = Rooms("Kitchen", "This is one huge kitchen ⏲️ . There is one knife missing from the knife block. Some of the drawers in the counters were drawn open. Drawers even has their handle pulled off... Inside the drawers, it is a mess. Everything inside was mixed together, like someone frantically trying to find something from there. What was so important in here? One of the island stools have their legs broken apart and soaked in blood. The sink is full of dirty dishes, assumming that they hadn't done the dishes in a while. Guess someone just snapped", [], ["bathroom", "living Room"])

Bathroom = Rooms("Bathroom", "So it seems that the bathroom is the cleanest place in the house 🚻. The cleaner must have cleaned this room recently. It still smells like chlorine and freshness. Oh look, there's a rag on the floor. They must have forgotten to take it away. Wait.. why is there blood on it? It looks like a really old rag with lots of rips and tears on it. Someone must have been in a rush to get out and forgot about the rag. Who would have forgotten this?", [], ["kitchen"])

Stairs = Rooms("Stairs", "These are some small and narrow stairs for a house like this. Everything in this house has been renovated except the stairs. The stairs are like those in a haunted house. As you walk, they creek more and more. The second floor is probably worst than this...", [], ["second floor hall", "hall"])

Second_Floor_Hall = Rooms("Second floor hall", "The hallway here is a lot bigger than a thought. It could possibly be a second living room. It's so quiet in this room it's unsettling. All of the photos that was once hung on the wall had been destroyed. ", [], ["master bedroom", "bedroom", "stairs"])

Master_Bedroom = Rooms("Master Bedroom", "This is the master bedroom 🛏️ . The bed is nicely made and the curtains are open to let in the light. There's a nice suit laided out on the bed but it looks like it's been there for a while.. A small layer of dust lays on top of the suit as it waits to be worn. It looks like nothing much has happened here.", ["Keys"], ["second floor hall"] )

Bedroom = Rooms("Kids bedroom", "This is where Ms. Louella was found. She was found sitting on the side shot with a gun. There were gun shot wounds to the head and thigh. The suspect must have shot her in the thigh in order to stop her from running away. There is a pool of blood sitting right next to her. Her dress is soaked in the blood and teared apart. What kind of cleaner is this? Forgetting to take away the cleaning supplies.. 🤦",[],["second floor hall"])

Basement = Rooms("Secret basement", "This is the hidden room 🙊. All the clues that you'll ever need is in here. A secret room with secret things. It's quite dim in here. There's a cork board with pins and pictures of the family. The photos of Donatella and Louella both circled in red. Looks like whoever has been here, has been here for a while. There's scraps on the floor, trash everywhere. In the very corner of the room, it looks like there's a bed. There's shelfs on the wall with cleaning supplies lined up on it. Boxes stacked together with black lines scribbled on the box. Oh look, there's a letter.", [], ["living room"])


# def helping_center(user_input):
#     global active
#     if user_input == "End" or user_input == "end":
#         active = False
#         # exit()    

def start_game():
    print("Welcome to Zed 🔪 ")
    print("In this game, you will be playing the role of a detective who is investagating the murders of Dontella Huxley and Louella Huxley.") 
    # print(instruction_message)
    print("In order to win the game, you must find out who is the murder. You'll get 2 chances to guess who the murder is. If you run out of the 2 chances, you lose.")
    # print(How_to_win)
    # print("If you would like to end the game, type 'end'.")



def intro():    
    global current_room
    global active
    answer = input("Are you ready to play? ")
    Player = Characters("", "Player",[])

    if answer == "yes" or answer == "Yes":
        Player.name = input("Okay! What is your name? ") 
        print(f"Welcome detective {Player.name}.")
        current_room = Outside
        print(current_room.description)
        print("Here is the room you can enter from here:")
        print(current_room.choice)
    elif answer == "no" or answer == "No":
        print("Okay! Bye!")
        active = False
    else: 
        print("You cannot enter this room from here.")



# def inventory(player_item):
#     global current_room
#     if player_item in current_room.items:
#         player_inventory.append(player_item)
#     print("You have added {player_inventory} into your inventory.")

# def prompt_user():
#     reply = input("Where would you like to go? ")
#     return reply


    
def check_answer():
    global current_room
    global active
    User_input = input("Where would you like to go? ")
    if ((User_input == "Hall" or User_input == "hall") and (current_room == Outside or current_room == Stairs or current_room == Living_Room)):
        current_room = Hall
        print(current_room.description)
        print("Here, this is the suspect list we have compiled.")
        print("You can always come back to the hall to view the suspect list. If you could not like to, hit the 'enter' key to ignore.")
        
        answer = input("Type 'Open' to open the paper: ")
        if answer == "open" or answer == "Open":
            print("Suspect List:\n -Dad \n -Mom \n -Nanny \n -Cleaner")
            
        print("Here are the rooms you can enter from here:")
        print(current_room.choice)
    elif ((User_input == "Living room" or User_input == "living room") and (current_room == Hall or current_room == Kitchen or current_room == Basement)):
        current_room = Living_Room
        print(current_room.description)
        print("Here are the rooms you can enter from here:")
        print(current_room.choice)
    elif ((User_input == "Stairs" or User_input == "stairs") and (current_room == Hall or current_room == Second_Floor_Hall)):
        current_room = Stairs
        print(current_room.description)
        print(current_room.choice)
    elif ((User_input == "Second floor hall" or User_input == "second floor hall") and (current_room == Stairs or current_room == Master_Bedroom or current_room == Bedroom)):
        current_room = Second_Floor_Hall
        print(current_room.description)
        print("Here are the rooms you can enter from here:")
        print(current_room.choice)
    elif ((User_input == "Kitchen" or User_input == "kitchen") and (current_room == Living_Room or current_room == Bathroom)):
        current_room = Kitchen
        print(current_room.description)
        print("Here are the rooms you can enter from here:")
        print(current_room.choice)
    elif ((User_input == "bathroom" or User_input == "Bathroom") and (current_room == Kitchen)):
        current_room = Bathroom
        print(current_room.description)
        print("Here are the rooms you can enter from here:")
        print(current_room.choice)
    elif ((User_input == "Basement" or User_input == "basement") and (current_room == Living_Room)):
        current_room = Basement
        if "Keys" in Player.inventory:
            print("The door is open... enter at your own risk..")
            print(current_room.description)
            print("He has been spending too much time with daughters. Does he even care about me? It's time to show him... 🗒️")
            print("Who's him?")
            question()
            # active = False
        else:
            print("This door is locked.. Find the key to unlock this. 🔑")
            print("Here are the rooms you can enter from here:")      
            print(current_room.choice)
    elif ((User_input == "Master bedroom" or User_input == "master bedroom") and (current_room == Second_Floor_Hall)):
        current_room = Master_Bedroom
        print(current_room.description)
        print("You see..")
        print(current_room.items)
        answer = input("Would you like to take the key? (Yes or no) ")
        if answer == "yes" or answer == "Yes":
            Removed_items = current_room.items.pop()
            Player.inventory.append(Removed_items)
            print(f"You have added {Player.inventory} into your inventory.")
        print("Here are the rooms you can enter from here:")
        print(current_room.choice)
    elif ((User_input == "Bedroom" or User_input == "bedroom") and (current_room == Second_Floor_Hall)):
        current_room = Bedroom
        print(current_room.description)
        print("Here are the rooms you can enter from here:")
        print(current_room.choice)
    else: 
        print("You cannot enter this room from here.")

def question():
    global active
    answer = input("Would you like to guess who the murder is? (yes or no)")
    if answer == "yes" or answer == "Yes":
        print("Suspect List:\n -Dad \n -Mom \n -Nanny \n -Cleaner")   
        guesses = 0
        while guesses <= 1:
            answer = input("Who do you think the murder is? ")
            if answer == "Mom" or answer == "mom":
                print("Good job! 🥳🥳🥳 You found out who the murder is! Hope you enjoyed!")
                exit()           
            else:
                print("Sorry that's not the murder 👻👻")
                if guesses == 1:
                    print("Damn. You lost. 👎👎 Sucks for you.. Just kidding! Anyways, nice try! Hope you enjoyed. :)")
                    active = False
            guesses += 1 
    else: 
        print("Okay! Here are the rooms you can enter from here.")      
        print(current_room.choice)

def end_game():
    global active
    active = False

def play_game():
    start_game()
    intro()
    while active:
        check_answer()

# question()
play_game()
    




#to do: "mom" and descriptions
    
    # answer = input("Would you like to guess who the murder is?")
    # if answer == "yes" or "Yes":
    #     player_input = input("Okay! Who do you believe is the murder?")
    #     if player_input == "Dad" or player_input == "dad":
    #         print("Sorry, that's incorrect. 2 more tries left! :)")
    #     elif player_input == "Nanny" or "nanny":
    #         print("Sorry, that ")
