class Solution(object):
    def fourSum(self, nums, target):
        i=0
        n=len(nums)
        nums.sort()
        s=set()
        for i in range(0,n):
            for j in range(i+1,n):
                k=j+1
                l=n-1
                while(k<l and l<n):
                    sum=nums[i]+nums[j]+nums[k]+nums[l]
                    if(sum==target):
                        s.add((nums[i],nums[j],nums[k],nums[l]))
                        l=l-1
                        k=k+1
                    elif(sum<target):
                        k=k+1
                    else:
                        l=l-1
        return s
                        


            
