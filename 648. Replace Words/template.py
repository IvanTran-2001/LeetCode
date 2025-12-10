class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        my_dict = {}
        
        for word in dictionary:
            my_dict[word] = None
        
        new_array = sentence.split(' ')
        
        for c in range(len(new_array)):
            for i in range(1, len(new_array) + 1):
                if new_array[c][:i] in my_dict:
                    new_array[c] = new_array[c][:i]
                    break
        
        return " ".join(new_array,)

if __name__ == "__main__":
    yes = Solution()

    print(yes.replaceWords(["cat","bat","rat"], "the cattle was rattled by the battery"))

