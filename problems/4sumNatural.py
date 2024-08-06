def sumNaturalSquare(n):
    sum=0
    for i in range (1,n+1):
        sum=sum+i**2
    return sum



def sumCubeOddNatural(n):
    sum=0
    for i in range (1,n*2,2):
        sum=sum+i**3
    return sum






# print("Finding Sum of First n NaturalNumbers")
# print("=====================================")
# n=int(input("Enter the nth natural number : "))
# print(sumNatural(n))

print("Finding Sum of First n Cube Odd NaturalNumbers")
print("=====================================")
n=int(input("Enter the nth natural number : "))
print(sumCubeOddNatural(n))

    
        