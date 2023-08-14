class Solution(object):
    def majorityElement(self, nums):
        n=len(nums)
        l=[]
        if(n==1):
            l.append(nums[0])
            return l
        if(n==2):
            l.append(nums[0])
            if(nums[0]!=nums[1]): l.append(nums[1])
            return l
        nums.sort()
        c=0
        for i in range(0,n-1):
            if(nums[i]==nums[i+1]): c+=1
            else:
                if(c>=n//3): l.append(nums[i])
                c=0
        if(c>=n//3): l.append(nums[n-1])
        return l



