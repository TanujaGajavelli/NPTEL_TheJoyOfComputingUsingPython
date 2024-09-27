# a = 10
# b = 20
# c = a+b
# print(c)
#
# x = int(input("Enter the cost:"))
# print("The amount to be aid after discount is:",int(x*0.9))
#
# if(x==100):
#     print("100")
# else:
#     print("Hii")
#
# for i in range(10):
#     print(i,"Hello World!!")
#
# print("Hello everyone,we are starting!!")
# n=1
# c=1
# while(c==1):
#     print("Token number",n,"may please come in")
#     c=int(input("Continue(0/1):"))
#     n+=1
# print("Thank you,this is the end of out day!!")

shopping = ["Bread", "Coffee", "Sugar"]
shopping.append("Milk")
for i in shopping:
    print(i)
shopping.insert(1,"Oil")
print(shopping)
print(shopping.count("Oil"),len(shopping))
print(shopping[1:3:1])
