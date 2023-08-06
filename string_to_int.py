lass Solution(object):
    def myAtoi(self, s):
        n=len(s)
        num=0
        f=0
        g=0
        h=0
        c=0
        space=0
        for i in range(0,n):
            if s[i]==' ' and c>0:
                break
            if(s[i]==' ' and num==0):
                g=1
            elif s[i]>='a' and s[i]<='z' and num==0:
                break
            elif s[i]>='0' and s[i]<='9':
                num=num*10+(eval(s[i]))
                c=c+1
            elif s[i:i+2]=="+ " or s[i:i+2]=="- ":
                break
            elif c>0:
                break
            elif s[i]=='+' and c>0:
                break
            elif s[i]=='-' and c>0:
                break
            elif s[i]=='-':
                f=f+1
            elif s[i]=='+':
                h=h+1
            elif s[i]=='.':
                break
            elif h==1 and s[i]!=' ':
                break
        if f==1:
            num=num*-1
        if f==1 and h==1 or f>1 or h>1:
            num=0
        if num>2147483647:
            num=2147483647
        if num<-2147483648:
            num=-2147483648    
        return num


       
