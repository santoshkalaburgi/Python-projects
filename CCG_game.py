import random

user_choice=0
compu_choice=0

while True:
    print("Welcome to colour choice game"+"\n Rules are as follows:"+"\n In order to win your choice should match with computer"+"\n All the best!")
    print("red=1"+"\nblue=2"+"\ngrey=3"+"\norange=4"+"\ngreen=5")
    user_inp=int(input("Your Turn: "))
    while user_inp>5 and user_inp<1:
        user_inp=int(input("Enter a valid option: "))
    if user_inp==1:
        user_colour="Red"
    elif user_inp==2:
        user_colour="Blue"
    elif user_inp==3:
        user_colour="Grey"
    elif user_inp==4:
        user_colour="Orange"
    else:
        user_colour="Green"

    print(f"Your choice is {user_colour}")
    print("Now it's computers turn")

    compu_inp=random.randint(1,5)

    if compu_inp==1:
        compu_colo="Red"
    elif compu_inp==2:
        compu_colo="Blue"
    elif compu_inp==3:
        compu_colo="Grey"
    elif compu_inp==4:
        compu_colo="Orange"
    else:
        compu_colo="Green"

    print(f"Computer choice is {compu_colo}")

    if user_inp==compu_inp:
        user_choice+=1
        print(f"Player score is {user_choice}")
    else:
        compu_choice+=1
        print(f"computer score is {compu_choice}")
    print("Do you want to play again(Y/N)")
    user=input()
    if user=="N" or user=="n":
        break

print("Time to know results!")
if user_choice==compu_choice:
    print("Game is tied!")
    print(f"Your score {user_choice} and computer score {compu_choice}")
elif user_choice<compu_choice:
    print("You loose")
    print(f"Your score {user_choice} and computer score {compu_choice}")
else:
    print("Congo You won!")
    print(f"Your score {user_choice} and computer score {compu_choice}")



