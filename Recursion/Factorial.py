def factorial(n):
    # product=1
    # for i in range(1,n+1):
    #     product*=i
    # return product
    if(n==0):
        return 1
    else:
        return n*factorial(n-1)
n=int(input("Enter the number:"))
if(n<0):
    print("Factorial is not defined on negative numbers!!")
else:
    f=factorial(n)
    print("Factorial of",n,"is",f)