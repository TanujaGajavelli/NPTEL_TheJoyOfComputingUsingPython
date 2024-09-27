def linear_search(n,x):
    element=[]
    for i in range(1,n):
        element.append(i)
    flag=0
    count=0
    for i in element:
        count+=1
        if(i==x):
            print("Yes!!I found ",x," at position "+str(i))
            flag=1
            break
    if(flag==0):
        print(x," is not found!!")
    print("Number of iterations is ",count)
num=int(input("Enter the number to search:"))
ran=int(input("Enter the range:"))
linear_search(ran,num)