class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        f=0
        if(nums[0]>0 and nums[0]!=1):
            return 1
        if(len(nums)==1 and nums[0]!=1):
            return 1
        elif(len(nums)==1 and nums[0]==1):
            return 2
        for i in range(0,n-1):
            if(nums[i]<=0 and nums[i+1]<=0):
                f=f+1
            if(nums[i]<=0 and nums[i+1]>0 and nums[i+1]!=1):
                f=-1
                return 1
            elif(nums[i]>=0 and nums[i+1]-nums[i]>1):
                f=-1
                return nums[i]+1
        if(f==len(nums)-1):
            return 1
        return nums[n-1]+1
