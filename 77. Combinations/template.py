class Solution(object):
    def __init__(self):
        self.new_array = []
        
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.recurse(1, n, k, [])
        return self.new_array
    
    def recurse(self, start, end, k, new_list):
        if k == 0:
            self.new_array.append(new_list)
        else:
            if start + k - 1 <= end:
                for i in range(start, end + 1):
                    self.recurse(i + 1, end, k - 1, new_list + [i])
                        
        
                
        

if __name__ == "__main__":
    yes = Solution()

    print(yes.combine(4, 2))

