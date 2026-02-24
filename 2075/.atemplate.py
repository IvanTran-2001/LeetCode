class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:

        if rows==1:
            return encodedText.rstrip()
        
        ans = []
        step = len(encodedText)//rows
        for i in range(step):
            for j in range(rows):
                index = step*j + j + i
                if index < len(encodedText):
                    ans.append(encodedText[index])
                else:
                    break


        
        return "".join(ans).rstrip()

if __name__ == "__main__":
    yes = Solution()

    print(yes.decodeCiphertext("ch   ie   pr", 3))
    print(len(yes.decodeCiphertext("ch   ie   pr", 3)))

