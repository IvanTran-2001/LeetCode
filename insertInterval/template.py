class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals:
            return [newInterval]
        
        lower = self.bisect(intervals, newInterval[0])
        higher = self.bisect(intervals, newInterval[1])
        
        new_array = [None, None]
        if lower == len(intervals):
            new_array[0] = newInterval[0]
        else:
            if intervals[lower][0] > newInterval[0]:
                new_array[0] = newInterval[0]
            else:
                new_array[0] = intervals[lower][0]
        
        if higher == len(intervals):
            new_array[1] = newInterval[1]
        else:
            if intervals[higher][0] > newInterval[1]:
                new_array[1] = newInterval[1]
            else:
                new_array[1] = intervals[higher][1]
                higher += 1

        
        return intervals[0: lower] + [new_array] + intervals[higher:]

    def bisect(self, lst, key):
        low, high = 0, len(lst)
        while low < high:
            mid = (low + high) // 2
            if lst[mid][0] < key and key > lst[mid][1]:
                    low = mid + 1
            else:
                high = mid
                
        return low
    

if __name__ == "__main__":
    yes = Solution()
    
    

    print(yes.insert([[1,5]],[6,8]))