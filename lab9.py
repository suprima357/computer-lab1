n=int(input("Enter a number: "))
temp=n
arm=0

while (n!=0):
    tmp=n%10
    arm= arm + tmp*tmp*tmp
    n=n//10
if(arm==temp):
    print("The given number is armstrong number")
else:
    print("the given number in not armstrong")    