class Solution(object):
    def strStr(self, haystack, needle):
        n,m=len(haystack),len(needle)
        if(n==1 and m==1):
            if(haystack[0]==needle[0]):
                return 0
        for i in range(0,n-m+1):
            if(haystack[i]==needle[0]):
                if(needle[:]==haystack[i:i+m]):
                    return i
        return -1
