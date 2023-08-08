class Solution(object):
    def maxArea(self, a):
        l=0
        r=len(a)-1
        max=0
        while(l<=r):
            if(a[l]<a[r]):
                d=(r-l)*a[l]
                l=l+1
            elif(a[l]>a[r]):
                d=(r-l)*a[r]
                r=r-1
            elif(a[l]==a[r]):
                d=(r-l)*a[l]
                if(r-l>=2 and a[l+1]>a[r-1]):
                    l=l+1
                else:
                    r=r-1
            if(d>max):
                max=d
        return max
