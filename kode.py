n=int(input("enter the num:"))
for i in range(1,n):
    if n%i==0:
        print("Prime")
        break
    else:
        print("Not Prime") 
