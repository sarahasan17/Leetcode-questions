#shortest palindrome partial
class Solution(object):
    def shortestPalindrome(self, s):
        i=0
        num=len(s)
        for j in range(0,num):
            if(s[i]==s[num-j-1]):
                i=i+1
        if i==num:
            return s
        p1=s[i:num][::-1]
        return p1+self.shortestPalindrome(s[:i])+s[i:]
