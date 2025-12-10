# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode
        temp = l3
        remainder = False
        while l1 and l2:
            total = 0
            if remainder:
                total += 1
                remainder = False
            total += l1.val + l2.val
            if total > 9:
                total -= 10
                remainder = True
            
            temp.next = ListNode(total)
            temp = temp.next
            
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            total = 0
            if remainder:
                total += 1
                remainder = False
            
            total += l1.val
            if total > 9:
                total -= 10
                remainder = True
            
            temp.next = ListNode(total)
            temp = temp.next
            
            l1 = l1.next

        while l2:
            total = 0
            if remainder:
                total += 1
                remainder = False
            
            total += l2.val
            if total > 9:
                total -= 10
                remainder = True
            
            temp.next = ListNode(total)
            temp = temp.next
            
            l2 = l2.next
        
        if remainder:
            temp.next = ListNode(1)
        
        return l3.next

            

        
        

            
            
