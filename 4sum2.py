class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        data={}
        for i in nums1:
            for j in nums2:
                sum=i+j
                if sum not in data:
                    data[sum]=0
                data[sum]+=1
        c=0
        for i in nums3:
            for j in nums4:
                sum=i+j
                if -sum in data:
                    c=c+data[-sum]

        return c
