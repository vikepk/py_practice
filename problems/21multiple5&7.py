def multiple():
    for i in range(2000,3201):
        if i%7==0 and not i%5==0:
            print(i,end=",")
            
# multiple()

lst=[str(x) for x in range(2000,3201) if x%5==0 and x%7!=0]
# print(','.join(lst))

