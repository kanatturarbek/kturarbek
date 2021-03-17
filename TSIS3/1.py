a=input().split()
s=0
d=""
for i in a:
    s+=1
    if s%2==1:
        d+=i
        d+=" "
print(d)

