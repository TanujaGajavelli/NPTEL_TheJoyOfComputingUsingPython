def binary_search(l,x,start,end):
    if(start>end):
        return -1
    mid=(start+end)//2
    if(l[mid]==x):
        return mid
    elif(l[mid]>x):
        return binary_search(l,x,start,mid-1)
    else:
        return binary_search(l,x,mid+1,end)
l=[20,10,30,5,45]
x=int(input("Enter search key:"))
l.sort()
index=binary_search(l,x,0,len(l)-1)
if(index==-1):
    print(x,"not found!!")
else:
    print(x,"is found at position",index+1)