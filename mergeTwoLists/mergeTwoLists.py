# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        valList = ListNode()
        head = valList

        while list2 and list1:
            if (list1.val > list2.val):
                valList.next = list2
                list2 = list2.next

            else:
                valList.next = list1
                list1 = list1.next
            
            valList = valList.next
        
        if list1:
            valList.next = list1   

        elif list2:
            valList.next = list2   
            

        return head.next
    
        

