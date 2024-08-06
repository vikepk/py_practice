def nthFiboLoop(n):
    a=0
    b=1
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        fibo=[a,b]
        for i in range(2,n+1):
            c=a+b
            fibo.append(c)
            a=b
            b=c
        return fibo
    
def nthFiboRecursive(n):
    a=0
    b=1
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return nthFiboRecursive(n-1)+nthFiboRecursive(n-2)
n=int(input("Enter the nth term in Fibonacci : "))
l=nthFiboRecursive(n)
print(l)
# print(l[len(l)-1])
#Printing in 10 * 10
for i in range(10):
    for j in range(10):
        print(f"{l[i * 10 + j]:<6}", end=' ')
    print()
    