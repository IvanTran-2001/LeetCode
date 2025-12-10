from collections import deque
class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        if len(hand) % groupSize != 0:
            return False
        
        if groupSize == 1:
            return True
        
        my_dict = {}
        
        for i in hand:
            my_dict[i] = my_dict.get(i, 0) + 1
        
        hand = sorted(my_dict)
        
        minimum_count = 0
        counter = deque()
        prev = None
        total = 0
        
        for element in hand:
            if my_dict[element] >= minimum_count:
                if minimum_count == 0:
                    
                    if counter:
                        return False
                    
                    counter.append([groupSize - 1, my_dict[element]])
                    minimum_count += my_dict[element]
                    total = groupSize - 1
                else:
                    if prev + 1 == element and my_dict[element] >= minimum_count:
                        
                        total -= 1
                        if my_dict[element] > minimum_count:
                            counter.append([groupSize - 1 - total, my_dict[element] - minimum_count])
                            total = groupSize - 1
                            
                        minimum_count = my_dict[element]
                        counter[0][0] -= 1
                        
                        if counter[0][0] == 0:
                            minimum_count -= counter[0][1]
                            counter.popleft()
                            
                    else:

                        return False
                
                prev = element
                    
            else:
                return False
        
        if counter:
            return False
        
        return True
                    
if __name__ == "__main__":
    yes = Solution()

    print(yes.isNStraightHand([8,6,5,7,9], 5))

