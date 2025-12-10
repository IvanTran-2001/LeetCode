class Solution(object):

    def intersect(self, n_list):
        new_list = []
        
        # Get the points coordinates for the side of the circles. Example, 0 with a radius of 2 is (-2, 2)
        for i, n in enumerate(n_list):
            new_list.append((i - n, i + n))
        
        # Sort by the left side of the circle
        new_list = sorted(new_list, key=lambda x: x[0])
        summary = 0
        
        # We iterate through each circle once. And for each ONE we determine how many circles are touching the ONE.
        # And each time will add to the total amount (the return value) 
        # To ensure we consider unique circle pairs, every itteration we shorten the input by essentially removing the first element every iteration
        for i in range(len(new_list)  - 1):
            
            #We only need to consider the points of the left side of the circle. If the left side point of any circle is
            #within the range of any circle, it means the circle is a pair no matter what. For example if a circle diameter is (-2, 2) and
            #if the left side of another circle is (1,n) where n can be any positive integer above 1, it will always be a match.
            
            #Hence that means any "left side coords" that is within the particular circle is a match
            
            #This is where these two lines come in, since everything is sorted, we can simply find every "left side coords" that is within a certain range
            #We can do that by using a binary search that will find us the 2 points we need. Then we can simply find the total of circles by just right - left
            #Minusing 2 points gives us the range 
            
            left = self.bisect_left_tuple(i + 1, new_list, new_list[i][0]) 
            right = self.bisect_right_tuple(i + 1, new_list, new_list[i][1]) 
            summary += right - left
        
        return summary
    
    def bisect_left_tuple(self, index, lst, key):
        low, high = index, len(lst)
        while low < high:
            mid = (low + high) // 2
            if lst[mid][0] < key:
                low = mid + 1
            else:
                high = mid
        return low
    
    def bisect_right_tuple(self, index, lst, key):
        low, high = index, len(lst)
        while low < high:
            mid = (low + high) // 2
            if lst[mid][0] <= key:
                low = mid + 1
            else:
                high = mid
        return low
    
if __name__ == "__main__":
    yes = Solution()

    print(yes.intersect([1,5,2,1,4,0]))