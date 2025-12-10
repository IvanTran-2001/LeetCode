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
        head = l1
        extend = None
        total = 0
        
        while l1 and l2:

            total += l1.val + l2.val

            if total > 9:
                total -= 10
                l1.val = total
                total = 1
            else:
                l1.val = total
                total = 0

            if not l1.next:
                extend = l1

            l1 = l1.next
            l2 = l2.next

        while l1:
            total += l1.val

            if total > 9:
                total -= 10
                l1.val = total
                total = 1
            else:
                l1.val = total
                total = 0
            if not l1.next:
                extend = l1
            
            l1 = l1.next
        
        if l2:
            extend.next = l2
            extend = extend.next

            while extend:
                total += extend.val

                if total > 9:
                    total -= 10
                    extend.val = total
                    total = 1
                else:
                    extend.val = total
                    total = 0
                if not extend.next:
                    break
                extend = extend.next
            
            if total == 1:
                extend.next = ListNode(1)
        else:
            if total == 1:
                extend.next = ListNode(1)

        return head

def convert(list):
    head = ListNode()
    temp = head

    for i in list:
        temp.next = ListNode(i)
        temp = temp.next

    return head.next

def printLL(head):
    while head != None:
        print(head.val, end="")
        print(" ", end="")
        head = head.next
    print


if __name__ == "__main__":
    yes = Solution()
    head1 = convert([9,9,9,9,9,9,9])
    head2 = convert([9,9,9,9])
    printLL(yes.addTwoNumbers(head1, head2))

    


        
        

            
            
