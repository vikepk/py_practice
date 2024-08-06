def SentenceLength(strSen=""):
    nlst=strSen.split(' ')
    long=""
    for i in nlst:
        if len(nlst)>len(long):
            long=i
    print(long,len(long))
    
    
SentenceLength(input("Enter Sentence : "))