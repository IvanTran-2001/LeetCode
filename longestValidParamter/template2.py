class Solution:
    def longestValidParentheses(self, s):
        max_length = 0
        stack = [-1]  # Initialize stack with -1 to handle edge case for first valid substring

        for i, char in enumerate(s):
            if char == '(':
                # Push the index onto the stack
                stack.append(i)
            else:
                # Pop the last '(' index
                stack.pop()
                if len(stack) == 0:
                    # If stack is empty, push the current index as the new base for future valid substrings
                    stack.append(i)
                else:
                    # Calculate the length of the valid substring
                    max_length = max(max_length, i - stack[-1])

        return max_length

if __name__ == "__main__":
    yes = Solution()

    print(yes.longestValidParentheses("()"))