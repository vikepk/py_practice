def Vowels(n=""):
    vowels=['a','e','i','o','u']
    vowelscount=0
    for i in n.lower():
        if i in vowels:
            vowelscount+=1
    return vowelscount

print(Vowels("You are Here"))
            
        