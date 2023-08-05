#shortest palindrome partial
class Solution(object):
    def shortestPalindrome(self, s):
        def max(l,r):
            if(l>=0 and r<len(s) and s[l]==s[r]):
               l=l-1
               r=r+1
            return l,r
        def max1(l,r):
            if(l>=0 and r<len(s) and s[l]==s[r]):
               l=l-1
               r=r+1
            return s[l+1:r]
        r,l=max(len(s)-1,0)
        new=""
        n=max1(0,0)
        m=max1(0,1)
        if(r==len(s)-1):
            if(len(n)>len(m)):
               new=s[len(s)-1:len(n)-1:-1]+s
            else:
               new=s[len(s)-1:len(m)-1:-1]+s
        else:
            new1="" 
            mid=0     
            for i in range (l,r):
                
            if(len(new1)==0):
                new=s[0:l]+s[r-1:l:-1]+s[l:r-1]+s[r::]
            else:
                m1=len(new1)
                in1=(m1/2)+mid
                new=s[0:l]+s[r-1:in1:-1]+new1+s[in1:r-1]+s[r::]
        return new
