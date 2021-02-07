class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
     n=len(nums)
     m=0
     cnt=0
     while m<n:
       a=m+1
       while a<n:
          if(nums[m]==nums[a]):
            cnt+=1 
          a+=1 
       m+=1 
     return cnt