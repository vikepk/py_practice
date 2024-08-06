import array as arr

names=["Pk","Dins","Ask","Ak"]
#Mutable Changeable
#  names.append(3)
# print(names.index("Dins"))
# names.insert(1,"JBK")
# names.remove("FJ")
# names.clear() 
# print("Ak" in names)
# print(len(names))
# print(names)

numbers=arr.array('i',[1,2,3,4,5])
# print(numbers)
numbers.remove(2)
for nu in numbers:
    print(nu,end="\n")