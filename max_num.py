n=4185
max=0
while n>0:
    digit=n%10
    if digit>max:
        max=digit
    n=n//10
print(max)