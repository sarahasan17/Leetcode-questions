class Solution(object):
    def finalString(self, s):
        new=s
        n=len(s)
        j=0
        c=0
        for i in range(0,n):
            if(s[i]=='i'):
                j=i-c
                a=new[:j][::-1]
                new=a+new[j+1:]
                c=c+1
                print(new)
        return new
