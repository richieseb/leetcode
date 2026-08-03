class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            val = int(str(x)[::-1])
        else:
            val = -int(str(abs(x))[::-1])
        if val < -2**31 or val > 2**31 - 1:
            return 0
        
        return val