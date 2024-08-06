def calculatePf(n):
    DA="{BASIC}* 0.4"
    HRA="{BASIC}+{DA}*0.30"
    PF="{BASIC}+{DA}+{HRA}*0.0833"
    DA=DA.replace("{BASIC}",n)
    print("DA",eval(DA))
    HRA=HRA.replace("{BASIC}",n)
    HRA=HRA.replace("{DA}",str(eval(DA)))
    print("HRA",eval(HRA))
    PF=PF.replace("{BASIC}",n)
    PF=PF.replace("{DA}",str(eval(DA)))
    PF=PF.replace("{HRA}",str(eval(HRA)))
    print("PF",eval(PF))
    
calculatePf('10000')
    