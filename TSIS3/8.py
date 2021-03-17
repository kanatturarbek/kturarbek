A=input().split()
B=input().split()
a=set(A)
b=set(B)
c=a&b
print(*sorted(c,key=int))
    