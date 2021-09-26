#Snake Water Gun GAME

import random
print("|= SNAKE WATER GUN =|")
print()
turns=int(input("How Many Turns You Like To Play: "))
print("Write:- \ns for Snake \nw for Water \ng for Gun")

def scoreboard():
    print("Scoreboard:")
    print("Your Score =", user_score)
    print("PC Score =", pc_score)

obj=["s","w","g"]
user_score=0
pc_score=0
i=0

while i<turns:
    i+=1

    pc= random.choice(obj)
    usr=str(input("Enter Your Choice: "))
    user= str.lower(usr)

    if user=="s" and pc=="s":
        print("\nDRAW, Both guesses SNAKE")
        scoreboard()
    elif user=="s" and pc =="w":
        print("\nYou Guess SNAKE, PC Guess WATER")
        user_score += 1
        scoreboard()
    elif user=="s" and pc=="g":
        print("\nYou Guess SNAKE, PC Guess GUN")
        pc_score += 1
        scoreboard()

    elif user=="w" and pc== "s":
        print("\nYou Guess WATER, PC Guess SNAKE")
        pc_score += 1
        scoreboard()
    elif user=="w" and pc== "w":
        print("\nDRAW, Both guesses WATER")
        scoreboard()
    elif user=="w" and pc== "g":
        print("\nYou Guess WATER, PC Guess GUN")
        user_score += 1
        scoreboard()

    elif user=="g" and pc== "s":
        print("\nYou Guess GUN, PC Guess SNAKE")
        user_score += 1
        scoreboard()
    elif user=="g" and pc== "w":
        print("\nYou Guess GUN, PC Guess WATER")
        pc_score += 1
        scoreboard()
    elif user=="g" and pc== "g":
        print("\nDRAW, Both guesses GUN")
        scoreboard()

    else:
        print("\nInvalid Letter Inputted.")

print("\nFINAL SCOREBOARD:")
print("Your Score:", user_score)
print("PC Score:", pc_score)

if user_score > pc_score:
    print("|| YOU WON THE MATCH ||")
elif user_score < pc_score:
    print("|| YOU LOST THE MATCH ||")
else:
    print("|| MATCH DRAW ||")

input("\nPress ENTER to Continue...")