class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        y=int(str(x)[::-1])
        if x==y:
            return True
        else:
            return False
