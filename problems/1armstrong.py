def getDigit(n):
    l=0
    while n>0:
        l+=1
        n=n//10
    # print(l)
    return l

# q=qn=int(input("Enter the number to check Armstrong : "))

# n=len(str(q))
def checkArmstrong(q):
    qn=q
    n=getDigit(q)
    ans=0
    while qn>0:
        rem=qn%10
        ans=ans+rem**n
        qn=qn//10
    if q==ans:
        print(q,"is a Armstrong Number")
        return
    else:
        # print(q,"is not an Armstrong Number")
        return
for i in range(100,1000):
    checkArmstrong(i)
    
    

