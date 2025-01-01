import random

def Roll():
    min_val=1
    max_val=6
    die=random.randint(min_val,max_val)
    return die

while True:                                                             
    no_of_player=input("/nEnter no.of player from 2-4 : ")
    if no_of_player.isdigit():
        no_of_player=int(no_of_player)
        if 2 <= no_of_player <= 4:            
            break
        else:
            print("enter no.of valid player")
    else:
        print("enter valid players")

max_score=50
player_scores=[0 for _ in range(no_of_player)]

while max(player_scores)<=max_score:
    
    for i in range(no_of_player):
        currentscore=0
        print(f"\n{i+1} player turn ")
        while True:
            y_n=str(input("would you like to roll (y/n) :"))
            if y_n.lower()!="y":
                break
            else:
                value = Roll()
                if value==1:
                    print(f"you rolled a {value} turn over")
                    currentscore=0
                    break
                else:
                    currentscore+=value
                    print(f"you rolled a {value}")
                    print(f"your current score is {currentscore}")
        print(f"your Score is {currentscore}")
        player_scores[i]+=currentscore
    
if player_scores[0]>player_scores[1]:
    print(f"player 1 won")
else:
    print("player 2 won")
