#longest palindrome substring
class Solution(object):
    def longestPalindrome(self, s):
        def newfun(l,r):
            while(l>=0 and r<len(s) and s[l]==s[r]):
                l=l-1
                r=r+1
            return s[l+1:r]
        final=""
        for i in range (0,len(s)):
            c=newfun(i,i)
            if(len(final)<len(c)):
                final=c
            c1=newfun(i,i+1)
            if(len(final)<len(c1)):
                final=c1
        return final
