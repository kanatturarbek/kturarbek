import re
text=input()
x=re.search(r'\b[0-9a-zA-Z]',text)
if x:
    print(x.group())
else:
    print(-1)    