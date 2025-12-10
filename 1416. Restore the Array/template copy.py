import math
class Solution(object):
    def numberOfArrays(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        #Requirement by task
        MOD = 10**9 + 7
        
        length_K = self.count_length(k)
        
        #Keep track of previous Fibonacci pattern
        #Only need to keep track of previous Fibonacci values length of K.
        # +1 is for the first Fibonacci value which is the default 1.
        memory_track = [0] * (length_K + 1)
        m_t_index = 2
        
        #Starting the Fibonacci Pattern
        memory_track[0] = 1
        memory_track[1] = 1
        
        #Transforming string into integers to seperate
        #Numbers with Zeroes such as 5000
        transform_array = []
        for i in s:
            c = int(i)
            if c == 0:
                transform_array[-1] *= 10
                if transform_array[-1] > k:
                    return 0
            else:
                if c > k:
                    return 0
                transform_array.append(c)
        
        #If no leading zeroes, return every combination amount
        if len(s) < len(str(k)):
            return 2**(len(transform_array)-1)
        
        #Doing two pointers instead of slicing arrays
        end = len(transform_array) - 1
        start = end - 1
        
        #Instead of using strings to combine numbers, we use actual math
        combine_num = transform_array[end]
        
        #First 2 numbers are combined, eg 6 and 7 will become 67
        combine_num += transform_array[start] * 10**(self.count_length(combine_num))
        
        #Scanning backwards
        while start >= 0:
            
            
            if combine_num <= k:
                
                #This array will be cycled, hence we need to 
                #replace previous/useless memories
                memory_track[m_t_index] = 0
                for i in range(end-start + 1):
                    
                    i_index = m_t_index - (i + 1)
                    
                    #m_t_index is the starting point of the array, 
                    # it can start anywhere with in the array
                    #hence when going backwards, the index can go 
                    # negative which this will bring back to valid index.
                    if i_index < 0:
                        i_index = len(memory_track) + i_index
                    
                    #Depending on how many valid integers with in the search 
                    # range, it will track the same amount backwards.
                    #Example, k = 5000 and current search is 4990, that is 4, 
                    # 9 and 90 meaning 3 numbers, it will sum the last 3
                    #Fibonacci values.  (Numbers can't start with 0 hence 90, not 9 and 0) 
                    memory_track[m_t_index] = (memory_track[m_t_index] + memory_track[i_index]) % MOD
                    
                #Move to next space to replace in Fibonacci (memory track)
                m_t_index += 1
                #If memory space is full, we can cycle back to the 
                # start and replace memory again
                if m_t_index >= len(memory_track):
                    m_t_index = 0
                
                start -= 1
                #Adding next number to the front
                combine_num += transform_array[start] * 10**(self.count_length(combine_num))
            else:
                #If the number is larger than k, we shrink the 
                # combine num by moving the end point
                #Removing the back
                combine_num -= transform_array[end]
                combine_num //= 10**(self.count_length(transform_array[end]))
                end -= 1
        
        #End of array is the answer. However, the end of the array 
        # isn't literally at the end but somewhere in the array.
        #We can track by simply getting the starting point and minus by 1.
        m_t_index -= 1
        
        return memory_track[m_t_index]
        
    #Getting length of an integer runtime(O(1))
    def count_length(self, n):
        if n == 0:
            return 1
        return int(math.log10(abs(n))) + 1
        
            
if __name__ == "__main__":
    yes = Solution()

    print(yes.numberOfArrays("226", 26))

