def ChinesePuzzle(heads,legs):
    res=[]
    for i in range(1,heads+1):
        chicken=i
        rabbit=heads-chicken
        if chicken*2 + rabbit*4==legs:
            res.append({'chicken':chicken,'rabbit':rabbit})
    return res

print(ChinesePuzzle(35,94))
            
    