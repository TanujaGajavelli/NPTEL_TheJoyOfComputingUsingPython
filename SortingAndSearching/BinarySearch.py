def binary_search(ran,x):
    a = []
    for i in range(1, ran):
        a.append(i)
    first_pos=0
    last_pos=len(a)-1
    flag=0
    count=0
    while(first_pos<=last_pos and flag==0):
        count+=1
        mid=(first_pos+last_pos)//2
        if(x==a[mid]):
            flag=1
            print("The element ",x," is at pos:",mid)
            print("The number of iterations are:",count)
            return
        elif(x<=a[mid]):
            last_pos=mid-1
        else:
            first_pos=mid+1
    print("The number is not found!!")
num=int(input("Enter the number to search:"))
ran=int(input("Enter the range:"))
binary_search(ran,num)
