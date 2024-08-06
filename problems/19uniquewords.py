def uniqueWords(n=""):
    lt=n.split()
    uniqueWordCount=[]
    result=[]
    for w in lt:
        if w not in result:
            result.append(w)
    for w in result:
        cnt=lt.count(w)
        uniqueWordCount.append(cnt)       
    print(result)
    print(uniqueWordCount)
    return result

uniqueWords("Hello there Hello dear dear there Three")

# Counting occurences in a list