n=int(input("Enter the number: "))
i=0
tmp=n
rev=0
int(rev)
int(i)
while (n!=0):
    i= n%10
    rev= rev*10+i
    n= n//10

if(rev== tmp):
    print(f"{tmp} is palindrome number")
else:
    print(f"{tmp} is not palindrome")
