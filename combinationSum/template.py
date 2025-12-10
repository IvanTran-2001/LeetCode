class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return self.recurse(sorted(candidates), target, 0)
        
    def recurse(self, canditates, target, j):
        
        myList = []
        for i in range(j, len(canditates)):
            
            if target - canditates[i] < 0:
                return myList
            elif target - canditates[i] == 0:
                myList.append([canditates[i]])
                return myList
            
            tempNum = self.recurse(canditates, target - canditates[i], i)
            if tempNum:
                for k in tempNum:
                    myList.append([canditates[i]] + k)
            
        return myList
        
        
        

if __name__ == "__main__":
    yes = Solution()

    print(yes.combinationSum([2,3,6,7,10], 10))