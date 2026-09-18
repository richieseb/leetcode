class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        # Step 1: Commutativity check
        if str1 + str2 != str2 + str1:
            return ""
        
        # Step 2: Euclidean algorithm for GCD of lengths
        a, b = len(str1), len(str2)
        while b:
            a, b = b, a % b
            
        # Step 3: Prefix slice using GCD length (stored in 'a')
        return str1[:a]