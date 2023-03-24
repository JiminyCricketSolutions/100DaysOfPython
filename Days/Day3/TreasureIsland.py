# this is a basic text game

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
alive = True

choiche = input("The trail you are following splits, do you go left or right? : ")
print("\n")
if choiche == "left":
    print("Congratulations you narrowly escaped death.")
elif choiche == "right":
    print("You passed through a portal, and teleported into the future!\nUnfortunately you landed on a road and were turned\ninto a bloody mess by a semi truck.")
    alive = False
else :
    print("You died to a spelling error! How emberassing 😂")
    alive = False

if alive:
    choiche = input("You have reached the shore of gathsemete, the island of fabled treasure is within sight\n Will you swim or wait for a boat? (swim or wait): ")
    print("\n")
    if choiche == "swim":
        print("you were so focused on the treasure, you forgot about fourier transforms,\n and clearly whoever designed the view from the shore, didn't\nits much further away than you anticipated,\nand can no longer fight off the eels")
        alive = False
    elif choiche == "wait":
        print("A fae ferry arrives, and you get onboard. \nYou quickly realize the island was not as close as you thought.\nyou think to yourself, 'whoever designed that view, must have known about fourier transforms'")
    else :
        print("The server admin has decided your spelling skills suck, \nand has kicked you from the server we call life.")
        alive = False



if alive:
    print("Finally, after your long, treacherous journey, you have arrived.")
    print("There are three doors, you must choose one to travel through.\nOne Red, so red, it looks like it was made from the blood of those who can not spell\n one blue, so blue, the spirits of those who forgot about fourier transforms must be possessing it\n and one yellow, so yellow, the gods themselves must have pissed on it.")
    choiche = input("What door will you enter? (red, blue, yellow) : ")
    print("\n")
    if choiche == "red":
        print("You pass through the door and find a room filled with honey, tis not the treasure you expected.")
        print("You turn to walk out, but a bear with a top hat enters the door behind you.")
        print("The bear suspects you of coming after their honey!\nThe bear whips out a P32 Space modulator and turns you into mist.")
        print('''
                 ^
         | |
       @#####@
     (###   ###)-.
   .(###     ###) \ 
  /  (###   ###)   )
 (=-  .@#####@|_--"
 /\    \_|l|_/ (\ 
(=-\     |l|    /
 \  \.___|l|___/            The bear says, Sionara.
 /\      |_|   /
(=-\._________/\ 
 \             /
   \._________/
     #  ----  #
     #   __   #
     \########/
        ''')
        alive = False
    elif choiche == "blue":
        print("Behind this door, you find a wealth of sapphire, all too big to carry.\nYou hear voices whispering about differential equations, but see no other living creatures")
        print("After a moment of pondering, the dead recruit you to their \nranks by dropping a sapphire boulder from the ceiling.")
        print("Your fate is to teach the dead about fourier transforms for all eternity.")
        alive = False
    elif choiche == "yellow":
        print("On opening the yellow door, you realize it was ichor, not piss.\n What a pleasant suprise!")
    else:
        print("Your atrocious spelling has angered the gods! \nYou are swarmed by Murderous Giant Spelling Bees!")
        print("Due to the bee's angle of attack, all your blood splatters on the red door")
        alive = False


if alive:
    print("Congratulations, You have found the treasure!\n You should consider dying so you get the full experience.")
    print("There are more ways to die than making a bad decision.")
else:
    print("Game Over. F in the chat for ma pal\nF\n")