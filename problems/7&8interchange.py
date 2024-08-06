
def interChangeLF(items=[]):
    n=len(items)
    tempF=items[0]
    items[0]=items[n-1]
    items[n-1]=tempF
    return items

# print(interChangeLF([1,2,3]))
# Interchange Last and First Element

#interChangeMiddle
def interChangeMiddle(items=[]):
    n=len(items)
    if n%2==1:
        return items
    else:
        mid=n//2
        tempR=items[mid]
        items[mid]=items[mid-1]
        items[mid-1]=tempR
        return items

# print(interChangeMiddle([1,2,3,4,5,6]))


#interChangeFirstSecPosition

def interChangeFirstSecPosition(fp,sp,items=[]):
    tempF=items[fp]
    items[fp]=items[sp]
    items[sp]=tempF
    print(items)
    return items

# interChangeFirstSecPosition(4-1,8-1,[1,2,3,4,5,6,7,8])


# interchange pairs

def interChangepair(items=[]):
    n=len(items)
    # if n%2==0:
    for i in range(0,n,2):
        if n-1==i:
            break
        temp=items[i]
        items[i]=items[i+1]
        items[i+1]=temp
    return items 
    # else:
    #     for i in range(0,n,2):
            # if n-1==i:
            #     break
    #         temp=items[i]
    #         items[i]=items[i+1]
    #         items[i+1]=temp
    #     return items  
        

print(interChangepair([1,2,3,4,5,6,7,8]))

    
    