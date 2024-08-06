def validBinary(n=""):
     b=set("10")
     a=set(n)
     return a==b or a=={'0'} or a=={'1'}

# print(validBinary("0003110"))

def checkHex(s):
   
    # Iterate over string
    for ch in s:
 
        # Check if the character
        # is invalid
        if ((ch < '0' or ch > '9') and
            (ch < 'A' or ch > 'F')):
                 
            print("False")
            return
         
    # Print true if all
    print("True")
 
s = "BF567C"
  
# Function call
checkHex(s)