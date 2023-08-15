class Solution(object):
    def partition(self, head, x):
        t,l,s=head,[],[]
        while(t):
            l.append(t.val)
            t=t.next
        for j in range(0,len(l)):
            if(l[j]<x): s.append(l[j])
        for j in range(0,len(l)):
            if(l[j]>=x): s.append(l[j])
        l1=ListNode(0)
        tail=l1
        for k in s:
            t1=ListNode(k)
            tail.next=t1
            tail=tail.next
        result=l1.next
        l1.next=None
        return result
