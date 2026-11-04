n=1279
temp=n
sum=-1
while n>0:
    digit=n%10
    if digit%2==0:
        sum=digit
        break
    n=n//10
if sum==-1:
    print("No even number")
else:
    print(sum)