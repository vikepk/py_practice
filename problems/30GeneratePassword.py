import random as rand

password=""
diffChar=['$','#','@']
# for i in range(0,4):


# strMultiply=[rand.randrange(0,6) for i in range (1,5)  ]
# print(strMultiply)
password+=chr(rand.randrange(ord('a'),ord('z')))
password+=str(rand.randrange(0,9))
password+=chr(rand.randrange(ord('A'),ord('Z')))
password+=diffChar[rand.randrange(0,len(diffChar))]
    
print(password.removeprefix('a'),len(password))

