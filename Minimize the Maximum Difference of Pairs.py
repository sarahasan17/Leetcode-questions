class Solution(object):
    def  search1(self,nums,mid,p):
        n=len(nums)
        c=0
        i=0
        while(i<n-1):
            if(nums[i+1]-nums[i]<=mid):
                c=c+1
                i=i+1
            if(c>=p):
                return 1
            i=i+1
        return 0
    def minimizeMax(self, nums, p):
        nums.sort()
        l=0
        n=len(nums)
        h=nums[n-1]-nums[0]
        while(l<h):
            mid=l+(h-l)//2
            if self.search1(nums,mid,p):
                h=mid
            else:
                l=mid+1
        return l
        

        
