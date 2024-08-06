def CountChar(strVal):
    countdic={}
    for i in strVal:
        if i in countdic:
            countdic[i]+=1
        else:
            countdic[i]=1
    return countdic
    
for item,count in CountChar("Hello").items():
    print(f"{item}:{count}")