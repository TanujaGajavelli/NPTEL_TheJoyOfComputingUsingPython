def rock_paper_scissors(num1,num2,bit1,bit2):
    p1=int(num1[bit1])%3
    p2=int(num2[bit2])%3
    print("Player one:",player_one[p1])
    print("Player two:",player_two[p2])
    if(player_one[p1]==player_two[p2]):
        print("Draw")
    elif(player_one[p1]=="Rock" and player_two[p2]=="Scissor"):
        print("Player one won!!")
    elif (player_one[p1] == "Rock" and player_two[p2] == "Paper"):
        print("Player two won!!")
    elif (player_one[p1] == "Paper" and player_two[p2] == "Scissor"):
        print("Player two won!!")
    elif (player_one[p1] == "Paper" and player_two[p2] == "Rock"):
        print("Player one won!!")
    elif (player_one[p1] == "Scissor" and player_two[p2] == "Rock"):
        print("Player two won!!")
    elif (player_one[p1] == "Scissor" and player_two[p2] == "Paper"):
        print("Player one won!!")


player_one={0:'Rock',1:'Paper',2:'Scissor'}
player_two={0:'Paper',1:'Scissor',2:'Rock'}
while(1):
    num1=input("Player 1,enter your choice:")
    num2=input("Player 2,enter your choice:")
    bit1=int(input("Player 1,enter the secret bit position:"))
    bit2=int(input("Player 2,enter the secret bit position:"))
    rock_paper_scissors(num1,num2, bit1, bit2)
    ch=input("Do you want to continue?(Y/n)")
    if(ch=='n'):
        break