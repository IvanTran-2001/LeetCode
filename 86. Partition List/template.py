class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return None
        
        temp = head
        save_head = ListNode()
        before = None
        save = save_head
        while temp:
    
            if temp and temp.val >= x:
                save.next = temp
                
                while save.next and save.next.val >= x:
                    save = save.next
                if before:
                    before.next = save.next
                    temp = before.next
                else:
                    before = save.next
                    temp = before
                    head = before
                save.next = None
            else:
                before = temp
                temp = temp.next
            
        if save_head.next:
            if before:
                before.next = save_head.next
            else:
                return save_head.next
        return head
            
            

if __name__ == "__main__":
    yes = Solution()
    node1 = ListNode(2)
    node2 = ListNode(1)
    # node3 = ListNode(3)
    # node4 = ListNode(2)
    # node5 = ListNode(5)
    # node6 = ListNode(2)

    # Link the nodes together
    node1.next = node2
    # node2.next = node3
    # node3.next = node4
    # node4.next = node5
    # node5.next = node6

    current = (yes.partition(node1, 0))
    
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

