import math
def magic_square(n):
    magicSquare = [[0 for i in range(n)] for j in range(n)]
    i = n//2
    j=n-1
    num=n*n
    count=1
    while(count<=num):
        if(i==-1 and j==n):
            j=n-2
            i=0
        else:
            if(j==n):
                j=0
            if(i<0):
                i=n-1
        if(magicSquare[i][j]!=0):
            j-=2
            i+=1
            continue
        else:
            magicSquare[i][j]=count
            count+=1
        i=i-1
        j=j+1
    for i in range(n):
        for j in range(n):
            print(magicSquare[i][j],end=" ")
        print("")
    print("The sum of each row and column is ",int(n*(n**2+1)/2))

try:
    n2=int(input("Enter the highest number in the magic square:"))
    n=math.sqrt(n2)
    if(n!=int(n)):
        print("Not a perfect square!!")
    else:
        if(n%2!=0 and n!=2):
            print("The magic square is:")
            magic_square(int(n))
        else:
            print("Magic square is not possible for ",n2,"!!")
except Exception as e:
    print(e)
