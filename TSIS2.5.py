class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
      x=0
      y=0
      for i in gain:
       x+=i
       if(x>y):
        y=x 
       
           
      return y 