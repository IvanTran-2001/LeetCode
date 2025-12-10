class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Incomplete
        """
        ind=0
        res=0
        x=-1
        y=-1
        n=len(nums)
        for i in range(n):
            if nums[i]==0:
                if ind==0:
                    ind=1
                    x=y
                    y=i
                else:
                    if res < i-x-2:
                        res = i-x-2
                        if res > (n - i + 1):
                            x=y
                            y=i
                            break
                    x=y
                    y=i
        if ind==0:
            return n-1
        else:
            res=max(res,n-x-2)
            return res