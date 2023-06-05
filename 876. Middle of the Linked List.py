class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = ListNode([1,2,3,4,5])
#head = ListNode([1,2,3,4,5,6])
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        count=0
        liste=[]
        while head is not None:
            count+=1
            liste.append(head)
            head=head.next
        #middle = n/2
        middle=count//2
        return liste[middle]

print(Solution().middleNode(head))