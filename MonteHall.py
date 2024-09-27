import random
swap=0  #wins in swapping
dont_swap=0  #wins in not swapping
play=True
while(play):
    doors = [0] * 3
    goatdoor = [0] * 2  # doors having goat
    x=random.randint(0,2)
    doors[x]="BMW"
    for i in range(0,3):
        if(i==x):
            continue
        else:
            doors[i]="Goat"
            goatdoor.append(i)
    choice=int(input("Enter your choice:"))
    door_open=random.choice(goatdoor)
    while(door_open==choice):
        door_open = random.choice(goatdoor)
    print("The door having goat is:",door_open)
    ch=input("Do you want to swap?(Y/n):")
    if(ch=='Y'):
        if(doors[choice]=='Goat'):
            print("You won!!")
            swap+=1
        else:
            print("You lost!!")
    elif(ch=='n'):
        if (doors[choice] == 'Goat'):
            print("You lost!!")
        else:
            print("You won!!")
            dont_swap+=1
    print("The no of wins when swapped:",swap)
    print("The no of wins when not swapped:",dont_swap)
    cond=input("Do you want to continue(Y/n):")
    if(cond=='Y'):
        continue
    else:
        play=False
