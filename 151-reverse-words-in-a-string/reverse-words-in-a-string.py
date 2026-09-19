class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s.strip()
        s=s.split()
        rev=s[::-1]
        return " ".join(rev)

        