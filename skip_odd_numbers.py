n=23461155
temp=n
even=[]
while n>0:
    digit=n%10
    if digit%2==0:
        even.append(digit)
    n=n//10
if len(even)>0:
    even.reverse()
    print(f"The even digits in {temp} are", *even)
else:
    print("No even digit in {temp}")