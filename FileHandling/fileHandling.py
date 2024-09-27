import random
def evolve(x):
    ind=random.randint(0,len(x)-1)
    p=random.randint(1,100)
    if(p==1):
        if(x[ind]=='0'):
            x[ind]='1'
        else:
            x[ind]='0'
with open("dna_data.txt", "r+") as myfile:
    x=myfile.read()
    x=list(x)
for i in range(0,len(x)):
    evolve(x)
x = ''.join(x)
with open("dna_data.txt", "w") as myfile:
    myfile.write(x)
print(3//10)
