class Solution(object):

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        i = 0
        length = 0
        front = 0
        maxLength = 0
        
        opened = 0
        closed = 0
        
        while i < len(s):
            
            if s[i] == ')':
                closed += 1
            else:
                opened += 1
            
            i += 1
            
            while opened >= closed and i < len(s):
                
                if s[i] == ')':
                    closed += 1
                else:
                    opened += 1
                    
                if closed == opened:
                    length = i - front + 1
                
                i += 1
            
            front = i
            
            if maxLength < length:
                maxLength = length
                
            
            opened = 0
            closed = 0
        
        i = 0
        length = 0
        front = 0
        
        s = s[::-1]
        
        while i < len(s):
            
            if s[i] == ')':
                closed += 1
            else:
                opened += 1
            
            i += 1
            
            while opened <= closed and i < len(s):
                
                if s[i] == ')':
                    closed += 1
                else:
                    opened += 1
                    
                if closed == opened:
                    length = i - front + 1
                
                i += 1
            
            front = i
            
            if maxLength < length:
                maxLength = length
                
            
            opened = 0
            closed = 0

        return maxLength
            
            
        
        
        

if __name__ == "__main__":
    yes = Solution()

    print(yes.longestValidParentheses("(((()"))