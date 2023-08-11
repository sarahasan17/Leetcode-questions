class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min=len(strs[0])
        n=len(strs)
        for i in range(1,n):
            if(len(strs[i])<min):
                min=len(strs[i])
        out=""
        f=0
        j=0
        for i in range(0,min):
            for j in range(0,n-1):
                if(strs[j][i]!=strs[j+1][i]):
                    f=1
                    break
            if(f==1):
                break
            else:
                out=out+strs[j][i]
        return out
