def onlyEvendigit(n):
    isEven=True
    while n>0:
        if n%2!=0:
            isEven=False
            break
        n=n//10
    return isEven
                
# for x in range(1000,3001):
#     if(onlyEvendigit(x)):
#         print(x,end=",")
            
            
lst=[x for x in range(1000,3001) if(onlyEvendigit(x))]
print(lst,end=' ')