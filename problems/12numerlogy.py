def numerlogy(lt1=[],lt2=[]):
    z=zip(lt2,lt1)
    return [x for _,x in sorted(z)]


alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's','t','u', 'v', 'w', 'x', 'y', 'z']
# alphabets=['i','n','d','i','a']
numbers=[1, 2, 3, 4, 5, 8, 3, 5, 1, 1, 2, 3,4,5,7, 8, 1, 2, 3, 4, 6, 6, 6, 5, 1, 7]
# print(numerlogy(alphabets,numbers))


def numerlogy(lt1=[],lt2=[]):
    z=zip(lt2,lt1)
    return list(z)

numLt=numerlogy(alphabets,numbers)
inputVal=input("Enter the word to check numerlogy : ")
inputVal=list(inputVal.lower())
cnt=0
for i in inputVal:
    for x,a in numLt:
        if a==i:
            cnt=cnt+x


if cnt>9:
    n=len(str(cnt))
    strCount=0
    for i in str(cnt):
        strCount+=int(i)
    print(strCount)
else:
    print(strCount)
        
        
    