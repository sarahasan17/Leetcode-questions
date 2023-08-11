class Solution(object):
    def searchInsert(self, a, target):
        if(target<=a[0]):
            return 0
        elif(target>a[len(a)-1]):
            return len(a)
        for i in range(0,len(a)-1):
            if(a[i]<target and a[i+1]>=target):
                return i+1
        return 0
