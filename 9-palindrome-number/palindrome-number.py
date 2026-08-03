class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # a = 100
        # b= a[0]
        # print (b)
        # if x[::-1] == x:
        #     return true
        # else:
        #     return false
        str1 = str(x)
        if str1[::-1] == str1:
            return True
        else:
            return False