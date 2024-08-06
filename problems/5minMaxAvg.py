a=[1,4,5,8,12.89,369.45]

print("Length of Array","%.2f" % len(a))

print("Sum of Array","%.2f" % sum(a))

print("Min of Array","%.2f" % min(a))

print("Max of Array","%.2f" % max(a))

print("Average of Array","%.4f" % (sum(a)/len(a)))

#To find 2 or n Largest Number

def nthLargestNumber(n, items=[]):
    print(items)
    lisArr=items
    for i in range(1,n):
        temp=max(lisArr)
        lisArr.remove(temp)
    print(lisArr)
    lisArr=items
    for i in range(1,n):
        temp=min(lisArr)
        lisArr.remove(temp)
    print(lisArr)
    return max(lisArr),min(lisArr)

print(nthLargestNumber(2,[1,2,4,5]))
        
