# the voices wont stop
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # i need a guy to give me head rn
        if head==None or head.next==None:
            return head
        temp,temp2=head,head.next
        temp.next,temp2.next=temp2.next,temp
        t=temp
        head=temp2 # store the damn value of temp2 in head
        if temp.next==None or temp2.next==None or temp.next.next==None or temp2.next.next==None:
            return head
        # need to move the stupid nodes 2 steps in forward direction 
        temp2,temp=temp.next.next,temp2.next.next 
        # pondering about offing myself rn
        t.next=temp2
        while temp and temp2:
            temp.next,temp2.next=temp2.next,temp
            t=temp
            if temp.next==None or temp2.next==None or temp.next.next==None or temp2.next.next==None:
                break
            # need to move the, 2 steps in forward direction (again hahaha)
            temp2,temp=temp.next.next,temp2.next.next
            t.next=temp2
        # finally completing this so we can off ourselves 
        return head
# comments are here because i felt nice 
