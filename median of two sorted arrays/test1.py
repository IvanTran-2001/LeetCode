class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        i = -1
        j = -1
        iLen = len(nums1)
        jLen = len(nums2)
        
        bal = True
        combine = (len(nums1) + len(nums2))
        while i + j + 2 <= combine//2:
            
            if i+1 < iLen and j+1 < jLen:
                if nums1[i+1] < nums2[j+1]:
                    i += 1
                    bal = True
                else:
                    j += 1
                    bal = False
                    
            elif i+1 < iLen:
                i += 1
                bal = True
                
            elif j+1 < jLen:
                j += 1
                bal = False
        
        if combine%2 == 0:
            if j == -1:
                return (nums1[i] + nums1[i-1])/2.0
            if i == -1:
                return (nums2[j] + nums2[j-1])/2.0
            
            if bal and i > 0 and (nums1[i - 1] > nums2[j]):
                return (nums1[i] + nums1[i - 1])/2.0
            
            if not bal and j > 0 and (nums2[j - 1] > nums1[i]):
                return (nums2[j] + nums2[j - 1])/2.0
            
            return (nums1[i] + nums2[j])/2.0
            
        if bal:
            return nums1[i]
        else:
            return nums2[j]
                
            
                
            
if __name__ == "__main__":
    test = Solution()
    print(test.findMedianSortedArrays([3], [1,2,4,5,6]))
    