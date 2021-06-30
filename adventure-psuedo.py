# Sandy Li, Kristy Le

# Theme: Getting the treasures
def start():
  print("\nYou have just entered the abandoned castle.")
  print("A dragon is chasing you.\nIn order to continue your journey, you must make a choice. What is your choice? (1 or 2)")
  print("1). Drink the chalice.")
  print("2). Turn around and attempt to slay the dragon!")
  
  # get user input using input() and save 
  answer = input(">")
  #print(answer)
  #print(type(answer))
  
  # use a loop to manage game -- 
  if answer == "1":
    castle_room()
  elif answer == "2":
    game_over("The dragon slain you. You are dead.")
  else:
    # else go to game over function
    game_over("Don't you know how to type something properly?")

def castle_room():
  # some prompts
  # '\n' is to print the line in a new line
  print("\nYou now have super strength.")
  print("You can fight either three dwarves or an ogre. Who do you want to fight? (1 or 2)")
  print("1). dwarves")
  print("2). ogre")

  castle_answer = input('>')
  #print(castle_answer)
  #print(type(castle_answer))

  if castle_answer == "1":
    print("You've made it to the throne room!")
    journey_home()
  elif castle_answer == "2":
    game_over("You were defeated")
  else:
    game_over("Don't you know how to type something properly?")

def journey_home():
  print("\nYou've made it to the end. Do you want to collect your treasures and head home?")
  print("1). Yes")
  print("2). No")

  home_answer = input('>')

  if home_answer == ("Yes"):
    game_over("You've returned home!")
  elif home_answer == ("No"):
    game_over("The dragon has woken and killed you.")
  else:
    game_over("Don't you know how to type something properly?")

# function to ask play again or not
def play_again():
  # use print statement to ask if user wants to play again
  print("\nDo you want to play again?")
  print("1). Y")
  print("1). N")
  # get input
  again_answer = input('>').upper()
  # evaluate input using conditional 
  if again_answer == "Y":
    return start()
  else: 
    exit()

# game_over function accepts an argument called "reason"
def game_over(reason):
  # print the "reason" in a new line (\n)
  print("\n" + reason)
  print("Game Over!")
  # STRETCH: maybe ask player to play again or not. 
  play_again()


# calling start function. 
start()
