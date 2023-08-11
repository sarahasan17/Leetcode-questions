class Solution(object):
    def trap(self, height):
        l,r=0,len(height)-1
        l1,r1=height[l],height[r]
        rain=0
        while l<r:
            l1,r1=max(l1,height[l]),max(r1,height[r])
            if(l1<=r1):
                rain+=l1-height[l]
                l=l+1
            else:
                rain+=r1-height[r]   
                r=r-1
        return rain 
