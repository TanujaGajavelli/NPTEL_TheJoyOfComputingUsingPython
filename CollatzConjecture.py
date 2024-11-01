def checkNum(num):
    iterations=1
    while(num!=1):
        if(num%2==0):
            num//=2
        else:
            num=3*num+1
        iterations+=1
    print(f"No of iterations:{iterations}")
num=int(input("Enter any number:"))
checkNum(num)