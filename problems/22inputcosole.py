def inputConsole():
    values=input("Enter the list of values : ")
    lst=values.split(',')
    print(lst)
    print("Minimum Number :",min(lst))
    print("Maximum Number :",max(lst))
    print("Sum of Numbers :",sum( int(i) for i in lst)  )
    print("Average Number :",sum( int(i) for i in lst)/len(lst))
    print("Second Largest Number : " ,list(reversed(lst))[-2])
    
    


inputConsole()