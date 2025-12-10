# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head != None:
            temp = head.next
            if temp != None:
                if head.val == temp.val:
                    while (temp.next != None) and (temp.next.val == head.val):
                        temp = temp.next
                    head.next = temp.next


                while temp != None:
                    temp2 = temp.next
                    if temp2 != None:
                        if temp.val == temp2.val:
                            while (temp2.next != None) and (temp2.next.val == temp.val):
                                temp2 = temp2.next
                            temp.next = temp2.next
                    temp = temp.next
                        
        return head

                    




if __name__ == "__main__":
    yes = Solution()
    yesL = ListNode()
    yesL.val = 1
    yesL.next = ListNode(1, ListNode(1, ))

    print(yes.deleteDuplicates())