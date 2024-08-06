def Encrypt(key,s=""):
    lAlpha='abcdefghijklmnopqrstuvwxyz'
    uAplha=lAlpha.upper()
    res=''
    for i in s:
        if i.islower():
            pos=(ord(i)-ord('a')+key)%26
            #because of the string "a-z" ord('a') is substracted and key added
            res=res+lAlpha[pos]
        elif i.isupper():
            pos=(ord(i)-ord('A')+key)%26
            res=res+uAplha[pos]
        else:
            res=res+i
    print(res)
    return


# Add a list of Upper and Lower alphabets
# according to Lower and Upper pos is found with keys and %26 and added back to result
Encrypt(int(input("Enter Key for Encryption : ")),input("Enter input to Encrypt : "))
            
            