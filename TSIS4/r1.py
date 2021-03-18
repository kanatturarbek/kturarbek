# import re 
# x=int(input())

# for i in range(x):
#     q=input()
#     p=re.search(r"\b+[0-9]"r"\b-[0-9]"|r"\b[0-9]",q)
#     if p:
#         print("True")
#     else:
#         print("False")    
import re
for _ in range(int(input())):
	print(bool(re.match(r'^[-+]?[0-9]*.[0-9]+$', input())))
