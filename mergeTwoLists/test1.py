
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        valList = []

        while list1 and list2:
            if list1[0] < list2[0]:
                valList.append(list1.pop(0))
            else:
                valList.append(list2.pop(0))
        
        if not list1:
            if list2:
                valList = valList + list2
        else:
            valList = valList + list1

            

        return valList
    
if __name__ == "__main__":
    list1 = [1,2,4]
    list2 = [1,3,4]

    yes = Solution()

    print(yes.mergeTwoLists(list1, list2))