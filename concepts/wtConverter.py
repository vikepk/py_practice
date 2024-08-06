wt=float(input("Weight : "))
unt=input("(K)g or (L)bs : ")
if unt.lower()=='k':
    wt=wt*2.20462
    print("Weight in Pound is " +str(wt))
elif unt.lower()=='l':
    wt=wt*0.453592
    print("Weight in Kilogram is" +str(wt))
else:
    print('Choose valid Kilogram(k) or Pound(L)')
    exit()

