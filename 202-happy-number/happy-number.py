class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sett=set()
        while n!=1:
            str_num=str(n)
            n=sum(int(i)**2 for i in str_num)

            if n!=1 and n in sett:
                return False
            else:
                sett.add(n)
        return True