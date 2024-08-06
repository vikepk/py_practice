def nthGreaterWord(nth,strN=""):
    return [x for x in strN.split() if len(x)>nth]


# print(nthGreaterWord(3,"Ramu is Good"))


def nthGreaterMerge(nth,strN=""):
    res=[x for x in strN.split() if len(x)>nth]
    res=res[:2]
    result=''
    #Alternative the first 2 string 
    for i in range(max(len(res[0]),len(res[1]))):
        if i<len(res[0]):
            result+=res[0][i]
        if i<len(res[1]):
            result+=res[1][i]
    print(result)
            
        
        
        
nthGreaterMerge(1,"Ramu is Handsome")
#Sorting and Merging alternative
        
    