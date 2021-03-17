a,b=input().split()
masha=set()
borya=set()
for i in range(int(a)+int(b)):
    c=input()
    if i<int(a):
        masha.add(c)
    else: 
        borya.add(c)    
same=masha.intersection(borya)
mash=masha.difference(borya)
bory=borya.difference(masha)
print(len(same))
print(*sorted(same,key=int))
print(len(mash))
print(*sorted(mash,key=int))
print(len(bory))
print(*sorted(bory,key=int))