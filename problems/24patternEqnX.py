def patternEqn(n):
    lst=['X'*i for i in range(1,9,2) ]
    print(lst)
    sum=0
    for l in lst:
        s=l.replace('X',n)
        sum=int(sum)+int(s)
    print('{0} + {1} + {2} + {3} = {4}'.format(n*1,n*3,n*5,n*7,sum))
    


patternEqn('3')