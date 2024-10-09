# Code goes here
# Programmers:  Cooper Nazar
# Course:  CS151, Professor Yalew
# Due Date: 10/9/2024
# Programming Assignment:  PA 01
# Problem Statement: Create a text adventure game in which the user gives input that affects the story.
# Data In: Story based decisions (Move forward or climb out, etc.)
# Data Out: Player health, attack power, win or lose
# Credits: None

# Preamble
print("In this story, your actions have consequences.")
print("In reality, the consequences may not even depend on your actions.")
print("Make good decisions, or they may be your last.")

print("Your responses to decisions should be the given letters.")

# Prompt the user to enter their name
name = input("Enter your name: ")

# Set player health to 10
player_health = 10

# Story begin (context or whatever, I am trying to be dramatic)
print("You wake up to the feeling of hard ground beneath your head.")
print("That's not why you're surprised, that's practically the start of every Sunday morning for you.")
print("The main cause for concern is the dried blood next to your head.")
print("As you sit up, you realize that you're in a cave.")
print("You spot a lighter on the ground by your foot with the name", name, "written on it in black marker.")
print("As you pick up the cheap lighter, you spot an old torch on the ground against the wall.")
print("Your eyes are drawn to the sky. The morning light shines into the cave through the large hole you fell through.")
print("The cave isn't deep, but the walls are steep.")
print("Alternatively, there seems to be a narrow path leading deeper into the cave.")

# Decision 1: Climb out or continue into the cave?
decision_1 = input("Do you (A) climb out of the cave, or (B) continue into the cave?")

while decision_1.upper() != 'A' and decision_1.upper() != 'B':
    print("That is not a valid decision. Please input the letter of your decision.")
    decision_1 = input("Do you (A) climb out of the cave, or (B) continue into the cave?")
if decision_1.upper() == 'A':
    print("You make it a few feet up the wall before your fingers slip on a smooth rock.")
    number = input("Pick a number from 1 to 10: ")
    while number < 1 or number > 10:
        print("That's not a valid number.")
        number = input("Pick a number from 1 to 10: ")
    if number <= 3 or number >= 8:
        player_health = player_health - 3
        print("Your health is now", player_health)
    else:
        player_health = player_health - 1
        print("Your health is now", player_health)

# The user would continue down the path anyway, choosing A only opens them up to losing health

print("You pick up the lighter and the torch, and after fumbling to light the torch, you make your way deeper into "
      "the cave.")
print("As you continue into the cave, you hear the sound of running water growing louder.")
print("You see a dim light in the distance and a sound that seems to be a very steady gust of wind.")

# Prompt the user to continue forward. Make them choose to go forward, but there is no other option
decision_illusion = input("Do you (A) follow the light, or (B) turn around?")
while decision_illusion.upper() != 'Y':
    print("The light calls to you.")
    decision_illusion = input("Do you follow the light, or (B) turn around?")

# Monster encounter
print("You follow the dim light. You can't seem to look away.")
print("As you get close to the light, your torch illuminates the source.")
print("You stub your toe on a rock and you snap back to reality.")
print("You stand face to face with a grey monster with pitch black eyes, large teeth, and a light hanging from its "
      "forehead. The sight reminds you of an anglerfish, but this creature is large and on land.")
print("The monster reaches a thin hand toward your face.")

# Decision 2: Fight, flee, or freeze?