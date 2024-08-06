import random 
import math
from datetime import datetime



# random.seed(datetime.now())
def randomRange(n):
    moves=[]
    for i in range(1,n+1):
        direction=random.randrange(1,5)
        dirstr=""
        if direction==1:
            dirstr='U'
        elif direction==2:
            dirstr='D'
        elif direction==3:
            dirstr='L'
        elif direction==4:
            dirstr='R'
        moves.append((dirstr,direction))
    return moves

def destination(moves,origin):
    des=origin.copy()
    for m in moves:
        if m[0]=='R':
            des[1]+=m[1]
        elif m[0]=='L':
            des[1]-=m[1]
        elif m[0]=='U':
            des[0]+=m[1]
        elif m[0]=='D':
            des[0]-=m[1]
    return des

origin=[0,0]
moves=randomRange(10)
des=destination(moves,origin)
print("Moves:", moves)
print("Destination:", des)
print("========================")
print("Distance Difference",math.sqrt(pow((des[0] - origin[0]), 2) + pow((des[1] - origin[1]), 2)))