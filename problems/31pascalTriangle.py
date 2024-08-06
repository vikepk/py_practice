def PascalTriangle(n):
    res=[]
    for i in range(1,n+1):
        rowValues=[]
        # i represent no of rows 
        for j in range(1,i+1):
        # j represent the row elements 
            if j==1 or i==j :
                element=1
            else:
                curRow=i-1
                prevRow=curRow-1
                curPos=j-1
                element=res[prevRow][curPos-1]+res[prevRow][curPos]
                # element=0
            rowValues.append(element)
        res.append(rowValues)
    return res
    
def DrawPascalTriangle():
    n=int(input("Enter the length of Pascal Triange : "))
    res=PascalTriangle(n)
    spr=n-1
    for lst in res:
        print("   "*spr,end='')
        for n in lst:
            print("{0:^6d}".format(n),end='')
        print()
        spr-=1



DrawPascalTriangle()        
        
                