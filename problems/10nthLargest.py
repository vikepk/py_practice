def nthLargest(max,n=[]):
    lt=n
    lt.sort(reverse=True)
    return lt[:max]    

# print(nthLargest(2,[2,3,4,5]))

# To find nth Largest Sort reverse and take the max no of element
# Using loop find the max element and delete the element


def nthLargeLoop(nthmax,n=[]):
    lt=n
    maxlt=[]
    for i in range(0,nthmax):
        maxlt.append(max(lt))
        lt.remove(max(lt))
    print(maxlt)
    return maxlt

# nthLargeLoop(2,[2,3,4,5])

def nthLowestProduct(nth,n=[]):
    n.sort()
    lowest=n[:nth]
    multiply=1
    for i in lowest:
        multiply*=i
    print(multiply)
    return(multiply)

nthLowestProduct(2,[4,2,3])