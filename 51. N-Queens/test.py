class Solution(object):
    def __init__(self):
        self.row = {}
        self.column = {}
        self.diagnalleft = {}
        self.diagnalright = {}
        self.answer = []

    def recurse(self, n, array, z):
        
        if len(self.row) == 4:
            self.answer.append(list(self.row.items()))
        else:
            coordinates = array[z]
            
            r = array[z][0]
            c = array[z][1]
            if not(r in self.row):
                
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
                        self.column[c] = None
                        self.diagnalright[rc] = None
                        self.diagnalleft[lc] = None
                        
                        self.recurse(n, array, z+1)
                        
                        del self.column[c]
                        del self.row[r]
                        
                        del self.diagnalright[rc]
                        del self.diagnalleft[lc]

if __name__ == "__main__":
    yes = Solution()
    yes.recurse(4, [(0,1), (1,3), (2,0), (3,2)], 0)
    print(yes.answer)
