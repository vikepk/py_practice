def CommonElements(x=[],y=[]):
    z=[]
    for i in x:
        if i in y:
            z.append(i)
    return z

print(CommonElements([1,2,3],[1,4,5,3]))