class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        temp = nums1[0:m]
        i=0
        j=0
        jTrue = True
        iTrue = True
        if nums1 == [] or m == 0:
            iTrue = False
        
        if nums2 == [] or n == 0:
            jTrue = False
            
        while jTrue or iTrue:
            if not iTrue or (jTrue and (temp[i] > nums2[j])):
                nums1[i + j] = nums2[j]
                j += 1
                if j == n:
                    jTrue = False
            else:
                nums1[i + j] = temp[i]
                i += 1
                if i == m:
                    iTrue = False

if __name__ == "__main__":
    yes = Solution()
    nums1 = [1]
    nums2 = []
    yes.merge(nums1, 1, nums2, 0)
    print(nums1)