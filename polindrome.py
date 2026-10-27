n="racecar"
l=0
r=len(n)-1
p=True
while l<r:
    if n[l]==n[r]:
        print("Polindrome")
        break
    else:
        p=False    
