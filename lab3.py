n=int(input("Enter the number: "))

i=1
factorial=1
if(n<0):
    print("factorial dosen't exist.")
else:
    while i<=n:
        factorial *= i
        i +=1

print(f"factorial is {factorial}")
