#adding 2 number(linked list)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def push(self,new_data):
        new_node=ListNode(new_node)
        new_node.next=self.head
        self.head=new_node
    def addTwoNumbers(self, l1, l2):
        n1=0
        head=l1
        temp=head
        count1=0
        lnew=[]
        while(temp):
            count1=count1+1
            lnew.append(temp.val)
            temp=temp.next
        for i in range (len(lnew)-1,0,-1):
            n1=n1*10+lnew[i]
        n1=n1*10+lnew[0]
        n2=0
        temp=l2
        lnew1=[]
        while(temp):
            lnew1.append(temp.val)
            temp=temp.next
        for i in range (len(lnew1)-1,0,-1):
            n2=n2*10+lnew1[i]
        n2=n2*10+lnew1[0]
        n3=n1+n2
        l3=[]
        g=n3
        while n3>0:
            a=n3%10
            l3.append(a)
            n3=n3/10
        l4=ListNode(g)
        tail=l4
        if(len(l3)==0):
            l4=ListNode(g)
            return l4
        for i in l3:
            temp1=ListNode(i)
            tail.next=temp1
            tail=tail.next
        result=l4.next
        l4.next=None
        return result
