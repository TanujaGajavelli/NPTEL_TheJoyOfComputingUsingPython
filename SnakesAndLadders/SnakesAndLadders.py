from PIL import Image
import random
def show_board():
    img=Image.open('SnakesAndLadders.png')
    img.show()
def check_ladder(points):
    if(points==8):
        print("Ladder")
        return 26
    elif(points==21):
        print("Ladder")
        return 82
    elif(points==43):
        print("Ladder")
        return 77
    elif(points==50):
        print("Ladder")
        return 91
    elif(points==54):
        print("Ladder")
        return 93
    elif(points==62):
        print("Ladder")
        return 96
    elif(points==66):
        print("Ladder")
        return 87
    elif(points==80):
        print("Ladder")
        return 100
    else:
        return points
def check_snake(points):
    if (points == 44):
        print("Snake")
        return 22
    elif (points == 46):
        print("Snake")
        return 5
    elif (points == 48):
        print("Snake")
        return 9
    elif (points == 52):
        print("Snake")
        return 11
    elif (points == 55):
        print("Snake")
        return 7
    elif (points == 59):
        print("Snake")
        return 17
    elif (points == 64):
        print("Snake")
        return 36
    elif (points == 69):
        print("Snake")
        return 33
    elif (points == 73):
        print("Snake")
        return 1
    elif (points == 83):
        print("Snake")
        return 19
    elif (points == 92):
        print("Snake")
        return 51
    elif (points == 95):
        print("Snake")
        return 24
    elif (points == 98):
        print("Snake")
        return 28
    else:
        return points
def reached_end(points):
    if(points==end):
        return True
    else:
        return False
def play():
    p1_name=input("Player 1,Please enter your name:")
    p2_name=input("Player 2,Please enter your name:")
    pp1=0
    pp2=0
    turn=0
    while(1):
        if(turn%2==0):
            print(p1_name,"Your turn!")
            c=int(input("Press 1 to continue,0 to exit:"))
            if(c==0):
                print(p1_name,"Scored",pp1)
                print(p2_name,"Scored",pp2)
                print("Quitting the game,Thanks for playing")
                break
            else:
                dice=random.randint(1,6)
                print("Dice showed:",dice)
                pp1+=dice
                pp1=check_ladder(pp1)
                pp1=check_snake(pp1)
                if(pp1>end):
                    pp1=end
                print(p1_name,"Your score:",pp1)
                if(reached_end(pp1)):
                    print(p1_name,"won!!")
                    break
            turn+=1
        else:
            print(p2_name, "Your turn!")
            c = int(input("Press 1 to continue,0 to exit:"))
            if (c == 0):
                print(p1_name, "Scored", pp1)
                print(p2_name, "Scored", pp2)
                print("Quitting the game,Thanks for playing")
                break
            else:
                dice = random.randint(1, 6)
                print("Dice showed:", dice)
                pp2 += dice
                pp2 = check_ladder(pp2)
                pp2 = check_snake(pp2)
                if (pp2 > end):
                    pp2 = end
                print(p2_name, "Your score:", pp2)
                if (reached_end(pp2)):
                    print(p2_name, "won!!")
                    break
            turn+=1

end = 100
show_board()
play()