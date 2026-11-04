n=1345
temp=n
sum=0
while n>0:
    digit=n%10
    sum=sum+digit
    n=n//10
print(f"The sum of {temp} is {sum}.")