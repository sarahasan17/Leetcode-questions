import numpy
class Solution(object):
    def canSplitArray(self, nums, m):
        n=len(nums)
        sum=0
        l1=[]
        if(n==1):
            return 1
        if n==2:
            return 1
        c=0
        for i in range(0,n):
            c=c+1
            if(c<=2):
                sum=sum+nums[i]
            if(sum>=m):
                print(sum)
                return 1
            if(c==2):
                sum=nums[i]
                c=1
        sum=0
        c=0
        for i in range(n-1,0,-1):
            c=c+1
            if(c<=2):
                sum=sum+nums[i]
            if(sum>=m):
                return 1
            if(c==2):
                sum=nums[i]
                c=1
        return 0
        
