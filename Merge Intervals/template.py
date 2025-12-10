class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        start = 0
        new_array = []
        index = 0
        intervals = sorted(intervals, key=lambda x: x[0])
        new_array.append(intervals[start])
        
        
        
        for i in range(1, len(intervals)):
            if intervals[i][0] <= intervals[start][1]:
                if intervals[start][1] < intervals[i][1]:
                    new_array[index][1] = intervals[i][1]
            else:
                start = i

                new_array.append(intervals[start])
                index += 1
        
        return new_array
                
                
            
if __name__ == "__main__":
    yes = Solution()

    print(yes.merge([[1,4],[2,3]]))