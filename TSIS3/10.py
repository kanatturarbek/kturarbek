# n=input()
# A={}
# for i in range(int(n)):
#     a,b=input().split()
#     A[b]=a
#     A[a]=b
# c=input()
# print(A[c])
n=input()
A=list()
B=list()
for i in range(int(n)):
    a,b=input().split()
    A.append(a)
    B.append(b)
c=input()
for q in range(len(A)):
    if A[q]==c:
        print(B[q])
    elif B[q]==c:
        print(A[q])  

