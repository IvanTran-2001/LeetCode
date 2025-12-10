class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        new_array = [1,3]
        if k == 1:
            return "0"
        
        k -= 4
        
        if k <= 0:
            return "1"
        
        for _ in range(n - 1):
            k, j = add_element(new_array, k)
            if k <= 0:
                return str(j % 2)
            new_array[-1] += 1
            k -= 1
            
            if k <= 0:
                return str(j % 2)

    

def add_element(array, k):
    i = 0
    length = len(array)
    array.append(array[-1] - 1)
    k -= array[-1]
    if k <= 0:
        return [k, length]
    
    for i in range(length - 2, -1, -1):
        array.append(array[i])
        k -= array[i]
        if k <= 0:
            return [k, length + i + 1]
    
    return [k, length + i + 1]
        
        
    

if __name__ == "__main__":
    yes = Solution()
    n = 5
    for i in range(1, 2**n):
        print(yes.findKthBit(n, i), end = '')
    
    print(yes.findKthBit(n, 4))

