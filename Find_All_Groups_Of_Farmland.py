class Solution(object):
    def findFarmland(self, land):
        n=len(land)
        m=len(land[0])
        def dfs(a,b,l):
            if(a<0 or a==n or b<0 or b==m or land[a][b]==0 or land[a][b]==2):
                return
            if(a==0 and b==0):
                l[0],l[1],l[2],l[3]=a,b,a,b
                land[a][b]=2
            elif(a>0 and land[a-1][b]==0 and b>0 and land[a][b-1]==0):
                l[0],l[1],l[2],l[3]=a,b,a,b
                land[a][b]=2
            elif(a>0 and land[a-1][b]==0 and b==0):
                l[0],l[1],l[2],l[3]=a,b,a,b
                land[a][b]=2
            elif(a==0 and b>0 and land[a][b-1]==0):
                l[0],l[1],l[2],l[3]=a,b,a,b
                land[a][b]=2
            elif((a>0 and land[a-1][b]==2) or (b>0 and land[a][b-1]==2)):
                if(a>=l[2] and b>=l[3]):
                    l[2],l[3]=a,b
                land[a][b]=2
            dfs(a+1,b,l)
            dfs(a,b+1,l)
        s=[]
        for i in range(0,n):
            for j in range(0,m):
                if(land[i][j]==1):
                    l=[0,0,0,0]
                    dfs(i,j,l)
                    s.append(l)
        return s
