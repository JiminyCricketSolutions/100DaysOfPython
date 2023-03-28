# This program lets you play rock paper scisors with the computer via randomisation


from random import randint

imgs = [ 

'''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''', 

'''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''',

'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''',
'''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⣤⡶⠶⠟⠛⠛⠛⠋⠙⠛⠛⠿⢶⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣴⡾⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⣾⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣽⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⣿⠃⠀⠀⢰⡶⠾⠿⠿⠛⠛⠻⣿⠋⠀⠀⢸⡟⠉⠉⣭⣍⢹⡿⣷⡀⠀⠀⠀⠀⠀⠀⠀
⠀⣾⠃⠀⠀⠀⣿⡀⠀⠀⠰⠿⠆⣠⡿⠀⠀⠀⠈⢷⣤⣀⣼⡿⠟⠀⠹⣷⠀⠀⠀⠀⠀⠀⠀
⢸⡟⠀⠀⠀⠀⠘⠿⣶⣤⣤⣶⠾⠟⠁⠀⠀⠀⠀⠀⠈⠉⣁⣀⣀⠀⠀⢻⡇⠀⠀⠀⠀⠀⠀
⢸⡇⠀⠀⠀⠀⢀⣀⣠⣤⣤⣤⡶⠶⠶⠶⠶⠖⠛⠛⠛⠛⣿⠋⠉⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀
⣺⡇⠀⠀⠀⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡇⠀⠀⠀⣼⡇⠀⠀⠀⣤⡄⠀
⠸⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⠀⢠⡿⠁⠀⣠⣾⠏⠀⠀⠀⢀⣿⣇⠀
⠀⠹⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣦⠟⠁⣠⣾⠟⠁⠀⠀⠀⠀⣿⠉⣽⠂
⠀⠀⠈⠻⢷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠋⣹⣿⣴⡿⠋⠀⠀⢀⣠⣤⣶⣿⡽⠞⠁⠀
⠀⠀⠀⠀⠀⣸⡿⠻⠿⢶⣶⣶⣶⣶⣶⠶⣛⣷⡾⠛⠉⣿⣁⣠⠴⢞⣫⡵⠟⠋⠁⠀⠀⠀⠀
⠀⠀⠀⠀⣰⡟⠀⠀⢀⣤⡴⠟⣋⣥⡶⠚⠋⠁⠀⠀⠀⣿⣋⣤⠶⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢰⡿⠀⠀⠐⣋⣤⣶⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⣿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⣿⠃⠀⠀⠘⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⠀\n\n'''
]

print("This is rock paper scisors, enter 'rock', 'paper' or 'scisors'")
uchoiche = input("Choiche : ")



if uchoiche == "rock":
    uligma = 0
elif uchoiche == "paper":
    uligma = 1
elif uchoiche == "scisors":
    uligma = 2
else :
    uligma = 3

cpligma = randint(0, 2)

T = False
W = False
if uligma == 3:
    print("Git Gud, double check spelling next time...")
elif uligma == cpligma:
    T = True
elif uligma == 1 and cpligma == 0:
    W = True
elif uligma == 2 and cpligma == 1:
    W = True
elif uligma == 0 and cpligma == 2:
    W = True





print(imgs[uligma])
if uligma != 3:
    print("Bot chose: ")
    print(imgs[cpligma])
    if W:
        print("Congrats! You, a sentient being, beat an\n inanimate object at a randomisation game! WOW!")
    elif T:
        print("BOOF, A tie, but could be worse")
    else:
        print("You lost! Computers are now your overlord")

