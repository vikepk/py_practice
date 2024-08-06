def deStarStr(n=""):
    n=n.split()[::-1]
    result=''
    for i in range(len(n)):
        result=result+i*'*'+n[i]
    return result
#   return '*'.join((reversed(n.split())))

print(deStarStr("Hello ramu Where are you"))
#you*are*Where*ramu*Hello

# you*are**Where***ramu****Hello
# With length of star