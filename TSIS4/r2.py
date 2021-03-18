import re 
text=input()
# x=re.split(r"\b[.,]?",text)
# for i in x:
#     print(i)
x=re.findall(r"\d+",text)
for i in x:
    print(i)
