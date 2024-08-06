def unCommon(str1="",str2=""):
    wordDic={}
    #Create a dict convert to List  
    for w in str1.split():
        wordDic[w]=wordDic.get(w,0)+1
    for w in str2.split():
        wordDic[w]=wordDic.get(w,0)+1
    
    print(wordDic)
    #  for w in wordDic:
    #     if wordDic.get(w)==1:
    #         print(w)
    for w,c in wordDic.items():
        if c==1:
            print(w)
    return

# unCommon("hello are you there","hello will you be there")


#Use Dict to count occurence of elements and based on value can get uncommon words or commom words



def matchingPercentage(str1='',str2=''):
    wordDic={}
    #Create a dict convert to List  
    for w in str1.split():
        wordDic[w]=wordDic.get(w,0)+1
    for w in str2.split():
        wordDic[w]=wordDic.get(w,0)+1
    
    print(wordDic)
    #  for w in wordDic:
    #     if wordDic.get(w)==1:
    #         print(w)
    cnt=0
    for w,c in wordDic.items():
        if c>1:
            cnt+=1
    # print(cnt)
    return (cnt/max(len(str1.split()),len(str2.split())))*100
        
print(matchingPercentage("Ramu is a very good boy","Somu is very good in cricket. He is tall."),"%")