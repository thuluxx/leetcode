class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # ab = ""
        # for i in range(len(haystack)):
        #     ab = ab+ haystack[i]
                

        if needle in haystack:
            return haystack.index(needle)
        elif needle not in haystack:
            return -1