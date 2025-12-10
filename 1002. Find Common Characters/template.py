class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        my_dict = {}
        temp_my_dict = {}
        new_array = []

        if len(words) == 1:
            return words[0]
        
        for c in words[0]:
            if c in my_dict:
                my_dict[c] += 1
            else:
                my_dict[c] = 1
        
        for i in range(1, len(words)):
            for c in words[i]:
                if c in my_dict:
                    if my_dict[c] > 0:
                        my_dict[c] -= 1
                        if c in temp_my_dict:
                            temp_my_dict[c] += 1
                        else:
                            temp_my_dict[c] = 1

            my_dict = temp_my_dict.copy()
            temp_my_dict = {}
        
        for i in my_dict:
            for _ in range(my_dict[i]):
                new_array.append(i)
        
        return new_array
                    

if __name__ == "__main__":
    yes = Solution()

    print(yes.commonChars(["bella","label","roller"]))

