class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        arrayList = []
        checkList = {}
        count = 0
        
        for n in strs:
            word = ''.join(sorted(n))
            if word in checkList:
                arrayList[checkList[word]].append(n)
            else:
                arrayList.append([n])
                checkList[word] = count
                count += 1
        
        return arrayList
                
    
    

if __name__ == "__main__":
    yes = Solution()

    print(yes.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))