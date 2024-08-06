def revWords(n=''):
    return ' '.join(list(reversed(n.split(" "))))
    # return ' '.join(list(n.split(" ")[-1::-1]))

# print(revWords(input("Enter the string to reverse word : ")))



def reverseWordsAndLetter(n=''):
    strS=n.split(' ')
    strS=strS[-1::-1]
    res=[]
    for i in strS:
        i=i[len(i)-1]+i[1:-1]+i[0]
        #India =>aidnI
        # String Immutable so Concat
        res.append(i)
    print(res)

reverseWordsAndLetter("India is my country")