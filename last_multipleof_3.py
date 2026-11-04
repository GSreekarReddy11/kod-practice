n=9168
temp=n
sum=-1
found=False
while n>0:
    digit=n%10
    if digit!=0 and digit%3==0:
        sum=digit
        found=True
        break
    n=n//10
if found:
    print(f"The multiple of {temp} is {sum}.")
else:
    print("Not found")