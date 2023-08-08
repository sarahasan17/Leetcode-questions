class Solution(object):
    def reverse(self, x):
        f=0
        n=x
        if(x<0):
            f=1
            n=-n
        num=0
        while(n>0):
            a=n%10
            num=num*10+a
            n=n//10
        if(f==1):
            num=-num
        if num>=2147483651 or num<=-2147483651:
            num=0
        return num
