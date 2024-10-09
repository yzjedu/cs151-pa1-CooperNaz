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
decision_1 = input("Do you (A) climb out of the cave, or (B) continue into the cave? ")

while decision_1.upper() != 'A' and decision_1.upper() != 'B':
    print("That is not a valid decision. Please input the letter of your decision.")
    decision_1 = input("Do you (A) climb out of the cave, or (B) continue into the cave? ")
if decision_1.upper() == 'A':
    print("You make it a few feet up the wall before your fingers slip on a smooth rock.")
    number = int(input("Pick a number from 1 to 10: "))
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
decision_illusion = input("Do you (A) follow the light, or (B) turn around? ")
while decision_illusion.upper() != 'A':
    print("The light calls to you.")
    decision_illusion = input("Do you (A) follow the light, or (B) turn around? ")

# Monster encounter
print("You follow the dim light. You can't seem to look away.")
print("As you get close to the light, your torch illuminates the source.")
print("You stub your toe on a rock and you snap back to reality.")
print("You stand face to face with a grey monster with pitch black eyes, large teeth, and a light hanging from its "
      "forehead.")
print("The sight reminds you of an anglerfish, but this creature is large and on land.")
print("The monster reaches a thin hand toward your face.")

# Set a value for attack power to be used in decision 2
attack_power = float(player_health / 8)

# Decision 2: Fight, defend, or freeze?
# If they choose to fight and their attack power is greater than or equal to 1, they injure the monster.
# If they choose to fight but their attack power is less than 1, they lose their torch and the game is over.
# If they choose to defend, they lose 4 health.
# If they choose to freeze, they lose 7 health.
# If at any point their health reaches 0, output "game over" and end the program.
decision_2 = input("Do you (A) fight, (B) defend, or (C) freeze? ")
while decision_2.upper() != 'A' and decision_2.upper() != 'B' and decision_2.upper() != 'C':
    print("That's not a valid decision. Please input the letter of your decision.")
    decision_2 = input("Do you (A) fight, (B) defend, or (C) freeze? ")
if decision_2.upper() == 'A':
    print("You step to the side and swing your torch at the monster, causing it to flinch back and raise its arms.")
    if attack_power >= 1:
        print("Your torch hits the monster's arm and burns its skin, causing it to screech and stumble backwards.")
    else:
        print("The monster swats the torch out of your hand, plunging the cave into darkness.")
        quit()
elif decision_2.upper() == 'B':
    print("You raise your arms as the monster swings its claws at you.")
    player_health = player_health - 4
    print("Your health is now", player_health)
    if player_health <= 0:
        quit()
else:
    print("You simply stare as the monster swings its claws at you.")
    player_health = player_health - 7
    print("Your health is now", player_health)
    if player_health <= 0:
        quit()

# More exposition; the user runs past the monster toward the sound of running water, and the monster chases them
print("Spotting an opening, you run past the monster, gripping your torch, your one lifeline.")
print("Hearing the sound of running water further into the cave, you run toward it.")
print("The monster screeches, and you hear the sound of rapid footsteps echoing behind you.")
print("You find an underground river to the side of your path. It could lead anywhere.")
print("The river is the only way forward, but you would have to abandon your torch.")

# Decision 3: Fight, run back the way they came, or jump in the river
# If they choose to fight and their attack power is greater than or equal to 1, they beat the monster and jump into the river.
# If they choose to fight and their attack power is less than 1, the monster attacks, and it's game over.
# If they choose to run back the way they came, the monster attacks them and it's game over.
# If they choose to jump into the river, they get swept away by the current, but it washes them up outside the cave, and they win.
decision_3 = input("Do you (A) stand your ground and fight, (B) run back the way you came, or (C) jump into the river? ")
while decision_3.upper() != 'A' and decision_3.upper() != 'B' and decision_3.upper() != 'C':
    print("That's not a valid decision. Please input the letter of your decision.")
    decision_3 = input("Do you (A) stand your ground and fight, (B) run back the way you came, or (C) jump into the river? ")
if decision_3.upper() == 'A':
    print("You turn to face your pursuer, gripping your torch. This is your final stand.")
    if attack_power >= 1:
        print("You land a clean hit on the monster's head with your torch.")
        print("The monster screeches as its skin burns, and it catches fire. It stumbles back, the inferno lighting "
              "up the cave.")
        print("Your torch goes out, and the monster stops struggling.")
        print("With no more light and no other option, you jump into the river.")
        print("The freezing cold water surrounds you in the darkness, and you are swept away with the current.")
        print("You struggle to hold your breath as you are slammed against rocks and walls.")
        print("Eventually, your vision is filled with blinding light, and you feel yourself falling.")
        print("You hit the surface of a lake. As you recover from the shock and look around, you realize you were sent "
              "off a short waterfall by the current.")
        print("The fresh air hits you at the same time as the realization that you're outside.")
        print("With a heavy sigh, you relax in the lake.")
        print("YOU ESCAPED!")
        print("CONGRATULATIONS!")
    else:
        print("You swing at the monster, but it ducks out of the way. Its claws scratch along your stomach, leaving a "
              "deep wound.")
        print("Your body feels cold, and your vision goes dark.")
        print("GAME OVER.")
elif decision_3.upper() == 'B':
    print("You turn on your heel and dash back the way you came, hoping to slip by the monster.")
    print("You are not so lucky.")
    print("The last thing you see is the monster's claws flashing toward your head.")
    print("GAME OVER.")
else:
    print("Seeing no other option, you abandon your torch and jump into the river.")
    print("The freezing cold water surrounds you in the darkness, and you are swept away with the current.")
    print("You struggle to hold your breath as you are slammed against rocks and walls.")
    print("Eventually, your vision is filled with blinding light, and you feel yourself falling.")
    print("You hit the surface of a lake. As you recover from the shock and look around, you realize you were sent off "
          "a short waterfall by the current.")
    print("The fresh air hits you at the same time as the realization that you're outside.")
    print("With a heavy sigh, you relax in the lake.")
    print("YOU ESCAPED!")
    print("CONGRATULATIONS!")