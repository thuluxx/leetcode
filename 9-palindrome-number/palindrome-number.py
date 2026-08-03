class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str1 = str(x)
        if str1[::-1] == str1:
            return True
        else:
            return False