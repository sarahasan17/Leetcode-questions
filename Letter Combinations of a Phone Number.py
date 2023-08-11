class Solution(object):
    def letterCombinations(self, digits):
        a=[]
        comb=["0","0","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        def solve(i,sum):
            if(i==len(digits)):
                a.append(sum)
            else:
                c=digits[i]
                b=comb[int(c)]
                for k in b:
                    solve(i+1,sum+k)
        if digits=="":
            return []
        solve(0,"")
        return a
