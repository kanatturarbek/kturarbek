class Solution:
    def interpret(self, command: str) -> str:
     x=''  
     i=len(command)
     a=0
     while a<i:
         if command[a:a+2]=='()':
           x+='o'
           a+=2
         elif command[a:a+4] =='(al)':
            x+='al'
            a+=4          
         else:
            x+=command[a]
            a+=1
     return x    