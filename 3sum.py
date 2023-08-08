class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        n=len(nums)
        val=0
        diff=100000
        for i in range(0,n):
            j=i+1
            k=n-1
            while(j<k):
                sum=nums[i]+nums[j]+nums[k]
                if sum==target:
                    val=sum
                    diff=0
                    return val
                elif(sum>target):
                    if(sum-target<diff):
                        val=sum
                        diff=sum-target
                    k=k-1
                else:
                    if(target-sum<diff):
                        val=sum
                        diff=target-sum
                    j=j+1
        return val
                
                
