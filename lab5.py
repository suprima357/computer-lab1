l=[]
n=int(input("enter total numbers: "))
for i in range(n):
    a=int(input("enter numbers: "))
    l.append(a)

small=l[0]
large=l[0]
for i in range(n):
    if(large<l[i]):
        large=l[i]
    if(small>l[i]):
        small=l[i]

print(f"largest number:{large}\nsmallest number:{small}")
        