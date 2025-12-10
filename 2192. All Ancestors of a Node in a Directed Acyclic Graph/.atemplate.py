from collections import defaultdict
from typing import List
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        my_dict = defaultdict(list)
        result = [[] for _ in range(n)]
        
        for x, y in edges:
            my_dict[x].append(y)
        
        for i in range(n):
            recurse(result, my_dict, i, i, {})
        
        return result
        

def recurse(result, my_dict, key, append, new_dict):
    for i in my_dict[key]:
        if not(i in new_dict):
            new_dict[i] = None
            result[i].append(append)
            recurse(result, my_dict, i, append, new_dict)
        

    
    

if __name__ == "__main__":
    yes = Solution()
    
    n = 8
    edgeList = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
    print(yes.getAncestors(n, edgeList))
