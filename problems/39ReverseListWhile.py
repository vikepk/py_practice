def ReverseList(n=[]):
    end_index=len(n)-1
    start_index=0
    while start_index<end_index:
        n[start_index],n[end_index]=n[end_index],n[start_index]
        start_index+=1
        end_index-=1
    return n

print(ReverseList([5,4,3,2,1,0]))
print([5,4,3,2,1,0][::-1])