n=[]

for i in range(10):
    a=int(input("Enter numbers: "))
    n.append(a)
zero=0
positive=0
negative=0
for i in range(10):
    if(n[i]==0):
        zero +=1
    elif (n[i]>0):
        positive += 1
    else:
        negative += 1

print(f"The numbers of zero ={zero}, positive number ={positive} and negative is {negative}")