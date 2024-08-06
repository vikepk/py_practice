def bankTransactions():
    inp=input("Enter Bank Transaction Deposit(D) Withdraw(W) : ")
    inp=inp.split(' ')
    # print(inp)
    deposit=[]
    withDraw=[]
    for i in range(0,len(inp),2):
        if inp[i]=='D':
            deposit.append(int(inp[i+1]))
        else:
            withDraw.append(int(inp[i+1]))
    # print(deposit,withDraw)
    print("           Deposit      Withdraw")
    for i in range(0,len(inp)):
        if inp[i]=='D':
            print("              {0}               ".format(inp[i+1]))
        elif inp[i]=='W':
            print("                             {0} ".format(inp[i+1]))
        
    print("Total     ",sum( deposit))
    print("Balance   ",sum(deposit)-sum(withDraw))
    
    
    return

bankTransactions()