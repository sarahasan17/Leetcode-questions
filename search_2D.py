class Solution(object):
    def searchMatrix(self, matrix, target):
        n=len(matrix)
        m=len(matrix[0])
        l=0
        r=m*n-1
        while l<=r:
            mid=(l+r)//2
            ro,col=divmod(mid,m)
            if matrix[ro][col]==target:
                return 1
            elif matrix[ro][col]>target:
                r=mid-1
            else:
                l=mid+1
        return 0
