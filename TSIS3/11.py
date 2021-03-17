d=dict()
try:
    while(True):
        list=input()
        words=list.split()
        for word in words:
            if d.get(word,0)!=0:
                d[word]+=1
            else:
                d[word]=1 
except:
    pass
def my_func(item):
    return(-item[1],item[0])
for item in sorted(d.items(),key=my_func):
    print(item[0])
        
