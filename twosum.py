class Solution(object):
    def twoSum(self, nums, target):
        j=0
        n=len(nums)
        l=[]
        for j in range(0,n):
            for k in range (j+1,n):
                if(nums[j]+nums[k]==target):
                    l.append(j)
                    l.append(k)
                    return l
        return l
