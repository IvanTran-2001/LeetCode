class Node(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def print_list(head):
        current = head
        while current:
            print(current.val, end=" ")
            current = current.next
        print("None")
        
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return 
        
        if k == 0 or not head.next:
            return head

        temp = head
        getEnd = head
        count = 1
        
        while getEnd.next:
            count += 1
            getEnd = getEnd.next
        
        k = count - k
        k = k % count
        
        if k == 0:
            return temp
        
        head = temp
        k -= 1
        while head.next and k > 0:
            head = head.next
            k -= 1
            
        main = head.next
        head.next = None
        
        getEnd.next = temp
    
        
        return main
    

if __name__ == "__main__":
    yes = Solution()
    
    head = Node(1)      # Head node
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    # Linking the nodes together
    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth

    Node.print_list(yes.rotateRight(head, 2))