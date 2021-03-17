a=input().split()
mini=11111
s=""
for i in a:
    if int(i)>0 and int(i)<mini:
        mini=int(i)
print(mini)        
