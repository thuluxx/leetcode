class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        a=s.split()
        b = a[-1]
        return len(b)
        # b = len(s)-1
        # # print(s[a])
        # a = (s.split(" "))
        # c = a[-1]
        # d = len(c)
        # return d