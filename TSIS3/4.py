a=input().split()
b=len(a)
s=0
v=""
for i in range(b):
    if int(a[i])!=0:
        a[0+s]=a[i]
        s+=1
for q in range(s,b):
    a[q]='0'    
for k in a:
    v+=k
    v+=" "

print(v)    