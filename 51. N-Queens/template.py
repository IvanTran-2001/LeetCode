class Solution(object):
    def __init__(self):
        self.row = {}
        self.column = {}
        self.diagnalleft = {}
        self.diagnalright = {}
        self.answer = {}
        
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.recurse(n)
        array_dict_keys = []
        new_array = []
        for i in list(self.answer):
            array_dict_keys.append(sorted(list(i), key=lambda x: x[0]))
        
        count = 0
        for i in array_dict_keys:
            new_array.append([])
            for j in i:
                string = ""
                for k in range(n):
                    if j[1] == k:
                        string = string + "Q"
                    else:
                        string = string + "."
                        
                new_array[count].append(string)
            count += 1
                
                        
        return new_array
            
        
    def recurse(self, n):
        if len(self.row) == n:
            coordinates_set = ({(x, y) for x, y in self.row.items()})
            coordinates_set = frozenset(coordinates_set)
            
            self.answer[coordinates_set] = 0
            
        else:
            for r in range(n):
                if not(r in self.row):
                    for c in range(n):
                        if len(self.row) == 0 and c == 1:
                            True
                        
                        lowest = min(r, c)
        
                        if n - c - 1  < r:
                            minus_val = n - c - 1 
                        else:
                            minus_val = r
                        
                        lc = (r-lowest, c-lowest)
                        rc = (r - minus_val, c + minus_val)
                        
                        if not(c in self.column):
                            if not(lc in self.diagnalleft or rc in self.diagnalright):
                                self.row[r] = c
                                self.column[c] = 0
                                self.diagnalright[rc] = 0
                                self.diagnalleft[lc] = 0
                                
                                self.recurse(n)
                                
                                del self.column[c]
                                del self.row[r]
                                
                                del self.diagnalright[rc]
                                del self.diagnalleft[lc]
                            
                    

if __name__ == "__main__":
    yes = Solution()
    print(yes.solveNQueens(7))