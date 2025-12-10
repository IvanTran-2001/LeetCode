class Solution(object):
    def strStr(self, haystack, needle):
        haystack = haystack.replace(needle, '1')
        k = 0
        for i in range(len(haystack)):
            if haystack[i] == '1':
                return k 
            k += 1

        return -1
