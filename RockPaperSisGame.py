import random

user_wins=0
computer_wins=0
options=["rock","paper","sis"]

while True:
    user_input=input("Pick rock/paper/sis or q  :").lower()
    
    if user_input=="q":
        break

    if user_input not in options:
        continue

    random_num= random.randint(0,2)
    
    computer_pick=options[random_num]
    print(computer_pick)
    if user_input==computer_pick:
        print("draw")
        continue
    elif user_input=="rock" and computer_pick=="paper":
        print("com won")
        computer_wins+=1
    elif user_input=="paper" and computer_pick=="sis":
        print("com won")
        computer_wins+=1
    elif user_input=="sis" and computer_pick=="rock":
        print("com won")
        computer_wins+=1
    else:
        print("you won")
        user_wins+=1

if user_wins>computer_wins:
    print(f"user won {user_wins} times over computer {computer_wins}")
elif user_wins==computer_wins:
    print("draw")
else:
    print(f"computer won {computer_wins} times over user {user_wins}")
    

