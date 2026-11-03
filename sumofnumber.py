n=12
while n>=10:
  s=0
  while n>0:
    d=n%10
    s=s+d
    n=n//10

  n=s
print(n)

#  OR 
# n=1211
# if n==0:  
#    print(0)
# a=1+(n-1)%9
# print(a)