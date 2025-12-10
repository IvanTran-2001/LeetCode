import math
class Solution(object):
    def numberOfArrays(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        length_K = self.count_digits_logarithm(k)
        memory_track = [0] * (length_K + 2)
        m_t_index = 2
        
        memory_track[0] = 1
        memory_track[1] = 1
        
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
        
        if len(s) < len(str(k)):
            return 2**(len(transform_array)-1)
        
        end = len(transform_array) - 1
        start = end - 1
        
        while start >= 0:
            combine_num = self.combine(transform_array, start, end + 1)
            if combine_num <= k:
                memory_track[m_t_index] = 0
                for i in range(end-start + 1):
                    
                    i_index = m_t_index - (i + 1)
                    
                    if i_index < 0:
                        i_index = len(memory_track) + i_index
                        
                    if i_index >= len(memory_track):
                        i_index = i_index - len(memory_track)
                        
                    memory_track[m_t_index] += memory_track[i_index]
                    
                m_t_index += 1
                if m_t_index >= len(memory_track):
                    m_t_index = 0
                
                start -= 1
            else:
                end -= 1
        
        m_t_index -= 1
        
        return memory_track[m_t_index] % MOD
        
    
    def count_digits_logarithm(self, n):
        if n == 0:
            return 1
        return int(math.log10(abs(n))) + 1
    
    def combine(self, arr, start, end):
    
        sliced_gen = self.sliced_generator(arr, start, end)
        combined_str = ''.join(sliced_gen)
        combined_int = int(combined_str)
        return combined_int
    
    def sliced_generator(self, array, start, end):
        for i in range(start, end):
            yield str(array[i])
        
            
if __name__ == "__main__":
    yes = Solution()

    print(yes.numberOfArrays("600342244431311113256628376226052681059918526204", 703))

