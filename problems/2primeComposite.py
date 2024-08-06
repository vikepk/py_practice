import math as m

def isPrime(n):
    sqrtn=int(m.sqrt(n))
    isPrime=True
    #If a num is not divisible till its sqrt nums then it is Prime
    for divisor in range(2,sqrtn+1):
        if(n%divisor==0):
            isPrime=False
            break
    return isPrime    
    

def toCheckPrime():
    n=int(input("Enter the number to check wheater it is Prime or Composite : "))
    if n in [1,2]:
        print("1 and 2 are neither Prime nor Composite")
    elif(isPrime(n)):
        print(n,"is a Prime Number")
    else:
        print(n,"is a Composite Number")
    return

# toCheckPrime()
primeCount=0
compCount=0
for i in range(101,201):
    if(isPrime(i)):
        primeCount+=1
    else:
        compCount+=1
print("Prime Count : "+str(primeCount)+"\nComposite Count "+str(compCount))
    