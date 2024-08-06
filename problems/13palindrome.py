def palindrome(n):
    #   rev=n[::-1]
    rev=''.join(reversed(n))
    return n==rev

def interChangepair(items=''):
    items=list(items)
    n=len(items)
    # if n%2==0:
    for i in range(0,n,2):
        if n-1==i:
            break
        temp=items[i]
        items[i]=items[i+1]
        items[i+1]=temp
    return items 

# print(interChangepair("Prem"))
# Changing the value Pairs
# print(palindrome(input("Enter the string to check Palindrome : ").lower()))

# n=121121
# if str(n)==str(n)[::-1]:
#     print(f"{n} is Plaindrome")
# else:
#     print(f"{n} Not a Plaindrome")
    
    
def reverse(string):
    rev_string=string.split()
    # for i in string:
    #     rev_string=i+rev_string
    return rev_string[::-1]

for i in reverse("Hello is you"):
    print(i[::-1],end=" ")