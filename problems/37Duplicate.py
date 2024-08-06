def Duplicate(n=[]):
    lst=[]
    duplicateLst=[]
    for i in range(0,len(n)):
        if n[i] not in lst:
            print(n[i])
            lst.append(n[i])
        else:
            duplicateLst.append(i)
    return (lst,duplicateLst)

print(Duplicate([1,1,2,1,2]))
        