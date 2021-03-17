# a=input().split()
# b=int(input())
# c=len(a)
# s=""
# for i in range(c):
#     if (b+i)%c<i:
#         s+=a[i]
#         s+=" "
# for i in range(c):
#     if (b+i)%c>i:
#         s+=a[i]
#         s+=" "        
# print(s)           
l = input().split()
k = int(input())
k %= len(l)
for elem in l[-k:] + l[:-k]:
    print(elem, end=' ')