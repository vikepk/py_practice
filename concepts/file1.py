import file2 as a

# a.add(2,3)
try:
    a=[1,2]
    print(a[3])
except Exception as e:
    print("An Error occured",e)
finally:
    print("Over")
    