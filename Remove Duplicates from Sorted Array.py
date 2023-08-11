class Solution(object):
    def removeDuplicates(self, nums):
        s=set(nums)
        n=len(s)
        nums[:]=list(s)
        nums.sort()
        return n
