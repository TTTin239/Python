from random import randint
print("Nhap lua chon cua ban: Bua, Keo, Bao?") 
player = input("Lua chon cua ban: ")
computer = randint(0,2)
if computer == 0:
    computer = "Keo"

if computer == 1:
    computer = "Bua"

if computer == 2:
    computer = "Bao"

print("-----------")
print("Player choose: " +player)
print("Computer chooses:"+computer )
print("------------")

if player == computer:
    print("Draw")
else:
    if player == "Keo":
        if computer == "Bao":
            print("You win!")    
        
        else:
            print("You lose!")
    elif player == "Bua":
        if computer == "Bao":
            print("You lose!")
        else:
            print("You win!")
    elif player == "Bao":
        if computer == "Keo":
            print("You lose!")
        else:
            print("You win!")
    else:
        print("Nhap sai!")                    
            