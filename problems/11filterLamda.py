def isEven(n):
    return n%2==0

a=[1,2,3,4,5,6,7,8]
b=list(filter(isEven,a))
c=list(filter(lambda x:x%2==0,a))

c=list(filter(lambda x:x%2!=0,a))
print(c,len(c))

