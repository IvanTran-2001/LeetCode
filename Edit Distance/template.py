class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        my_dict = {}
        for i, n in enumerate(word2):
            if n in my_dict:
                my_dict[n][0].append(i)
            else:
                my_dict[n] = [[i],[]]
        
        print(my_dict)
            
        for i, n in enumerate(word1):
            if n in my_dict:
                my_dict[n][1].append(i)
        
        return my_dict
        

if __name__ == "__main__":
    yes = Solution()

    print(yes.minDistance("hourse", "hoooosseeee"))