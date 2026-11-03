n=19
number=set()
while n!=1 and n not in number:
    number.add(n)
    total=0
    while n>0:
        digit=n%10
        total+=digit**2
        n=n//10
    n=total
if n==1:
    print("Happy Number")
else:
    print("Not Happy Number")
    
