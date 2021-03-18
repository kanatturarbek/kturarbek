import re
text=input()
x=re.findall("[EUOAeIiuoa][EYUOAeyuoa]+",text)
if x:
    for i in x:
     print(i)
else:
    print(-1)