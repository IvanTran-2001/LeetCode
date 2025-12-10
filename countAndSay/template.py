class Solution(object):
    def countAndSay(self, n):
        return self.countAndSayOne(n, ["1"])
        
    def countAndSayOne(self, n, word):
        """
        :type n: int
        :rtype: str
        """
        if n - 1 == 0:
            return "".join(word)
        
        j = 0
        for i in range(len(word)):
            
            count = len(word[i+j])
            
            if str(count) == word[i+j][0]:
                word[i+j] = word[i+j][0] + word[i+j][0]
            else:
                word[i+j] = word[i+j][0]
                if j+i - 1 >= 0 and (word[j+i - 1][0] == str(count)):
                    word[j+i - 1] = word[j+i - 1] + word[j+i - 1][0]
                else:
                    word.insert(j+i, str(count))
                    j += 1
                    
        return self.countAndSayOne(n-1, word)
            
        

if __name__ == "__main__":
    yes = Solution()

    print(yes.countAndSay(35))