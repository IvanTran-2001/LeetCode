class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strOutput = ""
        index = 0
        confirmOutput = ""

        word = strs[0]
        confirm = False
        length = len(min(strs, key = len))

        while length > index:
            
            yep = len(strOutput)
            if yep == length:
                break

            for n in strs:
                if (n[index] != word[index]):
                    confirm = True
                    break


            if confirm:
                confirmOutput = ""
            else:
                confirmOutput += word[index]
            
            if len(confirmOutput) > yep:
                    strOutput = confirmOutput
            
            index += 1

        return strOutput
                
if __name__ == "__main__":
    strs = ["a"]
    yes = Solution()

    print(yes.longestCommonPrefix(strs))