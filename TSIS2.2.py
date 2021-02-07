class Solution:
    def subtractProductAndSum(self, n: int) -> int:
     sum=0
     product=1
     a=str(n)    
     for i in a:
       p=int(i)
       sum+=p
       product*=p
     result=product-sum
     return result