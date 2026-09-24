class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Clean the string: keep only alphanumeric and convert to lowercase
        filtered = "".join(ch.lower() for ch in s if ch.isalnum())
        
        l, r = 0, len(filtered) - 1
        while l < r:
            if filtered[l] != filtered[r]:
                return False
            l += 1
            r -= 1
        return True