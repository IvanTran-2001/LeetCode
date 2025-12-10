import CusNode
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if left == right or not head.next:
            return head
        
        temp = head
        before = None
        index = 1
        
        while head:
            if left == index:
                break
            before = head
            head = head.next
            index += 1
            
        attach = before
        
        if not head:
            return temp
        
        before = head
        after = head.next
        head.next = None
        end_point = head
        head = after
            
        while head.next:
            if right == index:
                break
            
            after = head.next
            head.next = before
            before = head
            head = after
            
            index += 1
        
        if right != index:
            head.next = before
            before = head
        else:
            end_point.next = head
        
        if attach:
            attach.next = before
        else:
            return before
        
        return temp
        
if __name__ == "__main__":
    yes = Solution()

    head = yes.reverseBetween(CusNode.list_to_singly_linked_list([1,2,3]), 2,3)
    
    CusNode.print_el(head)

