def SeparateString(strVal):
    for i in range(0,len(strVal)):
        for j in range(0,i+1):
            print(strVal[j],end='')
        print()
    # if len(strVal)>0:
    #     SeparateString(strVal.replace(strVal[0],"")) Using Recursive
    

#Using While Loop
strVal="RAMU"
while strVal:
    SeparateString(strVal)
    strVal=strVal[1:]
        